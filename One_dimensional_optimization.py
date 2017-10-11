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
    b = own_vers*2
    n = own_vers+10
    return a + i*(b-a)/n

arr_i = [i for i in range(0,own_vers+11)]
arr_of_x = (list(map(func_x,arr_i)))


def f1(x):
    n = own_vers
    return (x-n)**2 + n*x

def f2(x):
    n = own_vers
    return (x-n)**2 + n*x**2

def f3(x):
    n = own_vers
    return (x-n)**2 + math.sin(n*x)

arr_of_result_f1 = list(map(f1,arr_of_x))
arr_of_result_f2 = list(map(f2,arr_of_x))
arr_of_result_f3 = list(map(f3,arr_of_x))

print('Min of F1 is: ',min(arr_of_result_f1))
print('Min of F2 is: ',min(arr_of_result_f2))
print('Min of F3 is: ',min(arr_of_result_f3))

print('-----------------------------------------------------------------')
print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format('ai','F1','F2','F3'))
print('-----------------------------------------------------------------')
for nn in arr_of_x:
    print('|{:^15.11}|{:^15.11}|{:^15.11}|{:^15.11}|'.format(nn,f1(nn),f2(nn),f3(nn)))


def extreme_points(arr_func):
    arr_of_x = []
    arr_of_x.clear()
    min_func = min(arr_func)
    min_right_elem = arr_func.index(min_func)+1
    min_left_elem = arr_func.index(min_func)-1

    arr_of_x.append(min_left_elem)
    arr_of_x.append(min_right_elem)

    return arr_of_x

def fill_new_arr(first_ai,last_ai,i):
    a = first_ai
    b = last_ai
    n = own_vers + 10
    return a + i * (b - a) / n

def sequential_search_func(arr_of_result_func,curent_func):
    for i in range(1, 27):

        extr_point_arr = extreme_points(arr_of_result_func)

        if i == 1:
            first_ai = func_x(extr_point_arr[0])
            last_ai = func_x(extr_point_arr[1])
        else:
            first_ai = arr_x_method2[extr_point_arr[0]]
            last_ai = arr_x_method2[extr_point_arr[1]]

        arr_x_method2 = []
        arr_x_method2.clear()

        for step in arr_i:
            arr_x_method2.append(fill_new_arr(first_ai, last_ai, step))

        arr_of_result_func.clear()

        arr_of_result_func = list(map(curent_func, arr_x_method2))
    return arr_of_result_func


sequential_search_func(arr_of_result_f1,f1)
sequential_search_func(arr_of_result_f2,f2)
sequential_search_func(arr_of_result_f3,f3)


#print(extreme_points(arr_of_result_f1))
#print(extreme_points(arr_of_result_f2))
#print(extreme_points(arr_of_result_f3))
