from groebner import dictionary_poly
from groebner.monomial_orders import degree_lex
from groebner.s_poly import s_poly
import fractions
from groebner.creator import DictPolyFactory
from groebner import monomial_orders
def test_s_poly_dict():
    fac = DictPolyFactory(("x","y"),degree_lex)
    p1 = fac.from_universal_rep({(1,1):2,(1,0):-1})
    p2 = fac.from_universal_rep({(2,0):3,(0,1):-1})
    expected = fac.from_universal_rep({(2,0):-0.5,(0,2):fractions.Fraction(1,3)})
    assert s_poly(p1,p2)==expected