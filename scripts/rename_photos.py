#!/usr/bin/env python3
"""Rename photos in place from EXIF metadata and embedded file number.

This script expects `exiftool` to be installed and available on PATH.
It reads metadata from each photo, derives a camera prefix from the model,
uses the capture date, and renames the file without changing its contents or
moving it to another directory.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DATE_KEYS = (
    "DateTimeOriginal",
    "CreateDate",
    "MediaCreateDate",
    "TrackCreateDate",
)

PHOTO_EXTENSIONS = {
    ".arw",
    ".dng",
    ".heic",
    ".jpeg",
    ".jpg",
    ".nef",
    ".orf",
    ".pef",
    ".png",
    ".raf",
    ".rw2",
    ".tif",
    ".tiff",
}


@dataclass(frozen=True)
class PhotoMetadata:
    path: Path
    model: str
    capture_date: str
    file_number: str


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rename photos in place using EXIF metadata and the embedded file number."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Photo files or directories to process.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned renames without changing any files.",
    )
    return parser.parse_args(argv)


def ensure_exiftool() -> str:
    exiftool = shutil.which("exiftool")
    if not exiftool:
        raise SystemExit(
            "error: exiftool is required but was not found on PATH. "
            "Install exiftool and try again."
        )
    return exiftool


def iter_photo_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(
                sorted(
                    p
                    for p in path.rglob("*")
                    if p.is_file() and p.suffix.lower() in PHOTO_EXTENSIONS
                )
            )
        elif path.is_file():
            if path.suffix.lower() in PHOTO_EXTENSIONS:
                files.append(path)
        else:
            raise SystemExit(f"error: path does not exist: {path}")
    return files


def read_metadata(exiftool: str, path: Path) -> PhotoMetadata:
    cmd = [
        exiftool,
        "-j",
        "-Model",
        "-FileNumber",
        *[f"-{key}" for key in DATE_KEYS],
        str(path),
    ]
    completed = subprocess.run(
        cmd,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(completed.stdout)
    if not payload:
        raise SystemExit(f"error: no metadata returned for {path}")
    data = payload[0]

    model = str(data.get("Model", "")).strip()
    if not model:
        raise SystemExit(f"error: missing camera model metadata for {path}")

    capture_date = ""
    for key in DATE_KEYS:
        value = str(data.get(key, "")).strip()
        if value:
            capture_date = normalize_capture_date(value)
            break
    if not capture_date:
        raise SystemExit(f"error: missing capture date metadata for {path}")

    file_number = str(data.get("FileNumber", "")).strip()

    return PhotoMetadata(
        path=path,
        model=model,
        capture_date=capture_date,
        file_number=file_number,
    )


def normalize_capture_date(value: str) -> str:
    match = re.search(r"(\d{4}):(\d{2}):(\d{2})", value)
    if not match:
        match = re.search(r"(\d{4})-(\d{2})-(\d{2})", value)
    if not match:
        raise SystemExit(f"error: unsupported capture date format: {value}")
    return "".join(match.groups())


def camera_prefix(model: str) -> str:
    if re.search(r"\bNIKON\s+Z\s+f\b", model, flags=re.IGNORECASE):
        return "Zf"

    normalized = re.sub(r"^RICOH\s+", "", model.strip(), flags=re.IGNORECASE)
    normalized = normalized.upper()
    normalized = normalized.replace("GR IV", "GR-IV")
    normalized = normalized.replace("GR IIIX", "GR-IIIX")
    normalized = normalized.replace("GR III", "GR-III")
    normalized = normalized.replace("GR II", "GR-II")
    normalized = normalized.replace("GR I", "GR-I")
    normalized = re.sub(r"[^A-Z0-9-]+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized).strip("-")
    if not normalized:
        raise SystemExit(f"error: could not derive camera prefix from model: {model}")
    return normalized


def embedded_number(path: Path) -> str:
    digits = re.findall(r"\d+", path.stem)
    if not digits:
        raise SystemExit(f"error: no embedded number found in filename: {path.name}")
    value = int(digits[-1])
    return f"{value:06d}"


def camera_number(photo: PhotoMetadata) -> str:
    if re.search(r"\bNIKON\s+Z\s+f\b", photo.model, flags=re.IGNORECASE):
        if not photo.file_number:
            raise SystemExit(f"error: missing file number metadata for {photo.path}")
        return photo.file_number
    return embedded_number(photo.path)


def build_target_name(photo: PhotoMetadata) -> str:
    path = photo.path
    model = photo.model
    capture_date = photo.capture_date
    prefix = camera_prefix(model)
    number = camera_number(photo)
    separator = "_" if prefix == "Zf" else "-"
    return f"{prefix}{separator}{number} {capture_date}{path.suffix}"


def rename_photo(photo: PhotoMetadata, *, dry_run: bool) -> None:
    target_name = build_target_name(photo)
    target_path = photo.path.with_name(target_name)
    if target_path == photo.path:
        print(f"unchanged: {photo.path.name}")
        return
    if target_path.exists():
        raise SystemExit(f"error: target already exists: {target_path}")
    if dry_run:
        print(f"would rename: {photo.path.name} -> {target_path.name}")
        return
    photo.path.rename(target_path)
    print(f"renamed: {photo.path.name} -> {target_path.name}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    ensure_exiftool()

    photo_files = iter_photo_files(args.paths)
    if not photo_files:
        raise SystemExit("error: no files to process")

    for path in photo_files:
        metadata = read_metadata("exiftool", path)
        rename_photo(metadata, dry_run=args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
