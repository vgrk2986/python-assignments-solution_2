
"""
Задание 2: Обрезка и повторение строки
"""

def trim_and_repeat(text, offset=0, repetitions=1):
    """
    Обрезает строку слева и повторяет её указанное количество раз.
    """
    if offset < 0:
        offset = 0
    elif offset > len(text):
        offset = len(text)
    
    trimmed_text = text[offset:]
    
    if repetitions < 1:
        repetitions = 1
    
    result = trimmed_text * repetitions
    return result


def main_task2():
    """Основная функция для задания 2"""
    print("=== ЗАДАНИЕ 2 ===")
    print("Обрезка и повторение строки")
    print("-" * 30)
    
    print("Тестовые примеры:")
    
    result1 = trim_and_repeat("hello")
    print(f'trim_and_repeat("hello") = "{result1}"')
    
    result2 = trim_and_repeat("hello", 2)
    print(f'trim_and_repeat("hello", 2) = "{result2}"')
    
    result3 = trim_and_repeat("hello", 0, 3)
    print(f'trim_and_repeat("hello", 0, 3) = "{result3}"')
    
    result4 = trim_and_repeat("hello", 2, 3)
    print(f'trim_and_repeat("hello", 2, 3) = "{result4}"')
    
    result5 = trim_and_repeat("hello", 10)
    print(f'trim_and_repeat("hello", 10) = "{result5}"')
    
    result6 = trim_and_repeat("hello", -2, 0)
    print(f'trim_and_repeat("hello", -2, 0) = "{result6}"')
    
    print("\n" + "=" * 40)
    print("Интерактивный режим:")
    print("=" * 40)
    
    while True:
        print("\nВведите параметры для функции:")
        text_input = input("Строка (или 'exit' для выхода): ")
        if text_input.lower() == 'exit':
            break
        
        offset_input = input("Смещение для обрезки (по умолчанию 0): ")
        repetitions_input = input("Количество повторений (по умолчанию 1): ")
        
        try:
            offset = 0 if offset_input == "" else int(offset_input)
            repetitions = 1 if repetitions_input == "" else int(repetitions_input)
            
            result = trim_and_repeat(text_input, offset, repetitions)
            print(f"Результат: \"{result}\"")
            
        except ValueError:
            print("Ошибка! Введите корректные числа.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main_task2()
