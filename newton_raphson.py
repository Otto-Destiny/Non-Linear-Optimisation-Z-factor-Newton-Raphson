from math import exp as e

def func(y,p,t):
    t1 = -0.06125*p*t*e(-1.2*(1-t)**2)
    t2 = (y+y**2+y**3-y**4)/(1-y)**3
    t3 = (14.76*t - 9.76*t**2+4.58*t**3)*y**2
    t4 = (90.7*t -242.2*t**2+42.4*t**3)*y**(2.18+2.82*t)
    f = t1+t2-t3+t4
    return f

def derivative_func(y,p,t):
    if y == 1:
        return None
    t1 = (1+4*y*+4*y**2-4*y**3+y**4)/(1-y)**4
    
    t2 = 2*(14.76*t - 9.76*t**2+4.58*t**3)*y

    t3 = (2.18+2.82*t)*(90.7*t -242.2*t**2+42.4*t**3)*y**(1.18+2.82*t)
    d_f = t1-t2+t3
    return d_f

def compressibility_func(y,p,t):
    return (0.06125*p*t*e(-1.2*(1-t)**2))/y
    


def newton_raphson(yi,p,t,err = 0.000001):
    """
    err is tolerance value of satisfactory convergence
    """
    f = func(yi,p,t)
    while abs(f) > err:
        yj = yi-f/derivative_func(yi,p,t)
        f = func(yj,p,t)
        yi = yj

    return yi


if __name__ == '__main__':
    p = float(input('enter the value of the pseudo reduced pressure'))
    t = eval(input('enter the value of t'))
    try:
        yi = eval(input('enter an initial guess'))
    #yi = None
    except :
        yi = 0.001
    if yi ==  1:
        yi = 0.001
        
    y = newton_raphson(yi,p,t)
    print(y)
    z = compressibility_func(y,p,t)
    print('the compressibility factor is ',z)
            
    
           
