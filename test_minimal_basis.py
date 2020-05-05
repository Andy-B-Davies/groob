from groebner.dictionary_poly import dict_poly
from groebner.creator import dict_creator, DictPolyFactory
from groebner import monomial_orders
import fractions
from groebner import minimal_basis

def test_minimal_basis():
    fac = DictPolyFactory(("y","x"), monomial_orders.lex)
    p1 = fac.from_string("y**2 + y*x + x**2")
    p2 = fac.from_string("y + x")
    p3 = fac.from_string("y")
    p4 = fac.from_string("x**2")
    p5 = fac.from_string("x")
    G = [p1,p2,p3,p4,p5]
    
    result = minimal_basis.minimise_basis(G)
    expected = [p5,p2]

    assert expected == result