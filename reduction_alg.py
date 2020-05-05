from . import dictionary_poly
import copy
def reduce_wrt(poly,reducor_polys):
    factors = [0]*len(reducor_polys)    
    h = copy.copy(poly)
    r = 0
    while not h == 0:
        divisor_exists = False
        for i,poly in enumerate(reducor_polys):
            if h.lead_term() | poly.lead_term():
                factor = h.lead_term() / poly.lead_term()
                factors[i] += factor
                h -= factor * poly
                divisor_exists = True
                break
        if not divisor_exists:
            r +=  h.lead_term()
            h -=  h.lead_term()
    return r
    
