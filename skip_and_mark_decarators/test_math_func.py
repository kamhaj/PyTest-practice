import math_func
import pytest
import sys

@pytest.mark.number
@pytest.mark.skipif(sys.version_info < (3, 11), reason="python version is to low")
def test_add():
    assert math_func.add(3, 8) == 11
    assert math_func.add(6, 6) == 12
    assert math_func.add(3)    == 5     # 2nd default arg is 2
 

@pytest.mark.number
def test_multiply():
    assert math_func.multiply(3, 8) == 24
    assert math_func.multiply(3, 9) != 24
    
    
@pytest.mark.strings
def test_add_string():
    result =  math_func.add('Hello', ' World') 
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Welcome' not in result

 
@pytest.mark.strings 
def test_multiply_string():
    assert math_func.multiply('Hello ', 3) == 'Hello Hello Hello '
    result =  math_func.multiply('Hello ') 
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello'  in result
    
    