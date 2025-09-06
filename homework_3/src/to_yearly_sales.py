from os.path import split

monthly_sales = {
    "Jan_2020": 100,
    "Feb_2020": 90,
    "Mar_2020": 15,
    "Jan_2021": 10,
    "Feb_2021": 50,
    "Mar_2022": 5,
    "Sep_2023": 12,
    "Oct_2023": 12
}

def to_yearly_sales(d: dict) -> dict:
    years = sorted(set([x.split('_')[1] for x in d]))
    return {
        year: sum([value for (y, value) in monthly_sales.items() if year in y]) for year in years
    }




print(to_yearly_sales(monthly_sales))


def test_sum_value_of_the_same_key_kinds():
    """
        Просуммировать словарь по годам
    """
    monthly_sales = {
        "Jan_2020": 100,
        "Feb_2020": 90,
        "Mar_2020": 15,
        "Jan_2021": 10,
        "Feb_2021": 50,
        "Mar_2022": 5,
        "Sep_2023": 12,
        "Oct_2023": 12
    }
    assert to_yearly_sales(monthly_sales) == {
        "2020": 205,
        "2021": 60,
        "2022": 5,
        "2023": 24
    }
