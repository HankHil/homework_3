"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""


def get_person_short_name(fio: str) -> str:
    first_name, middle_name, last_name = fio.split()
    return print(f'{first_name} {middle_name[0]}. {last_name[0]}.')


# КАК НАПИСАТЬ ASSERT ДЛЯ PRINT?


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_person_short_name('Лермонтов Михаил Юрьевич')
    get_person_short_name('Александр Сергеевич Пушкин')
    get_person_short_name('Андрей Борисович Ковтун')

