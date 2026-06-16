# Prompt Log

Record major development prompts here.

## Format

Use a timestamped title for each entry, followed by these sections:

- `Goal`
- `Prompt Summary`
- `Technical Context`

## Guidance

- Keep the summary concise and focused on the engineering intent.
- Paraphrase prompts when the original request is messy, repetitive, or verbose.
- Preserve only the technical meaning, not the exact wording.

## Entry Template

### 2026-06-16 10:45 - Short descriptive title

**Goal**

What this work is trying to achieve.

**Prompt Summary**

Brief paraphrase of the request or discussion.

**Technical Context**

Relevant files, constraints, implementation details, or environment notes.

## Backfilled Entries

### 2026-06-16 - Add prompt logging

**Goal**

Create a repo-local prompt log for major development prompts.

**Prompt Summary**

Add `prompts.md` with a timestamped title format and `Goal`, `Prompt Summary`, and `Technical Context` sections. Prefer paraphrasing when the original prompt is messy or repetitive.

**Technical Context**

Repo had only a basic README at the time; no prompt log existed yet.

### 2026-06-16 - Document skill purpose

**Goal**

Capture the purpose of the skill in a dedicated notes file.

**Prompt Summary**

Add `agents.md` to describe the skill as a picture-renaming tool and keep the repo notes separate from the skill implementation.

**Technical Context**

This repo was being used as a local skill package, not just a code project.

### 2026-06-16 - Create Ricoh GR4 sample folder

**Goal**

Create a camera-specific folder for sample photos.

**Prompt Summary**

Add a sample folder for Ricoh GR4 files so test images can be stored and renamed in place without moving or modifying them.

**Technical Context**

The repository started with no sample image structure.

### 2026-06-16 - Define rename rule

**Goal**

Lock down the exact filename format.

**Prompt Summary**

Use the camera model prefix, the six-digit embedded file number, and the ISO capture date, separated by spaces, while keeping files in place only.

**Technical Context**

Example target names were derived from Ricoh GR4 samples and EXIF metadata.

### 2026-06-16 - Implement EXIF renamer

**Goal**

Build the actual photo renaming program.

**Prompt Summary**

Implement a Python renamer that reads camera model and capture date from EXIF metadata, extracts the embedded file number from the filename, and renames JPG/DNG files in place.

**Technical Context**

The script depends on `exiftool` for metadata extraction across JPEG and DNG.

### 2026-06-16 - Package as a skill

**Goal**

Reorganize the repo as a proper skill package.

**Prompt Summary**

Move the implementation into the standard skill structure with `SKILL.md`, a scripts folder, and skill metadata under `agents/`.

**Technical Context**

The repo needed to function as a local skill without installing into a Codex home directory.

### 2026-06-16 - Use local agents folder

**Goal**

Match the user's local skill storage convention.

**Prompt Summary**

Switch the metadata folder to the normal `agents/` path and avoid the accidental `a.agents` naming.

**Technical Context**

The skill remained local in the repository while metadata lived alongside it.

### 2026-06-16 - Test Ricoh GR4 files

**Goal**

Verify the renamer against the sample camera files.

**Prompt Summary**

Run the script on the Ricoh GR4 JPG and DNG, confirm the EXIF model and date, and rename the files in place using the derived target names.

**Technical Context**

`exiftool` was installed and the files reported `RICOH GR IV` with a capture date of `2026:06:16 07:36:22`.

### 2026-06-16 - Restore traditional skill layout

**Goal**

Correct the accidental folder naming confusion.

**Prompt Summary**

Move the metadata back into a traditional `agents/` folder and keep the skill layout canonical.

**Technical Context**

The repo should remain a normal local skill package rather than inventing a custom folder name.

### 2026-06-16 - Record current sample coverage

**Goal**

State which sample cameras have been added so far.

**Prompt Summary**

Document that Ricoh GR4 is the only camera sample set present at the moment.

**Technical Context**

The sample folder structure currently contains only the Ricoh GR4 examples.

### 2026-06-16 - Make prompt logging automatic

**Goal**

Treat prompt logging as part of the repo workflow.

**Prompt Summary**

Update the repo notes so major development prompts are recorded in `prompts.md` as the work progresses.

**Technical Context**

The user wants the repo itself to preserve prior prompts without manual follow-up steps.
