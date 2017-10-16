import matplotlib as mlab
import pylab
import math

while True:
    variant = input('Enter your variant: ')
    if not variant.isdigit() or int(variant) < 0:
        print("Enter correct variant")
        continue
    if variant or variant == "exit":
        break

own_vers = int(variant)



def func_x(i):
    a = -own_vers
    b = own_vers*3
    n = own_vers+10
    return a + i*(b-a)/n

arr_i = [i for i in range(0,own_vers+11)]
arr_of_x = (list(map(func_x,arr_i)))


def f1_dichotomous(x):
    n = own_vers
    return (x-n)**2 + n*x

def f2_dichotomous(x):
    n = own_vers
    return (x-n)**2 + n*x**2

def f3_dichotomous(x):
    n = own_vers
    return (x-n)**2 + math.sin(n*x)

arr_of_result_f1 = list(map(f1_dichotomous,arr_of_x))
arr_of_result_f2 = list(map(f2_dichotomous,arr_of_x))
arr_of_result_f3 = list(map(f3_dichotomous,arr_of_x))

