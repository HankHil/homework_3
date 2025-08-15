"""
    Проверить, является ли строка с пробелами палиндромом (а роза упала на лапу азора).
    Упростим задачу, допуская, что cлова в предложении разделяются только одним пробелом.
"""


def is_palindrom(s: str) -> bool:
    letters = s.replace(' ', '')
    return letters == letters[::-1]





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert is_palindrom('а роза упала на лапу азора')
    assert is_palindrom('топот')
    assert is_palindrom('ага')
    assert is_palindrom('abc') == False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

