from groebner.buchberger import buchberger
from groebner.dictionary_poly import dict_poly
import pytest
from groebner.creator import DictPolyFactory
from groebner import monomial_orders

def test_buchberger():
    fac = DictPolyFactory(("x","y"),monomial_orders.lex)
    p1 = fac.from_universal_rep({(1,1):1,(0,1):-1})
    p2 = fac.from_universal_rep({(1,0):-1,(0,2):1})
    f = [p1,p2]
    p3 = fac.from_universal_rep({(0,3):1,(0,1):-1})
    expected = [p1,p2,p3]
    output = buchberger(f)
    assert expected == output