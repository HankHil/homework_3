def concat_dicts(first: dict, second: dict) -> dict:
    first.update(second)
    return first

def test_merge_two_dicts():
    """
        Соединить два словаря
    """
    developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }

    emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }

    assert concat_dicts(developed_markets, emerging_markets) == {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }


developed_markets = {
    "USA": 100,
    "Japan": 90,
    "France": 25
}

emerging_markets = {
    "China": 80,
    "India": 50,
    "Russia": 5
}

developed_markets.update(emerging_markets)
print(developed_markets)

test_merge_two_dicts()