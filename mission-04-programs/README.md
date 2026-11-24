# Mission 4 — How programs run

## 1. Task / objective
Explore how computer programs transition from human-readable code to machine execution:
- Write and execute a simple Python program (`hello.py`) displaying `"Hello from Python"`.
- Compare compilers and interpreters across translation timing, output artifacts, language examples, and performance advantages.
- Understand hybrid execution models in modern programming languages.

## 2. Work completed

### Task 4.1 — Python Program Creation and Execution
Inside `mission-04-programs/`, created `hello.py` with the following content:
```python
print("Hello from Python")
```

#### Execution and Verification
Ran the script from Terminal using Python 3:
```bash
python3 mission-04-programs/hello.py
```
**Terminal Output:**
```text
Hello from Python
```
The program executed cleanly and produced the expected message on standard output.

---

### Task 4.2 — Compiler vs. Interpreter Comparison

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code file into machine language or object code ahead of time, before the program runs. | Translates and executes the program instruction-by-instruction (or via bytecode execution) directly at runtime. |
| **Typical output** | A standalone executable binary file (e.g., Mach-O executable on macOS, `.exe` on Windows) or intermediate object file. | Direct output displayed in the terminal or GUI without generating a standalone executable file. |
| **One example** | C, C++ (`clang`/`gcc`), Rust (`rustc`), or Go. | Python (`python3`), Ruby, PHP, or JavaScript. |
| **One advantage** | Maximum execution speed and efficiency because all code is optimized and pre-translated into native processor instructions. | Rapid development and debugging; errors are detected immediately when the line is reached, and no compilation step is needed before running. |

#### Detailed Explanation
A compiler processes the complete source code file prior to execution, performing syntax checks, optimization, and generating a standalone binary file that the processor runs directly at high speed. An interpreter, on the other hand, reads code on the fly at runtime and executes each instruction sequentially, which makes interactive testing and cross-platform scripting very convenient. 

Modern languages frequently merge both concepts: Python first parses and compiles source code into intermediate platform-independent bytecode (stored in memory or `.pyc` files), and the Python Virtual Machine (PVM) then interprets and executes this bytecode instruction by instruction.

## 3. Commands / tools used
- Text editor: Created and edited `hello.py`.
- `python3 mission-04-programs/hello.py`: Executed the Python script from Terminal using the installed Python 3.14.7 runtime.
- Git: Staged and tracked the script and documentation.

## 4. My understanding
Computers cannot directly understand high-level programming languages like Python or C; the Central Processing Unit only understands binary machine code instructions specific to its hardware architecture. Compilers bridge this gap by converting code into native machine code beforehand, yielding fast execution but requiring recompilation for different CPU architectures. Interpreters read and execute code at runtime through a software virtual machine, providing great flexibility and rapid prototyping at the cost of slight runtime interpretation overhead.

## 5. Difficulties faced
- Confusing why Python is called an interpreted language even though it creates bytecode files (`.pyc`).
- Understanding how the operating system knows which tool to use when running a script.

## 6. How I resolved them
- Learned that Python uses a two-stage approach: a compilation stage that produces bytecode, followed by an interpreter stage where the virtual machine executes the bytecode.
- Observed that explicitly invoking `python3 hello.py` passes the file as an argument to the Python 3 binary, which parses and executes it.

## 7. Evidence / files
- `mission-04-programs/hello.py`
- `mission-04-programs/README.md`

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Branch: `main`
- Status: Staged, committed, and pushed to GitHub.
