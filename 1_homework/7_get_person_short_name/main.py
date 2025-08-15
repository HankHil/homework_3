"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""
from os.path import split


def get_person_short_name(fio: str) -> str:
    words = fio.split()
    return print(f'{words[0]} {words[1][0]}. {words[2][0]}.')


# КАК НАПИСАТЬ ASSERT ДЛЯ PRINT?


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_person_short_name('Лермонтов Михаил Юрьевич')
    get_person_short_name('Александр Сергеевич Пушкин')
    get_person_short_name('Андрей Борисович Ковтун')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
