from groebner.buchberger import buchberger
from groebner.dictionary_poly import dict_poly
import pytest
import fractions
from groebner.creator import DictPolyFactory
from groebner import monomial_orders
from groebner.is_groebner import is_groebner_basis

def test_is_groebner_basis():
    fac = DictPolyFactory(("x","y"),monomial_orders.lex)
    p1 = fac.from_universal_rep({(1,1):1,(0,1):-1})
    p2 = fac.from_universal_rep({(1,0):-1,(0,2):1})
    p3 = fac.from_universal_rep({(0,3):1,(0,1):-1})
    G = [p1,p2,p3]
    assert is_groebner_basis(G)


def test_is_not_groebner_basis():
    fac = DictPolyFactory(("x","y"),monomial_orders.lex)
    p1 = fac.from_universal_rep({(1,1):1,(0,1):-1})
    p2 = fac.from_universal_rep({(1,0):-1,(0,2):1})
    p3 = fac.from_universal_rep({(0,3):1})
    G = [p1,p2,p3]
    assert not is_groebner_basis(G)    