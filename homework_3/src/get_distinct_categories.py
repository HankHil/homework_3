def get_distinct_categories(l: list) -> set:
    return {x["category"] for x in l}

_sales_data = [
    {
        "category": "dairy products",
        "product": "milk",
        "price_rub": 100,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "cream",
        "price_rub": 290,
        "count": 1
    },
    {
        "category": "dairy products",
        "product": "yogurt",
        "price_rub": 50,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "white_bread",
        "price_rub": 60,
        "count": 1
    },
    {
        "category": "bakery",
        "product": "black_bread",
        "price_rub": 55,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "water",
        "price_rub": 90,
        "count": 1
    },
    {
        "category": "drinks",
        "product": "apple_juice",
        "price_rub": 300,
        "count": 1
    }
]

print(get_distinct_categories(_sales_data))

def test_get_distinct_categories():
    """
        Вернуть множество уникальных категорий товаров
        Воспользоваться set comprehension (по аналогии с list/dict comprehension)
    """

    assert get_distinct_categories(_sales_data) == {
        "dairy products", "bakery", "drinks"}