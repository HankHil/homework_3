from get_pct_growth import get_pct_growth

def test_get_pct_growth():
    assert get_pct_growth([100, 150, 300, 400]) == [None, '50%', '100%', '33%']
    assert get_pct_growth([100, 200, 300, 400]) == [None, '100%', '50%', '33%']
    assert get_pct_growth([100, 300, 600, 900]) == [None, '200%', '100%', '50%']