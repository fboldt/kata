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

def test_multiple_negatives(): #6. show multiple negatives in exception message
    with pytest.raises(Exception) as excinfo:
        StringCalculator().add("-1,-2")
    assert "negatives not allowed: -1 -2" in str(excinfo.value)

@pytest.mark.parametrize("calls, result", [
    ([], 0), ([""], 1), (["",""], 2), 
])
def test_getCalledCount(calls, result): #7. how many times the method add has been called
    sc = StringCalculator()
    for call in calls:
        sc.add(call)
    assert sc.getCalledCount() == result

def test_ignore_big_numbers(): #9. numbers bigger than 100 are ignored
    assert StringCalculator().add("2,1001") == 2

def test_any_length_delimiter(): #10. format: //[delimiter]\n
    assert StringCalculator().add("//[***]\n1***2***3") == 6

def test_multiple_delimiters(): #11. format: //[delim1][delim2]\n
    assert StringCalculator().add("//[*][%]\n1*2%3") == 6

def test_multiple_any_longer_delimiters(): #12. format: //[**][%%]\n1**2%%3
    assert StringCalculator().add("//[**][%%]\n1**2%%3") == 6
