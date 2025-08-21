"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""
from os.path import split

def get_vector():
    return 1, 2


x, y = get_vector()

def get_person_short_name(fio: str) -> str:
    first_name, middle_name, last_name = fio.split()

    words = fio.split()
    return print(f'{first_name} {middle_name[0]}. {last_name[0]}.')


# КАК НАПИСАТЬ ASSERT ДЛЯ PRINT?


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_person_short_name('Лермонтов Михаил Юрьевич')
    get_person_short_name('Александр Сергеевич Пушкин')
    get_person_short_name('Андрей Борисович Ковтун')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
