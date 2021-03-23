import math_func

def test_add():
    assert math_func.add(3, 8) == 11
    assert math_func.add(6, 6) == 13
    assert math_func.add(3)    == 5     # 2nd default arg is 2
  
 def test_multiply():
    assert math_func.multiply(3, 8) == 24
    
 