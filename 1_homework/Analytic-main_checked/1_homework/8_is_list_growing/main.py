"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""


def is_list_growing(lst: list[float]) -> bool:
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            return False
    return True



assert is_list_growing([1,2,3]) == True
assert is_list_growing([3,6,39]) == True
assert is_list_growing([7,2,4]) == False
assert is_list_growing([3,5,1]) == False


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
