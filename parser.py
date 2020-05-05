import re
import itertools

class Token:
    def __init__(self, start, match_str):
        self.start = start
        self.match_str = match_str

    def __eq__(self, other):
        return self.start == other.start and self.match_str == other.match_str

    def __repr__(self):
        return f'{type(self).__name__}({self.start}, "{self.match_str}")'

class PlusToken(Token): pass
class MinusToken(Token): pass
class MultToken(Token): pass 
class ExpToken(Token): pass
class NumberToken(Token): pass
class VarToken(Token): pass



class SubLexer:
    def __init__(self, regex, token_type):
        self.regex = regex
        self.token_type = token_type
        

    def lex(self, s):        
        return [self.token_type(match.start(), match.group()) for match in self.regex.finditer(s)]

class Lexer:

    def __init__(self, variables):

        self.variables = variables
        
        variable_pattern = ""
        for v in self.variables:
            variable_pattern += v + "|"

        
        self.sublexers = [
           
            SubLexer(re.compile(r"(?P<sought>\+)"),PlusToken),
            SubLexer(re.compile(r"(?P<sought>\-)"), MinusToken),
            SubLexer(re.compile(r"(?<!\*)(?P<sought>\*)(?!\*)"), MultToken),
            SubLexer(re.compile(r"(?P<sought>\*{2})"), ExpToken),
            SubLexer(re.compile(r"(?P<sought>\d)"), NumberToken),
            SubLexer(re.compile(f"(?P<sought>{variable_pattern[0:-1]})"), VarToken),
        ]

    @staticmethod
    def _eliminate_overlaps(token_list):
        ...

    def lex(self, s):
        token_list = list(itertools.chain( *(sublex.lex(s) for sublex in self.sublexers) ))
        token_list.sort(key=lambda item: item.start)
        return token_list


class Parser:

    def __init__(self,variables):
        self.variables = variables

    def _split_terms(self, tokens):
        term_tokens = []

        for token in tokens: 
            if term_tokens and isinstance(token, (PlusToken, MinusToken)): 
                yield term_tokens  
                term_tokens = [token] 
            else:
                term_tokens.append(token)
           

        yield term_tokens

    def get_exponents(self, tokens):
        exponents = [0]*len(self.variables)
        for i in tokens:
            if type(i) == VarToken:
                    pos_of_var = self.variables.index(i.match_str)
                    if tokens.index(i) == len(tokens) - 1: #checking if last token 
                        exponents[pos_of_var]= 1
                    elif type(tokens[tokens.index(i)+1]) == ExpToken: #checking if followed by exponent
                        exp =  int(tokens[tokens.index(i)+2].match_str)
                        exponents[pos_of_var]= exp
                    else:
                        exponents[pos_of_var]= 1
        return tuple(exponents)

    def get_coefficient(self, tokens):
        coeff = 1
        if len(tokens)==1:
            if type(tokens[0]) == NumberToken:
                coeff = int(tokens[0].match_str)
        elif type(tokens[0]) == NumberToken:
            coeff = int(tokens[0].match_str)                    
        elif type(tokens[1]) == NumberToken:
            coeff = int(tokens[0].match_str + tokens[1].match_str)
        return coeff   

    def parse(self,s):
        lexer = Lexer(self.variables)
        lexed = lexer.lex(s)
        terms = list(self._split_terms(lexed))
        
        dict_ = {}
        for t in terms:
            exponents = self.get_exponents(t)
            coeff = self.get_coefficient(t)
            dict_[exponents] = coeff
        return dict_

