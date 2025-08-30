"""
    Дан список, содержащий нули. Вернуть список, где все нули сдвинты вправо,
    сохранив порядок исходного списка:
    move_zeros([1, 0, 0, 2, 3, 0, 1]) -> [1, 2, 3, 1, 0, 0, 0]

    Решить в двух вариантах:
    - функция принимаем список и возвращает НОВЫЙ список
    - функция изменяет список, который был передан в аргументе функции
    (функция ничего не возвращает)
"""



def move_zeros(lst: list[float]) -> list:
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]

print(move_zeros([1, 0, 0, 2, 3, 0, 1]))

def move_zeros_two(lst: list[float]):
    # zeros = lst.count(0)
    # lst[:] = [x for x in lst if x != 0] + [0] * zeros
    #
    # for i in range(len(lst)):
    #     if lst[i] == 0:
    #         lst.append(0)
    #         lst.remove(0)
    zeros = lst.count(0)

    for _ in range(zeros):
        lst.remove(0)

    for _ in range(zeros):
        lst.append(0)
    return lst



res = [1, 0, 0, 2, 3, 0, 1]
q = [3, 0, 4, 6, 0, 1, 7, 0, 0, 0, 4, 4, 0, 1]

print(move_zeros_two(res))

print(move_zeros_two(q))