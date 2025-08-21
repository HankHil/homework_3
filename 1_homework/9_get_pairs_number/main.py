from statistics import mean

from astropy.io.fits import append

"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""


def get_pairs_number(lst: list[int], n: int) -> list[tuple]:
    # numbers = []
    # for i in range(0, len(lst)):
    #     for x in range(i + 1, len(lst)):
    #         if (lst[i] + lst[x]) == n:
    #             pair = (min(lst[i], lst[x]), max(lst[i], lst[x]))
    #             if pair not in numbers:
    #                 numbers.append(pair)
    # return numbers


    return list({(min(lst[i], lst[j]), max(lst[i], lst[j]))
            for i in range(len(lst))
            for j in range(i + 1, len(lst))
            if (lst[i] + lst[j]) == n})

    # return list({(min(x, y), max(x, y))
    #         for i, x in enumerate(lst)
    #         for k, y in enumerate(lst)
    #         if x + y == n and i != k})

def test_get_pairs_number():
   assert get_pairs_number([1, 2, 4, 3, 5, 2], 7) == [[2, 5], [4, 3], [5, 2]]
   assert get_pairs_number([1, 2, 4, 3, 5, 9, 6, 7, 8], 10) == [[1, 9], [2, 8], [4, 6], [3, 7]]
   assert get_pairs_number([2,4,5,1,6,7,3], 11) == [[4, 7], [5, 6]]
   assert get_pairs_number([11, 4, 5, 1, 6, 7, 3, 12, 14, 8], 12) == [[11, 1], [4, 8], [5, 7]]
# print(get_pairs_number([1, 2, 4, 3, 5, 2], 7))