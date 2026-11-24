# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the core roles of the operating system on macOS:
- Inspect OS version, kernel details, active user identity, storage utilization, and running processes.
- Understand what a process is and how Process IDs (PIDs) work.
- Analyse absolute and relative paths, file permissions (read, write, execute), and owner privileges.
- Explain the key responsibilities of an operating system with practical examples.

## 2. Work completed

### Task 3.1 — Operating System Exploration

All identifying personal details such as usernames and hostnames have been redacted in accordance with assignment privacy guidelines.

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS name, version, build number, and kernel architecture. | macOS (Darwin kernel 25.5.0 on `arm64` architecture). |
| **Current account identity** | Displays the current user account and group permissions executing the shell. | Active user: `[redacted]` (member of `staff` group). |
| **Available and used storage** | Shows mounted filesystem capacity, space consumed, and space remaining. | Filesystem size: `460Gi`, Used: `16Gi`, Available: `303Gi` (6% utilized). |
| **System activity snapshot** | Provides a real-time list of active processes, CPU utilization, and state. | System running essential daemons and user processes; root process `/sbin/launchd` active at PID 1. |

---

### Task 3.2 — Understanding Processes

- **What is a process?**
  A process is an active, executing instance of a computer program loaded into memory. While a program is passive code stored on disk, a process is dynamic, possessing its own memory space, CPU registers, file descriptors, and execution state.
- **What does the PID column represent?**
  The Process Identifier (PID) is a unique numerical integer assigned by the operating system kernel to each active process when it is spawned. The kernel uses PIDs to track, prioritize, communicate with, and terminate specific processes.
- **Two examples of processes running on this computer:**
  1. `/sbin/launchd` (PID 1): The macOS root initialization process that manages system services, daemons, and user login sessions.
  2. `/usr/libexec/logd` (PID 335): The system logging daemon responsible for capturing and routing system logs and diagnostic events.

---

### Task 3.3 — Paths and File Permissions

#### Absolute vs. Relative Paths
- **Absolute path:** The complete, unambiguous location of a file or directory starting from the filesystem root (`/`). It is valid regardless of current location.
  - *Example:* `/[redacted_path]/digital-detective-8502/terminal-practice/sample.txt`
- **Relative path:** The path specified in relation to the current working directory, without a leading `/`.
  - *Example:* `terminal-practice/sample.txt` (from `digital-detective-8502`)

#### File Permission Analysis
Running `ls -l terminal-practice/sample.txt` produced:
```text
-rw-r--r--  1 [redacted]  staff  83 Nov 24 14:34 terminal-practice/sample.txt
```

- **Permission breakdown:**
  - First character `-`: Normal file (not a directory).
  - Positions 2–4 (`rw-`): **Owner permissions** — Read (`r`) and Write (`w`) allowed; Execute (`x`) denied.
  - Positions 5–7 (`r--`): **Group permissions** — Read (`r`) allowed; Write and Execute denied.
  - Positions 8–10 (`r--`): **Others permissions** — Read (`r`) allowed; Write and Execute denied.

| Permission | Meaning | Example from practice |
| :--- | :--- | :--- |
| **r — Read** | Allows viewing/reading the contents of a file. | Opening `sample.txt` using `cat` or a text editor. |
| **w — Write** | Allows modifying, appending, or overwriting file contents. | Appending a line to `sample.txt` using `>>`. |
| **x — Execute** | Allows running the file as a program or script (or traversing into a directory). | Running a Python script or shell executable. |

---

### Task 3.4 — Operating-System Responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Controls process creation, schedules CPU execution time among competing programs, and handles process termination. | Switching CPU execution smoothly between a code editor and music playback without stuttering. |
| **Memory management** | Tracks allocated and free RAM, allocates memory blocks to active applications, and protects each program's memory space. | Allocating 400 MB of RAM to a web browser tab and freeing it when closed. |
| **Device management** | Communicates with hardware peripherals through device drivers, buffering data and handling hardware interrupts. | Coordinating print data sent from an application to an external network printer. |
| **File management** | Manages file creation, organization into hierarchical folders, storage allocation, and read/write access controls. | Organizing project files inside `digital-detective-8502/` and updating file metadata on APFS. |
| **User interface / shell** | Provides a visual GUI (desktop/windows) or text CLI (shell) allowing users to interact with computer hardware and run commands. | Launching macOS Terminal and executing `zsh` commands or using Finder. |
| **Security and permissions** | Enforces user authentication, access control lists, and permission boundaries to protect data from unauthorized access. | Restricting ordinary users from modifying core system files located in `/System` or `/sbin`. |

## 3. Commands / tools used
- `sw_vers` and `uname -srm`: Inspected operating system version and kernel hardware architecture.
- `whoami`: Checked the active user environment (redacted for privacy).
- `df -h /`: Examined disk capacity, used space, and free space on the root filesystem volume.
- `ps -ef`: Listed active processes to observe PIDs and parent-child relationships.
- `ls -l`: Inspected file permission flags (`r`, `w`, `x`) and ownership.

## 4. My understanding
The operating system acts as the vital layer between physical hardware and application software. Without an OS, every software program would need to contain low-level instructions to control each specific disk, keyboard, and display. The OS coordinates access to shared resources like CPU time and RAM, maintains file structures safely, and ensures that one malfunctioning program cannot crash other running processes or access protected files.

## 5. Difficulties faced
- Deciphering Unix file permission strings like `-rw-r--r--` and understanding who each triad applies to.
- Viewing the system process table without exposing private identifying information.

## 6. How I resolved them
- Divided the 9 permission characters into three distinct triads: owner, group, and others, mapping each letter to read, write, or execute.
- Carefully sanitized process outputs and command snapshots, replacing personal usernames, hostnames, and full home paths with `[redacted]`.

## 7. Evidence / files
- `mission-03-operating-system/README.md`

## 8. Commit details
- Commit message: `Document operating system and file management`
- Branch: `main`
- Status: Staged, committed, and pushed to GitHub.
