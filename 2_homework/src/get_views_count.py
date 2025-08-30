"""
    Нужно реализовать надпись в формате "N просмотров". Падеж слова "просмотр" зависит
    от числа N. Например, 1 просмотр, 2 просмотра и т.п.
"""
from panel.io.resources import json_dumps





def get_views_count_under_21(n: int) -> str:
    w = ''
    if n == 0 or n > 4:
        w = 'ов'
    elif n > 1 and n < 5:
        w = 'a'
    return f'{n} просмотр{w}'

def get_views_count_more_than_21(n: int) -> str:
    w = 'ов'
    if n % 10 == 1:
        w = ''
    elif 2<= n%10 <=5:
        w = 'a'
    return f'{n} просмотр{w}'

def get_views_count_more_than_99(n: int) -> str:
    w = 'ов'
    if n % 100 == 1:
        w = ''
    elif 2<= n%10 <=4:
        w = 'a'
    return f'{n} просмотр{w}'


def get_view(num : int) -> str:
    if 0 <= num <=20:
        return get_views_count(num)
    elif 100 > num > 20:
        return get_views_count_more_than_21(num)
    elif num > 99:
        return get_views_count_more_than_99(num)
    else:
        return None
