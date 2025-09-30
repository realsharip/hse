# Module 1 Lectures Summary

## Overview

Module 1 introduces fundamental Python concepts focusing on basic I/O, arithmetic operations, string manipulation, and variables. The module covers essential operations without using loops, conditionals, collections, or user-defined functions. All concepts are built around pure arithmetic and string operations.

## Lecture 1: Data Types and Output Functions

**Folder:** `Module_1/lectures/1/`

**What you learned**
- Basic `print()` function usage with strings and numbers
- String literals with single and double quotes
- String concatenation with `+` operator
- Multiple parameters in `print()` (automatic space separation)
- `sep` parameter for custom separators
- `end` parameter to control line endings

**Key examples**
```py
print('Hello, world!')
print('2 + 3 =', 2 + 3)
print('2+3=', 2 + 3, sep='')
print(1, 2, 3, 4, sep=' + ', end='')
print(' = ', 1 + 2 + 3 + 4, sep='')
```

**Notes & caveats**
- String literals need quotes, numbers don't
- String concatenation vs arithmetic addition
- Default space separation between print parameters
- Default newline after each print statement

## Lecture 2: Mathematical Expressions

**Folder:** `Module_1/lectures/2/`

**What you learned**
- Basic arithmetic operators: `+`, `-`, `*`, `**` (power)
- Integer division `//` and modulo `%` operations
- Variable assignment and usage
- Practical applications: clock arithmetic, speed/distance calculations

**Key examples**
```py
print(11 // 6)  # Integer division
print(11 % 6)   # Modulo operation
print((23 + 8) % 24)  # Clock wraparound
speed = 108
time = 12
dist = time * speed
```

**Notes & caveats**
- Integer division truncates towards zero
- Modulo useful for wraparound calculations (time, circular distances)
- Variables can be reused and reassigned

## Lecture 3: String Expressions

**Folder:** `Module_1/lectures/3/`

**What you learned**
- String repetition with `*` operator
- String concatenation techniques
- Converting numbers to strings with `str()`
- Combining string and numeric operations

**Key examples**
```py
phase = "Hasta la vista"
who = '"baby"'
print(phase, ', ', who, '!', sep="")
ans = 2 + 3
expr = "2 + 3 = "
print(expr + str(ans))
```

**Notes & caveats**
- String multiplication creates repeated strings
- Need `str()` to convert numbers for concatenation
- Nested quotes require careful handling

## Lecture 4: Input Operations

**Folder:** `Module_1/lectures/4/`

**What you learned**
- Reading user input with `input()`
- Converting string input to integers with `int()`
- Combining input/output for interactive programs
- Escape sequences: `\t`, `\n`, `\'`, `\"`, `\\`

**Key examples**
```py
name = input()
print("Hello,", name)
a = int(input())
b = int(input())
print(a + b)
```

**Notes & caveats**
- `input()` always returns strings
- Must use `int()` for arithmetic operations
- Escape sequences needed for special characters in string literals

## Lecture 5: Problem Solving Examples

**Folder:** `Module_1/lectures/5/`

**What you learned**
- Unit conversion strategies (rubles/kopecks)
- Wraparound arithmetic (game lives, circular counters)
- Multi-step arithmetic problems
- Converting between different measurement units

**Key examples**
```py
# Rubles and kopecks
cost1 = a * 100 + b
cost2 = c * 100 + d
totalCost = cost1 + cost2
print(totalCost // 100, totalCost % 100)

# Wraparound counter
n = int(input())
print(n % 256)
```

**Notes & caveats**
- Always convert to smallest unit for calculations
- Use `//` and `%` to extract different unit components
- Modulo arithmetic handles wraparound naturally

## Lecture 6: Advanced Problem Patterns

**Folder:** `Module_1/lectures/6/`

**What you learned**
- Digit extraction using powers of 10
- Removing trailing digits with `//` and `**`
- Rounding up with integer arithmetic
- Complex multi-step calculations

**Key examples**
```py
# Remove K trailing digits
print(n // 10**k)

# Round up division
print((a + b - 1) // b)
```

**Notes & caveats**
- `10**k` removes k rightmost digits when used with `//`
- Rounding up can be achieved with `(a + b - 1) // b`
- Power operator `**` useful for digit manipulation

## Lecture 7: Variables and Object Model

**Folder:** `Module_1/lectures/7/`

**What you learned**
- Python variable model (references to objects)
- Immutable nature of `int` and `str` types
- Object creation and reference management
- Variable assignment semantics

**Key examples**
```py
x = 2  # Creates object and reference
y = 2  # References same object
x = 3  # Creates new object, reassigns reference
```

**Notes & caveats**
- Variables are references, not containers
- Immutable objects cannot be changed in-place
- Assignment creates new references, not new objects when possible
- Garbage collection removes unreferenced objects
