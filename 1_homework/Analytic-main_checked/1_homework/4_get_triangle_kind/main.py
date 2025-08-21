"""
    Напишите функцию, которая принимает три положительных числа и
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""

def get_user_purchases(user_id: str) -> list[str]:
    _check_user(user_id)

    dskjflsdkf


    pass


def get_triangle_kind(a: int, b: int, c: int) -> str:
    # для определенных значений a,b,c треугольник может не существовать
    if a >= b + c:
        return "не существует"
    # a = 10000000 b = 1 c = 2

    if a == b == c:
        return "равносторонний"
    if a == b or b == c or c == a:
        return "равнобедренный"
    return "обычный"
        


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert get_triangle_kind(3,3,1) == "равнобедренный"
    assert get_triangle_kind(3, 3, 3) == "равносторонний"
    assert get_triangle_kind(5, 1, 5) == "равнобедренный"
    assert get_triangle_kind(3, 4, 5) == "обычный"

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
