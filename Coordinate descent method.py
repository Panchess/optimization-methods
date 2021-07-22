import numpy as np
from numpy import linalg as LA

def f1(x,a,b):
    return a*np.math.sin(x[0]) + b*np.math.cos(x[1])

def f2(x,a,b):
    return (x[0] - a)**2 + x[0]*x[1] + (x[1] - b)**2

def df1_1(x,a,b):
    return a*np.math.cos(x[0])

def df1_2(x,a,b):
    return -b*np.math.sin(x[1])

def df2_1(x,a,b):
    return -2*a+2*x[0]+x[1]

def df2_2(x,a,b):
    return -2*b+x[0]+2*x[1]

def coordinate_descent(f, df, a,b,x00, M, t0, eps1, eps2):
    x1 = x00
    x2 = x00
    count = 0
    while (df[0](x1,a,b) * df[0](x1,a,b) + df[1](x1,a,b) * df[1](x1,a,b)) > eps1 and count < M:
        x2[0] = x1[0] - t0 * df[0](x1,a,b)
        i = 0
        while (abs(x2[0] - x1[0]) > eps2) or (abs(f(x1,a,b) - f(x2,a,b)) > eps2) or i < 3:
            if (abs(x2[0] - x1[0]) > eps2) or (abs(f(x1,a,b) - f(x2,a,b)) > eps2):
                i = 0
            else:
                i = i + 1
            x1[0] = x2[0]
            x2[0] = x1[0] - t0 * df[0](x1,a,b)
        x1 = x2
        x2[1] = x1[1] - t0 * df[1](x1,a,b)
        i = 0
        while (abs(x1[1] - x2[1]) > eps2) or (abs(f(x1,a,b) - f(x2,a,b)) > eps2) or i < 3:
            if (abs(x2[0] - x1[0]) > eps2) or (abs(f(x1,a,b) - f(x2,a,b)) > eps2):
                i = 0
            else:
                i = i + 1
            x1[1] = x2[1]
            x2[1] = x1[1] - t0 * df[1](x1,a,b)
        x1 = x2
        t0 = t0 / 2
        count = count + 1
    return f(x1,a,b)

type = int(input())
a,b = map(float,input().split(" "))
if type == 0:
    f = f1
    df = [df1_1,df1_2]
else:
    f = f2
    df = [df2_1,df2_2]
eps1,eps2 = map(float,input().split(" "))
x1,x2 = map(float,input().split(" "))
x = [x1,x2]
print(coordinate_descent(f,df,a,b,x,10000,0.5,eps1,eps2))
