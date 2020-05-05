from groebner import reduction_alg
from groebner.dictionary_poly import dict_poly
import fractions as f
import pytest

from groebner.monomial_orders import degree_lex
from groebner.creator import dict_creator
from groebner.creator import  DictPolyFactory

def test_reduce_wrt():
    fac = DictPolyFactory(("x","y"),degree_lex)
    p1 = fac.from_universal_rep({(2,1):1,(1,1):4,(0,2):-3})
    p2 = fac.from_universal_rep({(1,0):2,(0,1):1,(0,0):1})
    expected = fac.from_universal_rep({(0,3):f.Fraction(1,4),(0,2):f.Fraction(-9,2),(0,1):f.Fraction(-7,4)})
    answer = reduction_alg.reduce_wrt(p1,[p2])
    assert answer == expected

