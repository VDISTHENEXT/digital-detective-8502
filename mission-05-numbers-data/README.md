# Mission 5 — Numbers and data

## 1. Task / objective
Explore how computers represent numerical values and text using binary, decimal, and hexadecimal number systems:
- Perform step-by-step manual calculations converting between decimal, binary, and hexadecimal.
- Verify manual arithmetic using Python built-in conversion functions.
- Create and execute an interactive Python script (`number_converter.py`) that converts user-provided decimal integers to binary and hexadecimal.
- Explain character encoding standards (ASCII vs. UTF-8) and verify character codes.

## 2. Work completed

### Task 5.1 — Manual Conversions (with Step-by-Step Working)

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | **Repeated division by 2:**<br>• 13 ÷ 2 = 6, remainder **1** (LSB)<br>• 6 ÷ 2 = 3, remainder **0**<br>• 3 ÷ 2 = 1, remainder **1**<br>• 1 ÷ 2 = 0, remainder **1** (MSB)<br>Read remainders from bottom to top: **`1101₂`**<br>*Check:* (1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 0 + 1 = 13. |
| **Convert decimal 25 to binary.** | **Repeated division by 2:**<br>• 25 ÷ 2 = 12, remainder **1** (LSB)<br>• 12 ÷ 2 = 6, remainder **0**<br>• 6 ÷ 2 = 3, remainder **0**<br>• 3 ÷ 2 = 1, remainder **1**<br>• 1 ÷ 2 = 0, remainder **1** (MSB)<br>Read remainders from bottom to top: **`11001₂`**<br>*Check:* (1×16) + (1×8) + (0×4) + (0×2) + (1×1) = 16 + 8 + 0 + 0 + 1 = 25. |
| **Convert binary 1010 to decimal.** | **Positional-value expansion (powers of 2):**<br>(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)<br>= (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)<br>= 8 + 0 + 2 + 0 = **`10₁₀`** |
| **Convert binary 1101 to decimal.** | **Positional-value expansion (powers of 2):**<br>(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)<br>= (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)<br>= 8 + 4 + 0 + 1 = **`13₁₀`** |
| **Convert hexadecimal A to decimal.** | In base 16, digits 0–9 have values 0–9, and letters A–F represent 10–15.<br>Hexadecimal A represents the decimal value **10**.<br>Positional calculation: 10 × 16⁰ = 10 × 1 = **`10₁₀`** |
| **Convert hexadecimal 1F to decimal.** | **Positional-value expansion (powers of 16):**<br>(1 × 16¹) + (F × 16⁰)<br>Since F = 15:<br>= (1 × 16) + (15 × 1)<br>= 16 + 15 = **`31₁₀`** |
| **Convert binary 1111 to hexadecimal.** | Group the 4 bits (nibble) and evaluate in decimal:<br>(1 × 2³) + (1 × 2²) + (1 × 2¹) + (1 × 2⁰)<br>= 8 + 4 + 2 + 1 = 15₁₀<br>In base 16, decimal 15 is represented by the hexadecimal symbol **`F`** (or `0xF`). |

---

### Task 5.2 — Python Verification

Verified the manual calculations using Python's interactive functions:

| Expression tested | Python result | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes (matches `1101₂`) |
| `bin(25)` | `'0b11001'` | Yes (matches `11001₂`) |
| `int("1010", 2)` | `10` | Yes (matches `10₁₀`) |
| `int("1101", 2)` | `13` | Yes (matches `13₁₀`) |
| `int("A", 16)` | `10` | Yes (matches `10₁₀`) |
| `int("1F", 16)` | `31` | Yes (matches `31₁₀`) |
| `hex(0b1111)` | `'0xf'` | Yes (matches `F₁₆`) |

---

### Task 5.3 — Python Number Converter (`number_converter.py`)

Created `mission-05-numbers-data/number_converter.py` utilizing Python's built-in functions:
- `input()`: Captures user input as a string from the terminal.
- `int()`: Converts the string of digits into a base-10 integer.
- `bin()`: Converts the integer into a binary string representation with the prefix `0b`.
- `hex()`: Converts the integer into a hexadecimal string representation with the prefix `0x`.

#### Test Executions
| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **42** | `0b101010` | `0x2a` |
| **128** | `0b10000000` | `0x80` |
| **255** | `0b11111111` | `0xff` |

---

### Task 5.4 — Character Encoding

- **ASCII decimal code for uppercase 'A':** `65` (binary `01000001`).
- **ASCII decimal code for lowercase 'a':** `97` (binary `01100001`).
  *(Notice: The difference is exactly 32, representing a single flipped bit at position 2⁵).*
- **Why a computer needs an encoding standard:**
  Digital circuits only store electronic charges representing binary ones and zeros. A character-encoding standard provides a universally recognized dictionary mapping numbers to symbols, ensuring that files created on one computer display the intended letters and symbols on any other machine.
- **Example of a character outside basic ASCII:**
  The Euro currency symbol **`€`** (Unicode code point `U+20AC`, decimal `8364`). Basic ASCII only supports 7-bit codes (0–127), whereas modern UTF-8 uses variable-length encoding (1 to 4 bytes) to support millions of characters from global alphabets and symbol sets.

## 3. Commands / tools used
- Paper / positional arithmetic methods for manual conversions.
- Python 3 interactive commands (`bin()`, `hex()`, `int()`, `ord()`) to verify values.
- Text editor to write `number_converter.py`.
- `python3 mission-05-numbers-data/number_converter.py`: Tested the interactive converter with test inputs.

## 4. My understanding
All digital information—whether integers, floating-point numbers, text, images, or audio—is ultimately stored as binary bits. Hexadecimal serves as human-friendly shorthand for binary, where every 4 binary bits (one nibble) collapse into exactly one hexadecimal digit (0–F). Text encoding bridges raw bytes to human language: 7-bit ASCII established standard English representations, while UTF-8 expanded this to encode all global writing systems while preserving backwards compatibility with ASCII.

## 5. Difficulties faced
- Remembering the order of remainders when performing repeated division by 2 (first remainder is LSB, last remainder is MSB).
- Understanding the prefixes `0b` and `0x` generated by Python conversion functions.

## 6. How I resolved them
- Double-checked the binary result by recalculating the positional powers of two from right to left (2⁰, 2¹, 2², etc.) to ensure the sum matched the starting decimal value.
- Recognized that `0b` stands for binary and `0x` stands for hexadecimal, which Python uses to distinguish string representations from plain base-10 numbers.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`
- `mission-05-numbers-data/README.md`

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Branch: `main`
- Status: Staged, committed, and pushed to GitHub.
