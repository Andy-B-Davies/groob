from . import dictionary_poly
from . import reduction_alg
import copy
from . import s_poly
import itertools

def buchberger(f):
    g = copy.copy(f)
    g_pairs = list(itertools.combinations(f,2))
    while len(g_pairs):
        a,b = g_pairs.pop()
        s = s_poly.s_poly(a,b)        
        h = reduction_alg.reduce_wrt(s,g)
        if not h == 0:
            for u in g:
                g_pairs.append([u,h])
            g.append(h)
    return g

