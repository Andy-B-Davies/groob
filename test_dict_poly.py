from groebner.dictionary_poly import dict_poly
from groebner.creator import dict_creator, DictPolyFactory
from groebner import monomial_orders
import fractions
import pytest

import groebner.errors as errors

def test_add():

    fac = DictPolyFactory(("x", "y", "z"), term_key = None)
    p1 = fac.from_universal_rep({(1, 2, 3): 4})
    p2 = fac.from_universal_rep({(1,2,3): 2 , (1,1,1):4})

    result = [p1 + p2,0+p1]

    expected =  [fac.from_universal_rep({(1,2,3): 6 , (1,1,1):4}),p1]

    assert result == expected

def test_sub():

    fac = DictPolyFactory(("x", "y", "z"), term_key = None)
    p1 = fac.from_universal_rep({(1, 2, 3): 4})
    p2 = fac.from_universal_rep({(1,2,3): 2 , (1,1,1):4})

    result = [p1 - p2,p1-p1]
    expected =  [fac.from_universal_rep({(1,2,3): 2 , (1,1,1):-4}),0]

    assert result == expected

def test_mul():

    fac = DictPolyFactory(("x", "y", "z"), term_key = None)
    p1 = fac.from_universal_rep({(1, 2, 3): 4})
    p2 = fac.from_universal_rep({(1,2,3): 2 , (1,1,1):4})

    result = [p1 * p2,p1*0]
    expected =  [fac.from_universal_rep({(2,4,6):8, (2,3,4):16}),0]

    assert result == expected    

def test_div():

    fac = DictPolyFactory(("x", "y", "z"), term_key = None)
    p1 = fac.from_universal_rep({(1, 2, 3): 4})
    p2 = fac.from_universal_rep({(1,2,3): 2 , (1,1,1):4})

    expected = [fac.from_universal_rep({(0,0,0):0.5,(0,-1,-2):1}),1]
    assert [p2/p1,p1/p1] == expected

   

fac_xyz = DictPolyFactory(("x", "y", "z"), term_key = lambda x:x)
fac_yx = DictPolyFactory(("y", "x"), term_key = lambda x:x)    
L = [
    (fac_xyz.from_string("2*x**2*y**2*z**3"), fac_xyz.from_string("4*x*y**2*z**3")),
    (fac_yx.from_string("y**2 + y*x + x**2"), fac_yx.from_string("y + x")),
    (fac_yx.from_string("y**2 + y*x + x**2"), fac_yx.from_string("y + x")),
]

@pytest.mark.parametrize("p1,p2", L)
def test_divisibility_yes(p1,p2):
    assert p1.lead_term() | p2.lead_term()

fac_xyz = DictPolyFactory(("x", "y", "z"), term_key = lambda x:x)
fac_yx = DictPolyFactory(("y", "x"), term_key = lambda x:x)    
L = [
    (fac_yx.from_string("y + x"), fac_yx.from_string("y**2 + y*x + x**2")),
    (fac_yx.from_string("x"), fac_yx.from_string("y + x")    ),
    (fac_yx.from_string("y+ x"), fac_yx.from_string("x")    ),
 
]    
@pytest.mark.parametrize("p1,p2", L)
def test_divisibility_no(p1,p2):
    assert not (p1.lead_term() | p2.lead_term()) 



fac_xyz = DictPolyFactory(("x", "y", "z"), term_key = lambda x:x)
fac_yx = DictPolyFactory(("y", "x"), term_key = lambda x:x)    
L = [
    (fac_yx.from_string("y + x"), fac_yx.from_string("y**2 + y*x + x**2")),
    (fac_yx.from_string("x + y**8"), fac_yx.from_string("y + x")    ),
    (fac_yx.from_string("y + x"), fac_yx.from_string("x")    ),
    (fac_yx.from_string("y"), fac_yx.from_string("x + y**7*x")    ),
    (fac_yx.from_string("y*x**5 + 12*y**7*x**104 "), fac_yx.from_string("x + y**7*x")    ),
    (fac_xyz.from_string("y*x**5 + 12*y**7*x**5  "), fac_xyz.from_string("14*x*z*y + y**7*x*z")    ),
]
@pytest.mark.parametrize("p1,p2", L)
def test_divisibility_error(p1,p2):
    with pytest.raises(errors.PolyDivisionError):
        p1 | p2






def test_eq():
    fac = DictPolyFactory(("x","y"),term_key=None)
    p1 = fac.from_universal_rep({})
    p2 = fac.from_universal_rep({(1,1):0.25})
    p3 = fac.from_universal_rep({(1,1):fractions.Fraction(1,4)})
    assert p1 == 0 and p2 == p3

def test_lead_term():
    fac = DictPolyFactory(("x","y"),monomial_orders.degree_lex)
    p = fac.from_universal_rep({(2,2):1,(1,3):1,(1,4):1})
    lt_deglex = p.lead_term()
    expected=fac.from_universal_rep({(1,4):1})
    assert lt_deglex == expected

def test_coeff_lt():
    fac = DictPolyFactory(("x","y"),monomial_orders.degree_lex)
    p = fac.from_universal_rep({(2,2):1,(1,3):1,(1,4):3})
    assert p.coeff_of_lead_term == 3

def test_lcm():
    fac = DictPolyFactory(("w","x","y","z"),monomial_orders.degree_lex)
    p1 = fac.from_universal_rep({(4,1,3,5):1})
    p2 = fac.from_universal_rep({(2,2,2,4):1})
    p3 = fac.from_universal_rep({(1,1,1):1,(1,2,3):1})
    expected = fac.from_universal_rep({(4,2,3,5):1})
    try: 
        p1.lcm(p3)
    except: "Task failed successfully"
    assert p1.lcm(p2) == expected    

def test_radd():
    fac = DictPolyFactory(("x","y"),term_key=None)
    p=fac.from_universal_rep({(1,1):1,(0,0):2})
    expected = fac.from_universal_rep({(1,1):1,(0,0):4})
    assert 2 + p == expected

def test_exponents_of_lead_term():
    fac = DictPolyFactory(("x","y"),monomial_orders.degree_lex)
    p = fac.from_universal_rep({(1,4):1,(2,2):1})
    exp = p.exponents_of_lead_term
    assert exp == (1,4)

def test_universal_add():
    d1 = {(1,1,1):1,(1,2,3):1}
    d2 = {(1,1,0):1,(1,2,3):1}
    expected = {(1,1,1):1,(1,2,3):2,(1,1,0):1}
    assert dict_poly._universal_add(d1,d2) == expected

def test_poly_from_string():
    string = "2*x**2 + 3*y**3 + z"
    variables = ("x","y","z")
    fac = DictPolyFactory(variables,monomial_orders.degree_lex)
    p = fac.from_string(string)
    expected = fac.from_universal_rep({(2,0,0):2,(0,3,0):3,(0,0,1):1})
    assert p == expected