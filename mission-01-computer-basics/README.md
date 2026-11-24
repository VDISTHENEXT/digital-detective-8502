# Mission 1 — Know your computer

## 1. Task / objective
Understand how a computer receives input, processes data, produces output, and stores information. Specifically:
- Trace a real-world activity through the Input, Processing, Output, and Storage (IPOS) model.
- Classify hardware components and software examples (operating system, application, and utility).
- Identify and describe three everyday computer-based systems outside of personal laptops and phones.

## 2. Work completed

### Task 1.1 — IPOS Model Trace
**Chosen Activity:** Searching the web using an internet browser.

| Stage | What happens in this example? | Hardware / Component involved |
| :--- | :--- | :--- |
| **Input** | The user types search keywords on the keyboard and clicks the search button using a trackpad or mouse. | Keyboard, trackpad / mouse, USB/input controller |
| **Processing** | The CPU runs the browser application, formats the search terms into an HTTP/HTTPS network request, receives the response over the network interface, and processes HTML, CSS, and JavaScript. | CPU (Central Processing Unit), RAM (holds active browser tabs and temporary variables), Motherboard bus |
| **Output** | The browser visualises the search results page on the screen for the user to read. | GPU (Graphics Processing Unit), Display screen / monitor |
| **Storage** | The browser caches downloaded images, writes visit history to a local database, and preserves session cookies so the user remains signed in. | SSD (Solid State Drive) / flash storage |

---

### Task 1.2 — Hardware and Software Classification

#### Hardware Items
| Item name | Hardware or software? | Purpose |
| :--- | :--- | :--- |
| **CPU (Central Processing Unit)** | Hardware | Executes arithmetic, logic, and control instructions that drive the operating system and running programs. |
| **RAM (Random Access Memory)** | Hardware | Provides fast, volatile working memory to hold programs and data currently in active use. |
| **SSD (Solid State Drive)** | Hardware | Provides persistent, non-volatile storage for files, applications, and the operating system when the computer is powered off. |
| **Monitor / Display** | Hardware | Translates video signals into visual text and graphics that the user can see and interact with. |
| **Keyboard** | Hardware | Converts mechanical key presses into digital scan codes sent to the operating system as user input. |

#### Software Examples
| Software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **macOS** | Software | Operating system software | Manages system hardware, schedules processes, manages memory and disk access, and provides the desktop interface. |
| **Mozilla Firefox** | Software | Application software | Allows the user to browse websites, display web pages, and interact with web services. |
| **Visual Studio Code** | Software | Application software | Provides a code editor with syntax highlighting and file management to help users write and edit source code. |
| **Disk Utility** | Software | Utility software | Checks disk health, partitions drives, formats storage volumes, and repairs file system errors. |
| **Antivirus / Security Scanner** | Software | Utility software | Scans files and memory for malware, monitors suspicious system activity, and isolates infected files to protect the computer. |

---

### Task 1.3 — Computer Systems Around You (Non-PC / Non-Phone)

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Allows bank customers to securely withdraw cash, check account balances, and deposit money without human staff. | Number keypad / PIN pad | Cash dispenser mechanism |
| **Microwave Oven** | Heats and cooks food according to user-selected cooking time and power level. | Front control dial or keypad | Heating magnetron (and digital timer display) |
| **Traffic Light Controller** | Coordinates traffic signals at an intersection to ensure safe vehicle and pedestrian movement. | Roadway inductive loop sensor (detects car presence) | Red, amber, and green signal lights |

## 3. Commands / tools used
- Text editor for writing and formatting Markdown documentation.
- macOS system information viewer for referencing hardware specifications.
- Terminal and Git for version control and file tracking.

## 4. My understanding
A computer is fundamentally an information processing machine. Data enters via input hardware, is manipulated by the processor using temporary volatile memory (RAM), displays results via output hardware, and is preserved on non-volatile storage.

Software operates in distinct layers:
- The **operating system** interfaces directly with the hardware.
- **Utility software** maintains and optimizes system health behind the scenes.
- **Application software** sits on top to perform tasks directly for the end user.

Additionally, dedicated microcontrollers in everyday items (like traffic lights and appliances) demonstrate that computing systems are not limited to desktops or smartphones, but exist in specialized devices all around us.

## 5. Difficulties faced
- Distinguishing utility software from core operating system features, since many modern operating systems include utilities built-in (such as disk maintenance tools).
- Separating the roles of RAM (volatile workspace) and SSD (non-volatile storage) during an active process like web browsing.

## 6. How I resolved them
- Clarified that utility software is defined by its role (system optimization, security, maintenance) regardless of whether it comes bundled with the operating system or is installed separately.
- Mapped out the lifecycle of data: RAM holds active tabs and execution stacks while the browser is running, whereas the SSD saves persistent files like cache and user history that survive computer restarts.

## 7. Evidence / files
- `mission-01-computer-basics/README.md`

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Branch: `main`
- Status: Staged, committed, and pushed to GitHub.
