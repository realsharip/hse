# Упражнение 89: Luhn Algorithm Check

![Difficulty](https://img.shields.io/badge/Difficulty-Module%201-green)
![Topics](https://img.shields.io/badge/Topics-luhn%2C%20algorithm-blue)
![Python](https://img.shields.io/badge/Python-Module%201%20Concepts-yellow)

---

## 📋 Описание задачи

Apply Luhn algorithm to 3-digit number. Double every 2nd digit from right, sum all, check if divisible by 10.
## 📥 Формат ввода

A three-digit number.
## 📤 Формат вывода

1 if valid, 0 if not.
## 💡 Примеры

### Пример 1

**Входные данные:**
```
123
```

**Выходные данные:**
```
0
### Пример 2

**Входные данные:**
```
124
```

**Выходные данные:**
```
1
### Пример 3

**Входные данные:**
```
456
```

**Выходные данные:**
```
0
## ⚠️ Ограничения

- Используйте только концепции Модуля_1: арифметические операции, остаток от деления, целочисленное деление, извлечение цифр.
- Никаких циклов, no conditionals, no lists/tuples/dicts/sets, no user-defined functions.
- Предпочитайте целочисленную математику (`//`, `%`) and арифметические тождества вместо любых форм ветвления.


---

## 🎯 Подход к решению

Это упражнение сосредоточено на **luhn, algorithm** концепциях из Модуля 1. Помните, что можно использовать только:

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
89_luhn_algorithm_check/
├── 89_luhn_algorithm_check.md     # Этот файл с описанием
└── 89_luhn_algorithm_check.py     # Ваш файл с решением
```

---

## 🔗 Навигация

- [← Previous Упражнение](88_previous) 
- [Next Упражнение →](90_next)
- [📚 Назад к Модулю 1](../../Module_1/)
- [🏠 Назад к корню курса](../../)

---

*Сгенерировано для практики Модуля 1. Часть курса Python-HSE.*
