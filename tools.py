import fractions

def dict_to_frac_dict(d):
    return {k : fractions.Fraction(v,1) for k,v in d.items()}