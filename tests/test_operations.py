from src.maths_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add (-1,1) ==0
    assert add(4,4) == 8

def test_sub():
    assert sub(1,1) ==0
    assert sub (2,1) == 1


