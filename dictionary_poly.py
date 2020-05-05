import numpy 
import copy
import itertools
from fractions import Fraction


from . import creator
from . import abstract_poly
from . import errors
from . import monomial_orders

class dict_poly(abstract_poly.abstract_poly):

##################################Class Methods#############################  
    
################################Properties##################################

    @property
    def _variable_count(self):
        k = next(iter(self.terms.keys()))
        return len(k) 
    
    @property
    def is_monomial(self):
        return len(self.terms) == 1

    @property
    def exponents_of_lead_term(self):
        if self.is_monomial:
            return next(iter(self.terms.keys()))
        else:
            return max(self.terms.keys(), key=self.term_key)

    @property
    def coeff_of_lead_term(self):
        lead_term = self.exponents_of_lead_term 
        return self.terms[lead_term]
    
################################Operators##################################

    def __repr__(self):
        # TODO clean up

        terms = []
        for exponent, coeff in self.terms.items():
            term_str = "*".join(
                f"{v}**{exp}" 
                for v,exp in zip(self.variable_names, exponent) if exp != 0
            )
            term_str = f"{coeff}*{term_str}" if coeff != 1 else term_str
            if coeff > 0:
                term_str = " + " + term_str
            terms.append(term_str)

        return "".join(terms)
            
        # return f"dict_poly({self.terms})"

    def _ensure_poly(self, item):
        if isinstance(item, type(self)):
            return item
        elif item == 0:
            return self.factory.from_universal_rep({})
        elif isinstance(item, int):            
            return self.factory.from_universal_rep({(0,)*self._variable_count:item})

    def lead_term(self):
        lt = max(self.terms.keys(), key = self.term_key)
        return self.factory.from_universal_rep({lt:self.terms[lt]})

    def lcm(self,other):
        if not (self.is_monomial and other.is_monomial):
            raise TypeError
        if self.is_monomial and other.is_monomial:
            self_exps = self.exponents_of_lead_term
            other_exps = other.exponents_of_lead_term

            lcm_exps = tuple( max(pair) for pair in zip(self_exps, other_exps) )

            return self.factory.from_universal_rep({lcm_exps:1})
        
    def __eq__(self, other):
        other = self._ensure_poly(other)
      
        all_terms = set(self.terms.keys()) | set(other.terms.keys())
        return all(self.terms.get(e,0) == other.terms.get(e,0) for e in all_terms)

    @staticmethod    
    def _universal_add(d1, d2, sign=1): 
        new_dict = {}
        exponents = set(d1.keys()) | set(d2.keys())

        for e in exponents:
            new_dict[e] = d1.get(e, 0) + sign * d2.get(e, 0)
            if not new_dict[e]:
                del new_dict[e]

        return new_dict

    def __add__(self,other):
        other=self._ensure_poly(other)
        new_dict = self._universal_add(self.terms, other.terms)
        return self.factory.from_universal_rep(new_dict)

    def __radd__(self,other):
        other=self._ensure_poly(other)
        new_dict = self._universal_add(self.terms, other.terms)
        return self.factory.from_universal_rep(new_dict)

    def __sub__(self,other):
        other = self._ensure_poly(other)
        new_dict = self._universal_add(self.terms, other.terms,-1)
        return self.factory.from_universal_rep(new_dict)

    def __mul__(self,other):

        other = self._ensure_poly(other)
        new_dict = {}

        for tuple1, tuple2 in itertools.product(self.terms, other.terms):
            key = tuple(sum(new_tup) for new_tup in zip(tuple1,tuple2))
            new_dict[key] = self.terms.get(tuple1) * other.terms.get(tuple2)
            if not new_dict[key]:
                del new_dict[key]    

        return self.factory.from_universal_rep(new_dict)

    def __truediv__(self,other):
        other = self._ensure_poly(other)
    
        if not other.is_monomial:
            raise errors.PolyDivisionError(f"Division by {other} is not a monomial")
        
        new_dict={}
        for tuple1, tuple2 in itertools.product(self.terms, other.terms):            
            key = tuple(e1-e2 for e1,e2 in zip(tuple1,tuple2))
            new_dict[key] = self.terms.get(tuple1) / other.terms.get(tuple2)
            if not new_dict[key]:
                del new_dict[key]    

        return self.factory.from_universal_rep(new_dict)

    def __or__(self,other):
        #TODO raise an error if not monomials
        
        if self.is_monomial and other.is_monomial:
            self_exps = self.exponents_of_lead_term
            other_exps = other.exponents_of_lead_term
            return all(a>=b for a,b in zip(self_exps, other_exps))
        else:
            raise errors.PolyDivisionError(f"Can only test for divisibility of monomials. {self}, {other} are not both monomials") 
