"""Тестирование программы."""
import pytest

from task_1 import ComparingLists

@pytest.fixture
def list1():
    """Фикстура, подставляем список 1 для тестирования."""
    return [1, 2, 3, 3, 2, 1]

@pytest.fixture
def list2():
    """Фикстура, подставляем список 2 для тестирования."""
    return [2, 2, 2, 3, 3, 3]

def test_init(list1, list2):
    """Тест инициализации класса двумя списками."""
    nums_list = ComparingLists(list1, list2)
    assert nums_list.lst1 == list1
    assert nums_list.lst2 == list2

def test_get_lists_averages(list1, list2):
    """Тест правильности вычисления средних значений списков."""
    nums_list = ComparingLists(list1, list2)
    assert nums_list.get_lists_averages() == (2, 2.5)

@pytest.mark.parametrize('lst1, lst2, result', [([1, 2, 3], [], (2, 0)),
                                                ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
def test_get_empty_lists_averages(lst1, lst2, result):
    """Тест вычисления средних значений, если какой-то из списков пуст."""
    nums_list = ComparingLists(lst1, lst2)
    assert nums_list.get_lists_averages() == result

def test_first_average_more(list1, list2, capfd):
    """Тест выводимого сообщения, если среднее значение первого списка больше второго."""
    nums_list = ComparingLists(list2, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Первый список имеет большее среднее значение.'


def test_second_average_more(list1, list2, capfd):
    """Тест выводимого сообщения, если среднее значение второго списка больше первого."""
    nums_list = ComparingLists(list1, list2)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Второй список имеет большее среднее значение.'


def test_equal_averages(list1, capfd):
    """Тест выводимого сообщения, если средние значения списков равны."""
    nums_list = ComparingLists(list1, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Средние значения равны.'
