# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Learn and practise basic Terminal operations to manage files and directories from the command line:
- Run and document core filesystem navigation and manipulation commands.
- Safely practise creating, appending, copying, moving, and reading files inside a dedicated `terminal-practice` folder.
- Understand command options/flags and how pipes connect processes.
- Check package manager status (Homebrew) and understand its role in software management.

## 2. Work completed

### Task 2.1 — Basic Terminal Operations Reference

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the absolute path of the current working directory. | Displayed `/.../digital-detective-8502`, confirming the shell was located inside the assignment root. |
| **Directory listing (`ls`)** | Lists names of visible files and folders in the current directory. | Displayed root folders such as `mission-00-setup`, `mission-01-computer-basics`, and `README.md`. |
| **Detailed listing (`ls -l`)** | Lists directory contents in long format including permissions, owner, file size, and timestamp. | Output showed lines starting with permissions like `drwxr-xr-x` and `-rw-r--r--`, along with file sizes and modification dates. |
| **Change directory (`cd ..` and `cd digital-detective-8502`)** | Changes the working directory to the parent folder or into a target child folder. | Running `cd ..` changed path to parent directory; running `cd digital-detective-8502` returned to the project folder. |
| **Create directory (`mkdir -p terminal-practice`)** | Creates a new folder. The `-p` flag prevents errors if the folder already exists. | A new folder named `terminal-practice` was created inside the project root. |
| **Create empty file (`touch terminal-practice/sample.txt`)** | Creates an empty file or updates the timestamp of an existing file. | An empty file `sample.txt` was created with a size of 0 bytes. |
| **Copy file (`cp sample.txt sample_backup.txt`)** | Copies a file from source to a new destination while leaving the source intact. | Created an exact duplicate `sample_backup.txt` with identical contents. |
| **Move / rename file (`mv sample_backup.txt sample_archive.txt`)** | Moves or renames a file to a new name or location. | `sample_backup.txt` was renamed to `sample_archive.txt`; the old filename ceased to exist. |
| **Display file contents (`cat sample.txt`)** | Concatenates and prints file contents directly to standard output. | Displayed both lines of text stored in `sample.txt` on the screen. |

---

### Task 2.2 — Safe File Changes Practice

Inside `terminal-practice/`, the following safe operations were performed:
1. Created `sample.txt` with an initial line: `echo "First line: Terminal practice file" > sample.txt`
2. Appended a second line without removing the first: `echo "Second line: Appending text without overwriting" >> sample.txt`
3. Confirmed both lines using `cat sample.txt`.
4. Made a backup copy: `cp sample.txt sample_backup.txt`
5. Renamed the backup: `mv sample_backup.txt sample_archive.txt`

#### Concept Questions:
- **Replacing vs. adding text:** The `>` redirection operator overwrites or truncates an existing file, wiping previous content. The `>>` operator appends new data to the end of the file, preserving all existing contents.
- **Copying vs. moving:** `cp` creates an independent duplicate file so two copies exist. `mv` changes the path or name of the existing file, leaving only one file.
- **Current-directory display:** `pwd` gives the exact full path from the filesystem root (`/`), showing where relative file paths will resolve.
- **Directory listing:** `ls` allows us to inspect what files and folders exist without needing a graphical window like Finder.

---

### Task 2.3 — Flags and Pipes

1. **Flags comparison (`ls` vs `ls -lah`):**
   - `ls`: Simple column of visible filenames.
   - `ls -lah`: 
     - `-l`: Detailed long listing (permissions, link count, owner, group, size, date).
     - `-a`: Shows all files, including hidden entries like `.` (current directory), `..` (parent directory), and `.gitkeep`.
     - `-h`: Formats file sizes into human-readable units (e.g., `83B`, `128B`, `4K`).

2. **Pipes exploration (`ls -l | head -n 5`):**
   - The pipe operator (`|`) takes the standard output (`stdout`) of the command on the left and connects it directly to the standard input (`stdin`) of the command on the right.
   - In `ls -l | head -n 5`, `ls -l` generates the complete directory listing, and `head -n 5` filters it so only the first 5 lines appear on screen. This is helpful when browsing directories with hundreds of files.

---

### Task 2.4 — Package Managers (Homebrew)

- **Verification:** Ran `which brew` and `brew --version`.
- **Observation:** Homebrew 7.0.7 is installed at `/opt/homebrew/bin/brew`. Listing installed packages via `brew list --formula` revealed packages including `git`, `cowsay`, `gettext`, and `pcre2`.
- **Purpose of package managers:** A package manager is a tool that automates searching, downloading, compiling, installing, configuring, updating, and removing software packages from a trusted repository. It automatically resolves dependencies (other libraries a program needs to function), saving developers from manually locating and compiling source files.

## 3. Commands / tools used
- `pwd`: Checked current directory path.
- `ls`, `ls -l`, `ls -lah`: Inspected directory contents with various flags.
- `cd`: Navigated between directories.
- `mkdir -p`: Created `terminal-practice` folder.
- `touch`: Created file.
- `echo ... >` and `echo ... >>`: Practised overwriting and appending text.
- `cp` and `mv`: Duplicated and renamed files.
- `cat`: Read file contents.
- `|` (pipe) and `head -n 5`: Streamed and filtered command output.
- `brew --version` and `brew list`: Inspected Homebrew package manager.

## 4. My understanding
The Terminal provides a direct text interface to the operating system shell (`zsh` on macOS). Unlike a graphical interface where actions require mouse clicks, the CLI allows precise, scriptable commands. Commands accept flags to adjust behavior (such as `-a` for hidden files or `-h` for readable sizes). Pipes allow small, single-purpose Unix tools to be chained together into powerful workflows without saving intermediate temporary files.

## 5. Difficulties faced
- Remembering the difference between `>` (which overwrites existing file content) and `>>` (which appends to the end).
- Understanding how the pipe `|` redirects data streams without writing to disk.

## 6. How I resolved them
- Tested both `>` and `>>` on `sample.txt` and verified the file after each step using `cat` to see the effect directly.
- Traced the pipe as a virtual pipeline: output from `ls -l` flows directly into the input of `head`, which truncates the stream to the specified line count.

## 7. Evidence / files
- `mission-02-terminal/README.md`
- `terminal-practice/sample.txt`
- `terminal-practice/sample_archive.txt`

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Branch: `main`
- Status: Staged, committed, and pushed to GitHub.
