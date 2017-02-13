# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
from math import*


def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n<0:
        raise ValueError("Fact take only positive integer")
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
        
    
        
        

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta= ((b**2)+(4*a*c))
    if delta < 0:
        print("erreur")
    else:
        x1=((-b+sqrt(delta))/(2*a))
        x2=((-b-sqrt(delta))/(2*a))
        reponse=(x1,x2)
        return reponse
    

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    x=lower
    sum=0
    while x<=upper:
        sum+=eval(function)*0.001
        x+= 0.001
    return(sum)

if __name__ == '__main__':
    print(fact(-5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
