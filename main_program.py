
"""
Главная программа - объединяет оба задания
"""

def main():
    """Главная функция программы"""
    print("ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ!")
    print("=" * 50)
    
    while True:
        print("\nВыберите задание:")
        print("1 - Сумма чисел в диапазоне")
        print("2 - Обрезка и повторение строки")
        print("3 - Запустить все задания последовательно")
        print("0 - Выход")
        
        choice = input("\nВаш выбор (0-3): ")
        
        if choice == '1':
            import task1_sum_distance
            task1_sum_distance.main_task1()
        elif choice == '2':
            import task2_trim_and_repeat
            task2_trim_and_repeat.main_task2()
        elif choice == '3':
            print("\n" + "="*50)
            import task1_sum_distance
            task1_sum_distance.main_task1()
            print("\n" + "="*50)
            import task2_trim_and_repeat
            task2_trim_and_repeat.main_task2()
        elif choice == '0':
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
