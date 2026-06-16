# auto-name-pics-skill

Repo for a skill that renames camera photos in place using EXIF metadata.

## What it does

- Reads the camera model from metadata
- Reads the capture date from metadata
- Extracts the embedded filename number
- Renames files in place without modifying contents or moving them

## Install

To use this as a skill, place the skill folder where your skill manager expects it.

The skill package itself is the repository content, centered on:

- [`SKILL.md`](./SKILL.md)
- [`agents/openai.yaml`](./agents/openai.yaml)
- [`scripts/rename_photos.py`](./scripts/rename_photos.py)
- [`assets/samples/ricoh-gr4/`](./assets/samples/ricoh-gr4/)

If you are managing skills locally, copy this folder into your skills location and keep the `SKILL.md` file at the root of the skill folder.

If you want to run the renamer directly, install `exiftool` first and then run:

```bash
python3 scripts/rename_photos.py assets/samples/ricoh-gr4
```

### Install exiftool

On macOS with Homebrew:

```bash
brew install exiftool
```

On other systems, install `exiftool` using your package manager or from the ExifTool distribution provided by Phil Harvey.

## Current sample coverage

- Ricoh GR4 only, under [`assets/samples/ricoh-gr4/`](./assets/samples/ricoh-gr4/)

## Development records

See [`prompts.md`](./prompts.md) for the repo prompt log.
