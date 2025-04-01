from converter import convert

def test_convert():
    assert convert(100, 0.5) == 50
    assert round(convert(123.45, 1.23), 4) == 151.8435

#from fetcher import get_exchange_rate
#def test_get_exchange_rate():
    