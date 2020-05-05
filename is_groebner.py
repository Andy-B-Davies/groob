from .reduction_alg import reduce_wrt
from .s_poly import s_poly
import itertools

def is_groebner_basis(G):
    return all(
        reduce_wrt(s_poly(p,q), G) == 0 
        for (p,q) in itertools.combinations(G, r=2)
    )