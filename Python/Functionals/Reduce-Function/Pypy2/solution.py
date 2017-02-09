from __future__ import print_function
from fractions import Fraction

def product(fracs):
    t = Fraction(reduce(lambda x,y: Fraction(x*y), fracs))# complete this line with a reduce statement
    return t.numerator, t.denominator
    
if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    result = product(fracs)
    print(*result)
