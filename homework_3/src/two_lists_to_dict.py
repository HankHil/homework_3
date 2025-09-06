def two_lists_to_dict(first: list, second: list) -> set:
    return {key:value for key, value in zip(first, second)}

def test_to_lists_to_dict():
    """
        Соединить два списка в словарь
    """
    keys = ["USA", "Russia", "France"]
    income = [100, 10, 25]
    assert two_lists_to_dict(keys, income) == {
        "USA": 100,
        "Russia": 10,
        "France": 25
    }
test_to_lists_to_dict()
