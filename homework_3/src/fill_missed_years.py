from calendar import firstweekday


def fill_missed_years(d: dict) -> dict:
    years = sorted([(int(k),v) for k,v in d.items()])
    result = {}
    for i in range(len(years)-1):
        y_start, v_start = years[i]
        y_end, v_end = years[i+1]
        result[y_start] = v_start
        if y_end - y_start > 1:
            step = (v_end - v_start) / (y_end - y_start)
            for year in range(y_start + 1, y_end):
                val = v_start + step*(year - y_start)
                result[year] = int(val)
    y_last, v_last = years[-1]
    result[y_last] = v_last
    return {str(k):v for k,v in result.items()}


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


test_fill_missed_years()
