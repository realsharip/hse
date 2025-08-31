# Упражнение 88: Checksum Isbn Simple

![Difficulty](https://img.shields.io/badge/Difficulty-Module%201-green)
![Topics](https://img.shields.io/badge/Topics-checksum%2C%20isbn-blue)
![Python](https://img.shields.io/badge/Python-Module%201%20Concepts-yellow)

---

## 📋 Описание задачи

Calculate ISBN-10 check digit for 9-digit number. Check = (11 - sum(i×digit[i]) mod 11) mod 11.
## 📥 Формат ввода

A 9-digit number (can have leading zeros).
## 📤 Формат вывода

Check digit (0-10, where 10 is represented as 0).
## 💡 Примеры

### Пример 1

**Входные данные:**
```
123456789
```

**Выходные данные:**
```
0
### Пример 2

**Входные данные:**
```
012345678
```

**Выходные данные:**
```
9
### Пример 3

**Входные данные:**
```
111111111
```

**Выходные данные:**
```
1
## ⚠️ Ограничения

- Используйте только концепции Модуля_1: арифметические операции, остаток от деления, целочисленное деление, извлечение цифр.
- Никаких циклов, no conditionals, no lists/tuples/dicts/sets, no user-defined functions.
- Предпочитайте целочисленную математику (`//`, `%`) and арифметические тождества вместо любых форм ветвления.


---

## 🎯 Подход к решению

Это упражнение сосредоточено на **checksum, isbn** концепциях из Модуля 1. Помните, что можно использовать только:

- ✅ Basic арифметические операции (`+`, `-`, `*`, `//`, `%`, `**`)
- ✅ Функции ввода/вывода (`input()`, `print()`, `int()`, `str()`)
- ✅ Строковые операции (конкатенация, повторение, срезы)
- ✅ Mathematical reasoning and арифметические тождества

- ❌ **Никаких циклов** (`for`, `while`)
- ❌ **Никаких условий** (`if`, `elif`, `else`)
- ❌ **Никаких коллекций** (lists, tuples, dictionaries, sets)
- ❌ **Никаких пользовательских функций**

---

## 📁 Структура файлов
```
88_checksum_isbn_simple/
├── 88_checksum_isbn_simple.md     # Этот файл с описанием
└── 88_checksum_isbn_simple.py     # Ваш файл с решением
```

---

## 🔗 Навигация

- [← Previous Упражнение](87_previous) 
- [Next Упражнение →](89_next)
- [📚 Назад к Модулю 1](../../Module_1/)
- [🏠 Назад к корню курса](../../)

---

*Сгенерировано для практики Модуля 1. Часть курса Python-HSE.*
