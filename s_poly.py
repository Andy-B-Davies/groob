from groebner.creator import dict_creator

def s_poly(poly1,poly2):
    p1 = poly1.lead_term()
    p2 = poly2.lead_term()
    l=p1.lcm(p2)
    s = (l/poly1.lead_term())*poly1 - (l/poly2.lead_term())*poly2
    return s