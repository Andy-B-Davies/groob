
from groebner import our_module

import pytest

def test_square():

    assert our_module.square(4) == 16
    assert our_module.square(2) == 4
    assert our_module.square(10) == 100    

    assert our_module.square(12) == 144  

def test_cube():
    assert our_module.cube(10) == 1000  


L = [
    (our_module.cube, 10, 1000),
    (our_module.square, 4, 16),
    (our_module.square, 6, 36) 
]

@pytest.mark.parametrize("f_to_test, input_, expected_output", L)
def test_f(f_to_test, input_, expected_output):
    assert f_to_test(input_) == expected_output

