from clean_name import clean_name

def test_clean_name():
    assert clean_name("Иsвtrан Ив^%ан Ива?но)вич" ) == "Иван Иван Иванович"
    assert clean_name("Андрdas4ей Андр%#$@!еевич Тара32asсенко") == "Андрей Андреевич Тарасенко"
    assert clean_name("Никdas5423ита Серasda43%$@геевич Хas23рущев") == "Никита Сергеевич Хрущев"
    assert clean_name("Ант23%$%@$#он Антоно@#@!@%$#sdfsdвич Сидорdsf3ов") == "Антон Антонович Сидоров"