import pytest
from groebner import parser
import re



def test_sublexer():
    plus_re = re.compile(r"\+") 
    minus_re = re.compile(r"\-")
    pluslexer = parser.SubLexer(plus_re, parser.PlusToken)
    minuslexer = parser.SubLexer(minus_re, parser.MinusToken)
    expression = '2+3-4+5'

    plus_matches = pluslexer.lex(expression)
    minus_matches = minuslexer.lex(expression)


    minus_expected = [ parser.MinusToken(3, "-")  ]
    plus_expected = [ parser.PlusToken(1, "+"), parser.PlusToken(5, "+")]
    
    assert plus_matches == plus_expected
    assert minus_matches == minus_expected

def test_lexer():  
    poly = "2*x**3 + 3*y**2"
    lex=parser.Lexer(("x","y"))
    list_ = lex.lex(poly)
    print(list_)



L = [
    (
        "-3*x**2*y**3+2*z**3 + 6",
        ("x","y","z"),
        {(2,3,0):-3,(0,0,3):2,(0,0,0):6}
    ),
     (
        "+3*x**2*y**3+2*z**3 + 6",
        ("x","y","z"),
        {(2,3,0):+3,(0,0,3):2,(0,0,0):6}
     ),
    (
        "3*x**2*y**3+2*z**3 + 6",
        ("x","y","z"),
        {(2,3,0):+3,(0,0,3):2,(0,0,0):6}
    ),
    (
        "3*x**2*y**3 + 2*z**3 + 4 -4*z**2*x ",
        ("x","y","z"),
        {(2,3,0):+3,(0,0,3):2,(0,0,0):4, (1,0,2):-4}
    ),
    (
        "3*x**2*y**3 + 2*z**3 + 4 -4*z**2*x**4 ",
        ("x","y","z"),
        {(2,3,0):+3,(0,0,3):2,(0,0,0):4, (4,0,2):-4}
    ),
    (
        "4",
        ("x","y","z"),
        {(0,0,0):4}
    ),
    (
        "-4",
        ("x","y","z"),
        {(0,0,0):-4}
    ),
    (
        "y+x",
        ("x","y"),
        {(0,1):1,(1,0):1}
    )
] 

def test_split_terms():

    poly_str = "+2*x**3 + 3*y - 4"
    vars_ = ("x","y","z")
    parser_ = parser.Parser(vars_)
    lex=parser.Lexer(("x","y","z"))
    
    for i in parser_._split_terms(lex.lex(poly_str)):
        print(i)
    
def test_get_exponents():
    lexer = parser.Lexer(("x","y"))
    poly = "2*x*y"
    tokens = lexer.lex(poly)
    parser_ = parser.Parser(("x","y"))
    exponents = parser_.get_exponents(tokens)
    expected = (1,1)
    assert exponents == expected

@pytest.mark.parametrize("poly_str, vars_, expected", L)
def test_parser(poly_str, vars_, expected):

    parser_ = parser.Parser(vars_)
    parsed = parser_.parse(poly_str)

    assert parsed == expected