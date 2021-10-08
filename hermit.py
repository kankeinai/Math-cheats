import numpy as np
import sympy as sym
    
x_val = np.array([0, 0.5])
t = 0.43
    
x = sym.symbols('x')
y = sym.exp(2*x)
y_1 = sym.diff(y)
    
y_val = np.array([y.evalf(subs={'x': x_0}) for x_0 in x_val])
y_val_diff = np.array([y_1.evalf(subs={'x': x_0}) for x_0 in x_val])
    
def gen_L(x_0, x_val):
    L = 1
    for val in x_val:
        L*=(x-val)/(x_0-val)
    return L.expand()

def interpolate(x_val, y_val, y_val_diff):
    L = np.array([gen_L(x_0, x_val[x_val!=x_0]) for x_0 in x_val])
    L_diff = np.array([sym.diff(f) for f in L])
    H = []
    H_1 = []
        
    for c, x_0 in enumerate(x_val):
        coef = L_diff[c].evalf(subs={'x': x_0})
        func = (1-2*(x-x_0)*coef)*L[c]**2
        H.append(func)
        H_1.append((x-x_0)*L[c]**2)
    
    H = np.array(H)
    H_1 = np.array(H_1)
    
    return sum(y_val*H + y_val_diff*H_1).expand()

 
result = interpolate(x_val, y_val, y_val_diff)
result, result.evalf(subs = {'x': t})