


def get_sorted_category_sum(l: list) -> list:
    category = list({x["category"] for x in l})
    result = [(cat, sum([x["price_rub"] for x in l if x["category"] == cat]))
               for cat in category]
    return sorted(result, key = lambda x: x[1])

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

print(get_sorted_category_sum(_sales_data))

def test_sum_category_as_tuples():
    """
        Показать сумму покупок по категориями. Отсортировать категории по возрастанию суммы
    """
    actual = get_sorted_category_sum(_sales_data)
    assert actual == [("bakery", 115),
                      ("drinks", 390),
                      ("dairy products", 440),
                      ]
