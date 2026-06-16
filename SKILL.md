---
name: auto-name-pics-skill
description: Rename camera photos in place using EXIF metadata and the embedded filename number.
---

# Auto Name Pics

Use this skill when you need to rename photo files in place from their EXIF metadata.

## Workflow

1. Read the camera model from EXIF metadata.
2. Read the photo capture date from EXIF metadata.
3. Extract the embedded numeric identifier from the original filename.
4. Rename the file in place using the pattern `CAMERA-NUMBER YYYYMMDD`.

## Rules

- Do not modify image contents.
- Do not move files to another directory.
- Preserve the original extension.
- Format the embedded number as six digits with leading zeroes when needed.

## Implementation

- Use [`scripts/rename_photos.py`](scripts/rename_photos.py) for the renaming logic.
- The script depends on `exiftool` being installed and available on `PATH`.
- Sample files currently exist only for Ricoh GR4 under [`assets/samples/ricoh-gr4/`](assets/samples/ricoh-gr4/).
- Skill UI metadata lives in [`agents/openai.yaml`](agents/openai.yaml).

## Examples

- `R0003565.JPG` -> `GR-IV-003565 20260611.JPG`
- `R0003565.DNG` -> `GR-IV-003565 20260611.DNG`
