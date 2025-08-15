"""
Напишите функцию, которая возвращает true, если число является четным.
Подсказка: используйте % для определения остатка от деления: 10 % 3 = 1
"""


def is_odd(n: int) -> bool:
    if n % 2 == 1:
        return False
    else:
        return True


assert is_odd(4)
assert is_odd(6)
assert is_odd(8)
assert is_odd(12)
print('all tests passed')