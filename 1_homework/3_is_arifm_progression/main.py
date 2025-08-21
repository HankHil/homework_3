"""
Напишите функцию, которая возвращает true, если
три заданных числа (в указанном порядке) являются последовательными членами
арифметической прогрессии
"""


def is_arifm_progression(a: int, b: int, c: int) -> bool:
    return c - b == b - a




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert is_arifm_progression(1,3,5)
    assert is_arifm_progression(2, 4, 6)
    assert is_arifm_progression(5, 7, 9)
    assert is_arifm_progression(11, 15, 19)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
