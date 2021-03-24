import math_func

def test_subtract():
    assert math_func.subtract(9, 4) == 5
    assert math_func.subtract(6, 8) == -2
    assert math_func.subtract(4, 4)    == 0     # 2nd default arg is 2
  
def test_divide():
    assert math_func.divide(9, 3) == 3
    assert math_func.divide(10, 3) == 3 + 1/3