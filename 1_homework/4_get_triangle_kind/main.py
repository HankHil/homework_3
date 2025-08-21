"""
    Напишите функцию, которая принимает три положительных числа и
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""


def get_triangle_kind(a: int, b: int, c: int) -> str:
    if a == b == c:
        return "равносторонний"
    elif (a == b or b == c or c == a) & ((a != b or b != c or c != a)):
        return "равнобедренный"
    else:
        return "обычный"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert get_triangle_kind(3,3,1) == "равнобедренный"
    assert get_triangle_kind(3, 3, 3) == "равносторонний"
    assert get_triangle_kind(5, 1, 5) == "равнобедренный"
    assert get_triangle_kind(3, 4, 5) == "обычный"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
