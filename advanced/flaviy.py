"""
Задача Иосифа Флавия 🌶️🌶️
�
n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый
k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
Напишите программу, определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа
n и k, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.
"""
import pytest


def get_flaviy(n: int, k: int) -> int:
    count = 0
    for i in range(1, n+1):
        count = (count + k) % i
    return count+1


get_flaviy(2, 1)


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (2, 1, 2),
        (5, 2, 3),
        (7, 5, 6)
    ]
)
def test_get_flaviy(n: int, k: int, expected: int) -> None:
    assert get_flaviy(n, k) == expected
