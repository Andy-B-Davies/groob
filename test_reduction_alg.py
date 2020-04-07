from groebner import reduction_alg as ra

import pytest

def test_reduce_wrt():
    assert ra.reduce_wrt()==None
