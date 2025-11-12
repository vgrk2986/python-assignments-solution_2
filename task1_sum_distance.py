
"""
Задание 1: Сумма чисел в диапазоне
"""

def sum_distance(start, end):
    """
    Суммирует все числа от start до end включительно.
    """
    if start > end:
        start, end = end, start
        print(f"Числа поменяны местами: от {start} до {end}")
    
    total = 0
    for number in range(start, end + 1):
        total += number
    
    return total


def main_task1():
    """Основная функция для задания 1"""
    print("=== ЗАДАНИЕ 1 ===")
    print("Сумма чисел в диапазоне")
    print("-" * 30)
    
    print("Тестовые примеры:")
    
    result1 = sum_distance(1, 5)
    print(f"sum_distance(1, 5) = {result1}")
    
    result2 = sum_distance(5, 1)
    print(f"sum_distance(5, 1) = {result2}")
    
    result3 = sum_distance(3, 3)
    print(f"sum_distance(3, 3) = {result3}")
    
    result4 = sum_distance(-3, 2)
    print(f"sum_distance(-3, 2) = {result4}")
    
    print("\n" + "=" * 40)
    print("Интерактивный режим:")
    print("=" * 40)
    
    while True:
        print("\nВведите два числа для вычисления суммы в диапазоне:")
        try:
            num1 = input("Первое число (или 'exit' для выхода): ")
            if num1.lower() == 'exit':
                break
            
            num2 = input("Второе число: ")
            if num2.lower() == 'exit':
                break
            
            num1 = int(num1)
            num2 = int(num2)
            
            result = sum_distance(num1, num2)
            print(f"Сумма чисел от {min(num1, num2)} до {max(num1, num2)} = {result}")
            
        except ValueError:
            print("Ошибка! Введите целые числа.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main_task1()
