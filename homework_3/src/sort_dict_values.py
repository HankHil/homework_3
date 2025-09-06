
def sort_dict_values(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda pair: pair[1], reverse=True))


def test_sort_dict_values():
    """
        Отсортировать словарь по убыванию
    """
    d = {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }
    assert sort_dict_values(d) == {
        "USA": 100,
        "Japan": 90,
        "China": 80,
        "India": 50,
        "France": 25,
        "Russia": 5
    }