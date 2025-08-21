"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""


def is_list_growing(lst: list[float]) -> bool:
#    if len(lst) <= 1:
#        return True
#    for i in range(1, len(lst)):
#        if lst[i-1] > lst[i]:
#            return False
#    return True

    return all(lst[i - 1] < lst[i] for i in range(1,len(lst)))



def test_is_list_growing():
    assert is_list_growing([1,2,3]) == True
    assert is_list_growing([3,6,39]) == True
    assert is_list_growing([7,2,4]) == False
    assert is_list_growing([3,5,1]) == False





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
