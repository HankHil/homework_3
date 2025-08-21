from get_views_count import get_views_count

def test_get_views_count():
    assert get_views_count(5) == "5 просмотров"
    assert get_views_count(1) == "1 просмотр"
    assert get_views_count(0) == "0 просмотров"
    assert get_views_count(2) == "2 просмотра"