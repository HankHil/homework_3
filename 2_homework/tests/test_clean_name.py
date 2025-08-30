from src.clean_name import clean_name

def test_clean_name():
    assert clean_name("Иsвtrан Ив^%ан Ива?но)вич" ) == "Иван Иван Иванович"