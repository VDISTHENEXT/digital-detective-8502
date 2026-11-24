# Mission 6 — Git and GitHub

## 1. Task / objective
Understand modern version control workflows using Git and GitHub:
- Practise core Git commands: staging, committing, viewing repository status, and inspecting history.
- Explain the key conceptual difference between staging (`git add`) and committing (`git commit`).
- Create and push a feature branch named `update-about` with a new "My Learning" section added to the root `README.md`.
- Document the Pull Request workflow and explain why branching and PRs are vital for team collaboration.
- Build a concise glossary of fundamental Git operations.

## 2. Work completed

### Task 6.1 — Basic Git Workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Shows which files are currently tracked, untracked, modified, or staged for the next commit. |
| **Stage selected changes (`git add <file>`)** | Moves specified file modifications into the staging area (index) so they will be included in the next commit. |
| **Create a commit (`git commit -m "<msg>"`)** | Records a permanent snapshot of all currently staged changes into local history with an author name, timestamp, and unique hash. |
| **View commit history (`git log`)** | Displays a chronological log of previous commits showing commit hashes, author details, dates, and commit messages. |

#### Difference between Staging and Committing
- **Staging (`git add`):** Acts as a drafting/preparation table (the index). It lets you selectively choose which exact files and lines of code should be bundled into the next snapshot. Staging does not save a permanent history record.
- **Committing (`git commit`):** Takes a permanent, immutable snapshot of whatever is currently sitting on the staging table. Each commit receives a unique SHA-1 identifier and becomes an official milestone in the project's historical timeline.

---

### Task 6.2 — Creating and Using a Branch (`update-about`)

1. Created and switched to the new branch:
   ```bash
   git checkout -b update-about
   ```
2. Edited the root `README.md` to add a new section titled **"My Learning"**, highlighting three core takeaways:
   - Operating system fundamentals (process scheduling, PIDs, permissions).
   - Command-line proficiency (flags, file operations, Unix pipes).
   - Data representation (binary, decimal, hexadecimal, and UTF-8 encoding).
3. Staged and committed the change on branch `update-about`:
   ```bash
   git add README.md
   git commit -m "Add My Learning section to root README"
   ```
4. Published the branch to GitHub:
   ```bash
   git push -u origin update-about
   ```

---

### Task 6.3 — Pull Request (PR) Workflow

- **PR Target:** `update-about` into `main`.
- **Compare & PR URL:** `https://github.com/VDISTHENEXT/digital-detective-8502/pull/new/update-about`
- **Current Status:** Branch published and PR available for instructor review (left unmerged as instructed unless required).
- **Why branches and Pull Requests are useful:**
  - **Branching:** Allows multiple developers to work on features, bug fixes, or experiments simultaneously in complete isolation without disturbing the stable production code on `main`.
  - **Pull Requests:** Provide a collaborative review forum before changes merge. Teammates can review visual diffs, leave inline comments, run automated tests, and ensure code quality and security standards before integrating the code into the main branch.

---

### Task 6.4 — Git Command Glossary

| Git operation | One-line explanation in your own words |
| :--- | :--- |
| **`git init`** | Initialises a new, empty Git version-control repository in the current folder. |
| **`git status`** | Displays working tree status, showing staged, unstracked, and modified files. |
| **`git add`** | Adds changes from the working directory into the staging area (index). |
| **`git commit`** | Saves a permanent snapshot of staged changes into the local repository history. |
| **`git log`** | Displays the commit history showing previous commits and their messages. |
| **`git branch`** | Lists existing branches or creates a new branch pointer. |
| **`git switch` / `git checkout`** | Switches from one working branch to another. |
| **`git push`** | Uploads local branch commits to the remote GitHub repository. |
| **`git pull`** | Fetches and integrates changes from the remote repository into the local branch. |

## 3. Commands / tools used
- `git status`: Inspected repository state before and after edits.
- `git checkout -b update-about`: Created and checked out the feature branch.
- `git add`: Staged modified files.
- `git commit -m "..."`: Created atomic commits with clear messages.
- `git push -u origin update-about`: Pushed the feature branch to GitHub.
- `git checkout main`: Switched back to the main branch.
- `git log --oneline`: Inspected commit graph and history.

## 4. My understanding
Version control is like a safety net and time machine for software development. Git tracks changes locally at the file system level without requiring internet connectivity. GitHub provides a centralized cloud hosting platform that enables code review, collaboration, and issue tracking. Branching allows engineers to explore ideas and develop features without risk to stable code, while Pull Requests establish a structured review gate before code becomes part of the shared main branch.

## 5. Difficulties faced
- Remembering whether `git push` pushes all branches automatically or requires specifying the branch name.
- Ensuring the `update-about` branch stayed separate from `main` without accidentally merging before review.

## 6. How I resolved them
- Used `git push -u origin update-about` to explicitly push the feature branch and configure upstream tracking.
- Checked `git branch` and `git status` after switching back to `main` to confirm that `main` remained clean.

## 7. Evidence / files
- `mission-06-git-github/README.md`
- Branch `update-about` published to GitHub (`https://github.com/VDISTHENEXT/digital-detective-8502/tree/update-about`)
- Root `README.md` updated on `update-about` branch

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Branch: `main`
- Status: Staged, committed, and pushed to GitHub.
