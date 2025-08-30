from decimal import Decimal
"""
    Дан массив цен акций, вывести список, содержащий темпы прироста от периода к периоду.
    Для первого элемента списка выведите значение None. Округлите до целых.
    Например: [100, 150, 300, 400] -> [None, 50%, 100%, 33%]
"""


def get_pct_growth(s: list[float]) -> list[float]:
    # res = [None]
    # for i in range(len(s) - 1):
    #     res.append(f'{((s[i+1] - s[i]) / s[i]):.0%}')
    # return res

    return [None] + [
        f'{((s[i+1] - s[i]) / s[i]):.0%}'
                     if s[i] != 0 and s[i+1] != 0 and s[i] != None else None for i in range(len(s) - 1)]

print(get_pct_growth([100, 150, 300, 400]))