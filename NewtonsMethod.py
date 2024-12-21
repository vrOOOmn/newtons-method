import math 
import numpy as np
from sympy import *



def newtons_method(x0: float, f: str, precision: int):
    x = symbols('x')
   
    x_values = [x0]
    xn = x0
    

    while True:
        functionValue = f.subs(x, xn).evalf()
        slope = diff(f,x).subs(x,xn).evalf()

        xn -= (functionValue/slope)

        x_values.append(round(xn, precision))

        if x_values[-1] == x_values[-2]:
            break


    return x_values

print("Welcome to the Newton's method calculator!")
function_input = input("Please enter your function f(x): ")
precision_input = int(input("Please input your desired precision (# of decimal places): "))

try:
    f = parse_expr(function_input)
except Exception as e:
    print(f'Error {e}\n Please enter your function in terms of x')
    exit(1)

x0 = float(input("What is your initial x-value: "))
solution = newtons_method(x0, f, precision_input)


for x in solution:
    print(f'x ≈ {x}')

