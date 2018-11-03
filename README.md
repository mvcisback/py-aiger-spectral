# py-aiger-spectral

This library is a tool for performing (Fourier) Analysis of Boolean
Functions. `py-aiger-spectral` is built on the
[py-aiger](github.com/mvcisback/py-aiger) sequential circuit
library/ecosystem.

For an excellent introduction to the theory behind this library, I
highly recommend Ryan O'Donnell's book, [Analysis of Boolean
Functions](http://www.contrib.andrew.cmu.edu/~ryanod/).

# Usage
```python
import aiger

x = aiger.atom('x')
y = aiger.atom('y')
expr = x.implies(y) & x

# Compute Fourier coefficients of expr.
print(list(coeffs(expr)))
## [((), 0.5), (('y',), 0.5), (('x',), 0.5), (('y', 'x'), -0.5)]

# Compute weights at each degree.
print(list(weights(expr)))
## [0.25, 0.5, 0.25]

# Note that the weights of a Boolean function sum to 1.
print(sum(weights(expr)))
## 1.0

# Compute the 'mean' or first fourier coefficient.
print(mean(expr))
## 0.5

# Compute the 'variance' or sum of weights of degree > 0.
print(variance(expr))
## 0.75

# Compute the 'covariance'.
print(covariance(expr, x ^ y))
## -0.5
```

# TODO

1. [ ] Implement spectral sampling.
2. [ ] Implement convolution.
3. [ ] Implement inner product with (probability density function).

