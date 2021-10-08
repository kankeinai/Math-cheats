import numpy as np
import sympy as sym
    
x_val = np.linspace(1,2.2,5)
y_val = np.array([0.7651977,0.6200860,0.4554022,0.2818186,0.1103623])
n = len(x_val)
F = np.zeros((n, n))
F[:,0] = y_val
    
for i in range(1, n):
    for j in range(1, i+1):
        F[i,j] = (F[i,j-1]-F[i-1,j-1])/(x_val[i]-x_val[i-j])
    
div_diff = np.diagonal(F, offset=0, axis1=0, axis2=1)
x = sym.symbols('x')
    
coef = 1
P = div_diff[0]

for c, val in zip(div_diff[1:], x_val[0:-1]):
    coef *=(x-val)
    P+= c*coef

sym.expand(P), P.evalf(subs={x:1.5})