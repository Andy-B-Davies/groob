import numpy 
import copy

from . import abstract_poly as ap

class dict_poly(ap.abstract_poly):
        

    @classmethod
    def from_dict(cls, dict_):        
        new_poly = cls()
        new_poly.terms = dict_.copy()
        return new_poly

    @classmethod
    def from_universal_rep(cls, universal_representation):
        return cls.from_dict(universal_representation)


    def __eq__(self, other):
        all_terms = set(self.terms.keys()).union(other.terms.keys())        
        return all(self.terms.get(e,0) == other.terms.get(e,0) for e in all_terms)

    def __add__(self,other):
        new_dict={}
        exponents = set(self.terms.keys()).union(other.terms.keys())

        for e in exponents:
            new_dict[e] = self.terms.get(e, 0) + other.terms.get(e, 0)
            if not new_dict[e]:
                del new_dict[e]

            
        # for product in other.terms:
        #     if product in poly_sum.terms:
        #         poly_sum.terms[product] += other.terms[product]
        #     else poly_sum.terms[product] = other.terms[product]
        #     if poly_sum.terms[product] == 0
        #         del poly_sum.terms[product]
        return dict_poly.from_dict(new_dict)


    def __sub__(self,other):
        pass
    def __mul__(self,other):
        pass