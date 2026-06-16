# agents

This skill exists to rename picture files automatically using the camera metadata and the date taken.

## Purpose

- Turn unnamed or poorly named photos into consistent, useful filenames.
- Prefer metadata-based naming over manual renaming.
- Keep the workflow focused on picture files and naming logic.

## File Handling

- Never modify photo contents.
- Never move files to a different directory.
- Only rename files in place.

## Naming Convention

- Use the camera model prefix, then a space, then the embedded file number, then another space, then the ISO date the picture was taken.
- Example: `GR-IV-003414 20260611`
- The prefix should come from the camera model.
- The number should come from the numeric value embedded in the original filename, formatted as six digits with leading zeroes when needed.
- The date should be formatted as `YYYYMMDD`.

## Working Notes

- Automatically record major development prompts in [`prompts.md`](./prompts.md) as work happens.
- Use timestamped entries with `Goal`, `Prompt Summary`, and `Technical Context`.
- Paraphrase messy or repetitive prompts in the log instead of copying them verbatim.
- Keep the log current whenever a substantial prompt changes direction, scope, or implementation details.
- Sample photos currently exist only for the Ricoh GR4 in [`assets/samples/ricoh-gr4/`](./assets/samples/ricoh-gr4/).
- Skill metadata lives under [`agents/`](./agents/).
