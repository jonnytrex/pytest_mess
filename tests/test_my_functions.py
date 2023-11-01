import pytest
import source.my_functions as my_functions
import time

def test_add():

    result = my_functions.add_number(1,4)
    assert result == 5

def test_divide():

    result = my_functions.divide(10,5)
    assert result == 2

def test_divide_by_zero():

    with pytest.raises(ValueError):
        result = my_functions.divide(10,0)

def test_add_strings():
    result = my_functions.add_number("I Like ","Burgers")
    assert result == "I Like Burgers"

@pytest.mark.slow

def test_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2

@pytest.mark.skip(reason="This test is lame")
def test_add():

    result = my_functions.add_number(1,4)
    assert result == 5

@pytest.mark.xfail(reason="You can't divide by zero")
def test_divide_by_zero_broken():
    result = my_functions.divide(10,0)



