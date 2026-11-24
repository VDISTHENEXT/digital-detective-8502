# Mission 0 - Create your GitHub workspace

## 1. Task / objective
Create the `digital-detective-8502` workspace and folder structure for all missions, verify required tools, and prepare the repository for GitHub.

## 2. Work completed
- Checked `python3` and `git` versions in Terminal.
- Created the `digital-detective-8502` project folder.
- Created all required mission folders (`mission-00-setup` through `mission-08-final-report`), `evidence/`, and the starter `README.md` and `number_converter.py` files.
- Wrote the root `README.md` with the mission index and workflow note.

## 3. Commands / tools used
- `python3 --version` and `git --version`: Checked that Python 3 (`Python 3.14.7`) and Git (`git version 2.55.0`) were available.
- `mkdir -p` and `cd`: Created the project directory and mission subfolders and moved into the project folder.
- `touch`: Created empty Markdown files, `number_converter.py`, and `evidence/.gitkeep`.
- Code editor: Edited and saved `README.md` and mission documentation.

## 4. My understanding
A repository tracks project files and their change history over time. Organizing the assignment into separate mission folders keeps each mission's work isolated so each step can be completed, documented, committed, and pushed cleanly in order.

## 5. Difficulties faced
Hit a `zsh: parse error near '&&'` when running a command that still contained `<` and `>` around `<last-4-digits>`.

## 6. How I resolved them
Replaced `<last-4-digits>` with `8502` without angle brackets and re-ran the command.

## 7. Evidence / files
- `README.md`
- `mission-00-setup/README.md`
- Mission folders `mission-00-setup` through `mission-08-final-report`, `mission-05-numbers-data/number_converter.py`, and `evidence/`

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Target branch: `main`
- Remote repository: `https://github.com/VDISTHENEXT/digital-detective-8502.git`