class abstract_poly():

##################################Class Methods#############################

    @classmethod
    def new_poly(cls, universal_representation, term_key):
        pass

    @classmethod
    def zero(cls):
        pass


################################Properties##################################
    
    @property
    def _variable_count(self):
        pass

    @property
    def is_monomial(self):
        pass

################################Operators##################################
    
    def _ensure_poly(self, other):  # TODO remove order
        pass

    def lead_term(self, order): # TODO remove order
        pass

    def exponents_of_lead_term(self):
        pass


    def lcm(self,other):
        pass   

    def __eq__(self,other):
        pass

    def __add__(self,other):
        pass

    def __sub__(self,other):
        pass

    def __mul__(self,other):
        pass

    def __truediv__(self,other):
        pass

    def __or__(self,other):
        pass

    def __radd__(self,other):
        pass
    

    
