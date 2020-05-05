import groebner.dictionary_poly
import fractions
import groebner.parser


class AbstractPolyFactory():

    def from_universal_rep(self, universal_rep):
        pass

    def from_string(self, s):
        pass


class DictPolyFactory(AbstractPolyFactory):

    def __init__(self, variable_names, term_key):
        self.variable_names = variable_names
        self.term_key = term_key


    def from_universal_rep(self, universal_rep):
        p = groebner.dictionary_poly.dict_poly()

        rational_universal_rep = { k : fractions.Fraction(v) 
                                    for k,v in universal_rep.items() }

        p.terms = rational_universal_rep
        p.variable_names = self.variable_names
        p.term_key = self.term_key
        p.factory = self

        return p        

    def from_string(self, s):
        parser = groebner.parser.Parser(self.variable_names)
        parsed_dict = parser.parse(s)
        p = self.from_universal_rep(parsed_dict)
        return p


class creator():
    def create_poly(self):
        pass



class dict_creator(creator):
    
    @classmethod
    def create_poly(self,universal_rep={}):
        p = groebner.dictionary_poly.dict_poly()
        for key in universal_rep.keys():
            universal_rep[key] = fractions.Fraction(universal_rep[key])
        p.terms = universal_rep
        return p
