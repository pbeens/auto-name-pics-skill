# auto-name-pics-skill

Repo for a skill that renames camera photos in place using EXIF metadata.

## What it does

- Reads the camera model from metadata
- Reads the capture date from metadata
- Extracts the camera-specific number source
- Renames files in place without modifying contents or moving them
- Supports DJI drones, Ricoh GR IV, and Nikon Z f files

## Install

To use this as a skill, place the skill folder where your skill manager expects it.

You also need Python 3 and ExifTool available on your machine.

The skill package itself is the repository content, centered on:

- [`SKILL.md`](./SKILL.md)
- [`agents/openai.yaml`](./agents/openai.yaml)
- [`scripts/rename_photos.py`](./scripts/rename_photos.py)

If you are managing skills locally, copy this folder into your skills location and keep the `SKILL.md` file at the root of the skill folder.

### Install exiftool

ExifTool does not need a formal installation to run, but it does need to be on your `PATH` for this skill. The official install page says the MacOS package installs `exiftool` so you can run it from Terminal, and if `/usr/local/bin` is not already in `PATH`, you should add it. For Windows, download the Windows executable, rename `exiftool(-k).exe` to `exiftool.exe`, and move `exiftool.exe` plus the `exiftool_files` folder into a directory on `PATH`.

macOS:

```bash
brew install exiftool
```

Windows:

- Download the Windows executable from the official ExifTool site.
- Rename `exiftool(-k).exe` to `exiftool.exe`.
- Put `exiftool.exe` and `exiftool_files` in a folder that is on `PATH`.

If you want to run the renamer directly after installing ExifTool, run:

```bash
python3 scripts/rename_photos.py assets/samples/ricoh-gr4
```

On Windows, use the equivalent Python launcher command if needed, such as `python`.

## Development records

See [`prompts.md`](./prompts.md) for the repo prompt log.
