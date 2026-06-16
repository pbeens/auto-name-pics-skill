# auto-name-pics-skill
Skill package for renaming pictures in place based on EXIF camera metadata and capture date.

See [prompts.md](./prompts.md) for the development prompt log format and recorded entries.
Skill metadata is stored locally under [`a.agents/`](./a.agents/), not in a Codex home folder.

## Usage

The skill is implemented as a Python renamer in [`scripts/rename_photos.py`](./scripts/rename_photos.py).

It reads EXIF metadata from each file, determines the camera model and capture date, and renames files in place without modifying their contents or moving them.

The script expects `exiftool` to be installed on your system and available on `PATH`.

For example, on macOS you can install it with Homebrew:

```bash
brew install exiftool
```
