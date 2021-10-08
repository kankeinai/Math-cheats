import numpy as np
import sympy as sym
    
x0 = 0.5 #the last point
h = 0.25
y_val = np.array([1.93750, 1.33203,0.984, 0.800781, 0.687500])
n = len(y_val)
F = np.zeros((n, n))
F[:,0] = y_val[::-1]
for i in range(1, n):
    for j in range(1, i+1):
        F[i,j] = (F[i,j-1]-F[i-1,j-1])
    
div_diff = np.diagonal(F, offset=0, axis1=0, axis2=1)
    
x = sym.symbols('x')
s = (x-x0)/h
coef = 1
P = div_diff[0]
for i in range(1, n):
    coef = -coef*(s+i-1)/i
    P += div_diff[i]*coef
    
P.expand(), P.evalf(subs = {x:0.5})