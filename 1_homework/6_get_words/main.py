"""
    Дана строка, разбить ее на слова. Слова разделены одним пробелом
    "Александр Сергеевич Пушкин" -> ["Александр", "Сергеевич", "Пушкин"]
"""


def get_words(s: str) -> list[str]:
    return s.split(' ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert get_words("Александр Сергеевич Пушкин") == ['Александр', 'Сергеевич', 'Пушкин']
    assert get_words("Александр Александрович Ковтун") == ['Александр', 'Александрович', 'Ковтун']
    assert get_words("Валерий Андреевич Панько") == ['Валерий', 'Андреевич', 'Панько']

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
