from groebner.dictionary_poly import dict_poly



def test_add():

    p1 = dict_poly.from_universal_rep({(1,2,3): 4 })
    p2 = dict_poly.from_universal_rep({(1,2,3): 2 , (1,1,1):4})

    result = p1 + p2
    expected =  dict_poly.from_universal_rep({(1,2,3): 6 , (1,1,1):4})

    assert result == expected


# def test_mul():

#     p1 = dict_poly.from_universal_rep({(1,2,3): 4 })
#     p2 = dict_poly.from_universal_rep({(1,2,3): 2 , (1,1,1):4})

#     result = p1 * p2
#     expected =  dict_poly.from_universal_rep({   })

#     assert result == expected    