# The Digital Detective — Explore Your Computer • Build a Mini System Report

An independent learning assignment exploring computer fundamentals, command-line operations, operating system architecture, program execution, number systems and data encoding, Git/GitHub version control workflows, and computer networks.

---

## Mission Index

- [Mission 0 — Setup](mission-00-setup/README.md): Repository structure, tool verifications, and GitHub initialization.
- [Mission 1 — Computer Basics](mission-01-computer-basics/README.md): IPOS model trace, hardware/software classifications, and everyday computing systems.
- [Mission 2 — Terminal Practice](mission-02-terminal/README.md): CLI commands, safe file operations, flags (`-l`, `-a`, `-h`), Unix pipes (`|`), and package managers.
- [Mission 3 — Operating System](mission-03-operating-system/README.md): OS kernels, process management, Process IDs (PIDs), file permissions (`rwx`), and OS responsibilities.
- [Mission 4 — Programs](mission-04-programs/README.md): Execution of Python script (`hello.py`) and compiler vs. interpreter comparison.
- [Mission 5 — Numbers and Data](mission-05-numbers-data/README.md): Number base conversions (decimal, binary, hex), Python verification, character encoding (ASCII & UTF-8), and working converter script.
- [Mission 6 — Git and GitHub](mission-06-git-github/README.md): Version control fundamentals, branching (`update-about`), Pull Requests, and Git command glossary.
- [Mission 7 — Networking](mission-07-networking/README.md): Network concepts (LAN, MAN, WAN, DNS, Router, Protocols), `ping` & `nslookup` observations, and website loading lifecycle.
- [Mission 8 — Final Report](mission-08-final-report/README.md): Comprehensive repository audit, checklists, and submission verification.

---

## Topics Explored

1. **Hardware & Architecture:** Central Processing Unit (CPU), volatile memory (RAM), persistent storage (SSD), input/output peripherals, and embedded computer systems.
2. **Terminal Navigation & Scripting:** macOS `zsh` shell commands (`pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `cat`), standard input/output redirection (`>`, `>>`), command options, and stream piping (`|`).
3. **Operating System Internals:** Process scheduling, daemon supervision (`launchd`), memory management, Unix file permission triads, and filesystem paths.
4. **Program Execution:** Differences between ahead-of-time compiled binaries (C/Rust) and interpreted/bytecode execution engines (Python).
5. **Data Representation:** Positional-value arithmetic, repeated division conversions, bit nibbles, hexadecimal notation, and character encoding standards (ASCII vs. variable-width UTF-8).
6. **Distributed Version Control:** Atomic commits, staging index mechanics, feature branching, and remote pull request code reviews.
7. **Computer Networks:** IP addressing, Domain Name System (DNS) translation, packet-switched routing, transport protocols, and client-server architecture.

---

## Running the Python Number Converter

The repository includes a standalone interactive Python tool that converts decimal numbers to binary and hexadecimal.

To run the program from the project root:

```bash
# Navigate to the mission directory
cd mission-05-numbers-data

# Execute the converter using Python 3
python3 number_converter.py
```

**Example Run:**
```text
=== Decimal to Binary and Hexadecimal Converter ===
Enter a positive decimal number: 42
Decimal value:     42
Binary value:      0b101010
Hexadecimal value: 0x2a
```

---

## What I Learned

Throughout this assignment, I learned how software interacts with physical hardware across multiple layers of abstraction:
- At the lowest level, all information is stored as binary bits and bytes.
- The operating system manages physical memory and schedules CPU time among competing processes, providing a secure, sandboxed environment.
- The command-line interface provides precise, scriptable control over the computer without graphical overhead.
- Version control with Git and GitHub enables reproducible history, safe experimentation through branches, and collaborative peer review through Pull Requests.
- The global Internet operates via decentralized protocols, translating human-friendly names into IP addresses and routing data as independent packets.

---

## Workflow & Commit Discipline

Each mission in this assignment was completed in strict chronological order, verified practically on the computer, documented in its dedicated mission `README.md`, and committed and pushed separately to GitHub with meaningful commit messages.
