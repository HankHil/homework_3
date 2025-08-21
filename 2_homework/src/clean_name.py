"""
    Данные загрузились из БД с лишними символами, а должны быть только русские буквы.
    Напишите функцию, которая удаляет символы, которые не являются русскими буквами.
    "Иsвtrан Ив^%ан Ива?но)вич" -> "Иванов Иван Иванович"
"""



def clean_name(fio: str) -> str:
    alf = [chr(x) for x in range(ord('а'), ord('я'))] + [chr(y) for y in range(ord('А'), ord('Я'))] + ['я', 'Я', ' ']
    return ''.join([x for x in list(fio) if x in alf])
    # res =''
    # for x in list(fio):
    #     if x in alf:
    #         res += str(x)
    # return res
    

print(clean_name('Иванов1 Иван Иванович'))
print(clean_name('Иsвtrан Ив^%ан Ива?но)вич'))

#print('Иванов Иван Иванович'.split())