from src.maths_operations import _add,_sub

def test_add():
    assert _add(2,3)==5
    assert _add (-1,1) ==0
    assert _add(4,4) == 8

def test_sub():
    assert _sub(1,1) ==0
    assert _sub (2,1) == 1

