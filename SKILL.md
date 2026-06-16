---
name: auto-name-pics-skill
description: Rename camera photos in place using EXIF metadata and the embedded filename number.
---

# Auto Name Pics

Use this skill when you need to rename photo files in place from their EXIF metadata.

## Workflow

1. Read the camera model from EXIF metadata.
2. Read the photo capture date from EXIF metadata.
3. Extract the camera-specific number source.
4. Rename the file in place using the camera-specific pattern.

## Rules

- Do not modify image contents.
- Do not move files to another directory.
- Preserve the original extension.
- Ricoh GR IV uses `GR-IV-<six-digit filename number> YYYYMMDD`.
- Nikon Z f uses `Zf_<file number from EXIF> YYYYMMDD`.
- Format the Ricoh embedded number as six digits with leading zeroes when needed.

## Implementation

- Use [`scripts/rename_photos.py`](scripts/rename_photos.py) for the renaming logic.
- The script requires Python 3.
- The script depends on `exiftool` being installed and available on `PATH`.
- For macOS, install ExifTool so `exiftool` runs from Terminal. If `/usr/local/bin` is not already on `PATH`, add it. For Windows, install the executable version, rename `exiftool(-k).exe` to `exiftool.exe`, and place `exiftool.exe` plus `exiftool_files` in a folder on `PATH`.
- Supported camera families currently include Ricoh GR IV and Nikon Z f.
- Skill UI metadata lives in [`agents/openai.yaml`](agents/openai.yaml).

## Examples

- `R0003565.JPG` -> `GR-IV-003565 20260611.JPG`
- `R0003565.DNG` -> `GR-IV-003565 20260611.DNG`
- `DSC_8690.JPG` -> `Zf_8690 20260616.JPG`
- `DSC_8690.NEF` -> `Zf_8690 20260616.NEF`
