import add_func
import pytest       # for decorators


#1st argument is a comma separated string
#2nd argument is an iterable list  
@pytest.mark.parametrize('arg1, arg2, result',   
                        [
                                (7, 3, 10),
                                ('Hello', ' Kamil', 'Hello Kamil'),
                                (10.5, 25.5, 36),
                                (-8, -7, -15)
                        ]
                        )       
def test_add(arg1, arg2, result):
    assert add_func.add(arg1, arg2) == result
    