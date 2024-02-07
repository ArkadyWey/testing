import pytest

def square_number_plus_one(number: int):
    output = (number * number) + 1
    return output

def test_positive_integer():
    result = square_number_plus_one(5)
    assert result == 26

def test_negative_integer():
    result = square_number_plus_one(-3)
    assert result == 10

def test_zero():
    result = square_number_plus_one(0)
    assert result == 1

def test_large_integer():
    result = square_number_plus_one(10**6)
    assert result == 1000000000001

def test_float_input():
    with pytest.raises(TypeError):
        square_number_plus_one(3.5)