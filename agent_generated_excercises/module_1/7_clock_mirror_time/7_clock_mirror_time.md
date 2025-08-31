# Exercise 7: Clock Mirror Time

![Difficulty](https://img.shields.io/badge/Difficulty-Module%201-green)
![Topics](https://img.shields.io/badge/Topics-clock%2C%20mirror-blue)
![Python](https://img.shields.io/badge/Python-Module%201%20Concepts-yellow)

---

## 📋 Task Description

Find the mirror time of a clock reading (mirror across 6:00-12:00 axis). For H:M, mirror is (12-H):(60-M) adjusted for valid time.
## 📥 Input Format

Two integers: H (1-12), M (0-59).
## 📤 Output Format

Mirror time as two integers: hours and minutes.
## 💡 Examples

### Example 1

**Input:**
```
3
15
```

**Output:**
```
8 45
### Example 2

**Input:**
```
6
0
```

**Output:**
```
6 0
### Example 3

**Input:**
```
12
30
```

**Output:**
```
11 30
## ⚠️ Constraints

- Use only Module_1 concepts: arithmetic operations, modulo, integer division, digit extraction.
- No loops, no conditionals, no lists/tuples/dicts/sets, no user-defined functions.
- Prefer integer math (`//`, `%`) and arithmetic identities over any form of branching.


---

## 🎯 Solution Approach

This exercise focuses on **clock, mirror** concepts from Module 1. Remember to use only:

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
7_clock_mirror_time/
├── 7_clock_mirror_time.md     # This description file
└── 7_clock_mirror_time.py     # Your solution file
```

---

## 🔗 Navigation

- [← Previous Exercise](6_previous) 
- [Next Exercise →](8_next)
- [📚 Back to Module 1](../../Module_1/)
- [🏠 Back to Course Root](../../)

---

*Generated for Module 1 practice. Part of Python-HSE coursework.*
