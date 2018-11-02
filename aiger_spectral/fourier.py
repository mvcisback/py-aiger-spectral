from itertools import combinations

import aiger
import funcy as fn
from aiger_analysis.count import count


def character(subset):
    if len(subset) == 0:
        return aiger.atom(False)

    return aiger.BoolExpr(aiger.parity_gate(subset))


def dist(expr1, expr2):
    '''Compute the relative Hamming distance between expr1 and expr2.'''
    return count(expr1 ^ expr2, percent=True)


def inner_product(expr1, expr2):
    return 1 - 2*dist(expr1, expr2)


def coeff(expr, subset):
    return inner_product(expr, character(subset))


def coeffs(expr):
    names = expr.inputs
    for i in range(len(names) + 1):
        for subset in combinations(names, i):
            yield subset, coeff(expr, subset)


def weights(expr):
    deg = weight = 0
    for subset, coeff in coeffs(expr):
        if len(subset) != deg:
            yield weight
            deg = len(subset)
            weight = 0

        weight += coeff**2

    yield weight
        

def mean(expr):
    return fn.first(coeffs(expr))[1]


def variance(expr):
    return sum(fn.drop(1, weights(expr)))


def covariance(expr1, expr2):
    c1 = fn.pluck(1, coeffs(expr1))
    c2 = fn.pluck(1, coeffs(expr2))
    return sum(x*y for x, y in fn.drop(1, zip(c1, c2)))


def spectral_sample(expr):
    pass


def convolve(expr1, expr2):
    pass


if __name__ == '__main__':
    x = aiger.atom('x')
    y = aiger.atom('y')
    z = aiger.atom('z')
    expr = x.implies(y) & x | z
    print(list(coeffs(expr)))
    print(sum(weights(expr)))
    print(mean(expr))
    print(variance(expr))
    print(covariance(expr, expr))
