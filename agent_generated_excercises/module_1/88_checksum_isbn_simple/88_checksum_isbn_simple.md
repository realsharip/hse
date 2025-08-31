# Exercise 88: Checksum Isbn Simple

![Difficulty](https://img.shields.io/badge/Difficulty-Module%201-green)
![Topics](https://img.shields.io/badge/Topics-checksum%2C%20isbn-blue)
![Python](https://img.shields.io/badge/Python-Module%201%20Concepts-yellow)

---

## 📋 Task Description

Calculate ISBN-10 check digit for 9-digit number. Check = (11 - sum(i×digit[i]) mod 11) mod 11.
## 📥 Input Format

A 9-digit number (can have leading zeros).
## 📤 Output Format

Check digit (0-10, where 10 is represented as 0).
## 💡 Examples

### Example 1

**Input:**
```
123456789
```

**Output:**
```
0
### Example 2

**Input:**
```
012345678
```

**Output:**
```
9
### Example 3

**Input:**
```
111111111
```

**Output:**
```
1
## ⚠️ Constraints

- Use only Module_1 concepts: arithmetic operations, modulo, integer division, digit extraction.
- No loops, no conditionals, no lists/tuples/dicts/sets, no user-defined functions.
- Prefer integer math (`//`, `%`) and arithmetic identities over any form of branching.


---

## 🎯 Solution Approach

This exercise focuses on **checksum, isbn** concepts from Module 1. Remember to use only:

- ✅ Basic arithmetic operations (`+`, `-`, `*`, `//`, `%`, `**`)
- ✅ Input/output functions (`input()`, `print()`, `int()`, `str()`)
- ✅ String operations (concatenation, repetition, slicing)
- ✅ Mathematical reasoning and arithmetic identities

- ❌ **No loops** (`for`, `while`)
- ❌ **No conditionals** (`if`, `elif`, `else`)
- ❌ **No collections** (lists, tuples, dictionaries, sets)
- ❌ **No user-defined functions**

---

## 📁 File Structure
```
88_checksum_isbn_simple/
├── 88_checksum_isbn_simple.md     # This description file
└── 88_checksum_isbn_simple.py     # Your solution file
```

---

## 🔗 Navigation

- [← Previous Exercise](87_previous) 
- [Next Exercise →](89_next)
- [📚 Back to Module 1](../../Module_1/)
- [🏠 Back to Course Root](../../)

---

*Generated for Module 1 practice. Part of Python-HSE coursework.*
