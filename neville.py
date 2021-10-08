import numpy as np
import sympy as sym
    
x_val = np.linspace(0, 0.75, 4)
x = sym.symbols('x')
y_val = np.array([1, 1.64872, 2.71828, 4.48169])
n = len(x_val)
Q = sym.zeros(n, n)
Q[:, 0] = y_val
    
for i in range(1,n):
    for j in range(1,i+1):
        Q[i, j] = ((x-x_val[i-j])*Q[i, j-1] -
        - (x-x_val[i])*Q[i-1, j-1])/(x_val[i] - x_val[i-j])
    
sym.expand(Q[n-1, n-1]), Q[n-1, n-1].evalf(subs = {x:0.43})