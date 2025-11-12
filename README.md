# Решение заданий на Python

## Описание проекта
Этот репозиторий содержит решения двух заданий на Python.

## Содержание
- `task1_sum_distance.py` - Задание 1: Сумма чисел в диапазоне
- `task2_trim_and_repeat.py` - Задание 2: Обрезка и повторение строки
- `main_program.py` - Главная программа, объединяющая оба задания
- `README.md` - Документация

## Задание 1: Сумма чисел в диапазоне

### Описание
Функция `sum_distance(from, to)` суммирует все числа от значения `from` до величины `to` включительно.

### Примеры работы
- `sum_distance(1, 5)` = 15
- `sum_distance(5, 1)` = 15 (автоматически меняет местами)
- `sum_distance(3, 3)` = 3

## Задание 2: Обрезка и повторение строки

### Описание
Функция `trim_and_repeat()` обрезает строку слева и повторяет её.

### Примеры работы
- `trim_and_repeat("hello")` = "hello"
- `trim_and_repeat("hello", 2)` = "llo"
- `trim_and_repeat("hello", 0, 3)` = "hellohellohello"

## Запуск программ

### Способ 1: Запуск главной программы
python main_program.py

### Способ 2: Запуск отдельных заданий
python task1_sum_distance.py
python task2_trim_and_repeat.py

## Требования
- Python 3.6+

## Чек-лист проверки

### Задание 1
- `sum_distance(1, 5)` возвращает 15
- `sum_distance(5, 1)` возвращает 15
- Работает с отрицательными числами

### Задание 2
- `trim_and_repeat("hello")` возвращает "hello"
- `trim_and_repeat("hello", 2)` возвращает "llo"
- `trim_and_repeat("hello", 0, 3)` возвращает "hellohellohello"
