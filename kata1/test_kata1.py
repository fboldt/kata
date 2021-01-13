import pytest
from StringCalculator import StringCalculator

@pytest.fixture(autouse=True)
def newStringCalculator():
    sc = StringCalculator()
    assert sc is not None
    return sc

def test_empty_string(newStringCalculator):
    value = newStringCalculator.add("")
    assert value == 0

def test_one_number(newStringCalculator):
    value = newStringCalculator.add("5")
    assert value == 5

def test_two_numbers(newStringCalculator):
    value = newStringCalculator.add("5,6")
    assert value == 11

@pytest.mark.parametrize("numbers, result", [
    ("", 0), ("5", 5), ("5,6", 11), #1. the same old tests
    ("5,6,7", 18), ("5,,7", 12), ("1,2,3,4,5", 15), #2. undefined number of values
    ("1\n2,3", 6), ("1\n2\n3", 6), #3. allow new lines as delimiter
    ("//;\n1,2", 3) #4. custom delimiters
])
def test_many_numbers(numbers, result):
    assert StringCalculator().add(numbers) == result

def test_negative_number(): #5. exception "negatives not allowed"
    with pytest.raises(Exception):
        StringCalculator().add("2,-1")
