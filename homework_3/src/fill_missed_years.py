def fill_missed_years(d: dict) -> dict:
    #d = {int(k): v for (k, v) in d.items()}
    years = list(int(x) for x in d)
    a = {}
    a = a.setdefault(list(range(years[0], years[-1]+1)))
    return a


yearly_sales = {
    "2015": 50,
    "2018": 65,
    "2019": 120,
    "2023": 160,
    "2025": 200
}

print(fill_missed_years(yearly_sales))

def test_fill_missed_years():
    """
        Заполнить пропущенные значения средним арифметическим двух соседних значений.
        Например, если в 2015 году значение равно 50, в 2018 - 80,
        то в 2016 должно быть 60, в 2017 - 70
    """
    yearly_sales = {
        "2015": 50,
        "2018": 65,
        "2019": 120,
        "2023": 160,
        "2025": 200
    }

    assert fill_missed_years(yearly_sales) == {
        "2015": 50,
        "2016": 55,
        "2017": 60,
        "2018": 65,
        "2019": 120,
        "2020": 130,
        "2021": 140,
        "2022": 150,
        "2023": 160,
        "2024": 180,
        "2025": 200
    }



