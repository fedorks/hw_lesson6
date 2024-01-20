"""Основной модуль программы"""
import task_1

def main():
    """Вводим оба списка и запускаем сравнение"""
    num_lists = task_1.ComparingLists([1, 9, 7, 0], [2, 0, 2, 4])

    averages = num_lists.get_lists_averages()

    print(f"Среднее значение первого списка: {averages[0]}")
    print(f"Среднее значение второго списка: {averages[1]}")

    num_lists.compare_averages()


if __name__ == "__main__":
    main()
