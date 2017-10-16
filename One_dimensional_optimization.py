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


def extreme_points(arr_func,final_arr):
    arr_of_x = []
    arr_of_x.clear()
    min_func = min(arr_func)
    min_right_elem = arr_func.index(min_func)+1
    min_left_elem = arr_func.index(min_func)-1

    arr_of_x.append(min_left_elem)
    arr_of_x.append(min_right_elem)
    final_arr.append(min_func)

    return arr_of_x

def fill_new_arr(first_ai,last_ai,i):
    a = first_ai
    b = last_ai
    n = own_vers + 10
    return a + i * (b - a) / n

def sequential_search_func(arr_func,curent_func):
    final_arr_seq_searc = []
    curent_arr_of_result = arr_func

    for i in range(1, 26):

        extr_point_arr = extreme_points(curent_arr_of_result,final_arr_seq_searc)

        if i == 1:
            first_ai = func_x(extr_point_arr[0])
            last_ai = func_x(extr_point_arr[1])
        else:
            first_ai = arr_x_method2[extr_point_arr[0]]
            last_ai = arr_x_method2[extr_point_arr[1]]

        arr_x_method2 = []

        for step in arr_i:
            arr_x_method2.append(fill_new_arr(first_ai, last_ai, step))

        curent_arr_of_result = list(map(curent_func, arr_x_method2))
    return final_arr_seq_searc


print(sequential_search_func(arr_of_result_f1,f1))
print(sequential_search_func(arr_of_result_f2,f2))
print(sequential_search_func(arr_of_result_f3,f3))


arr_iter = [i for i in range(1,26)]

while True:
    shed_numb = int(input('Enter number of schedule of function: '))
    if not variant.isdigit() or shed_numb < 1 or shed_numb > 3:
        print("Enter correct schedule of function")
        continue
    if shed_numb or shed_numb == "exit":
        break

pict_f4 = pylab.figure(4)
#pylab.yticks(range(-10,125,1))
pylab.xticks(range(1,26,1))

if shed_numb == 1:
    pylab.plot(arr_iter, sequential_search_func(arr_of_result_f1, f1))
elif shed_numb == 2:
    pylab.plot(arr_iter, sequential_search_func(arr_of_result_f2, f2))
elif shed_numb == 3:
    pylab.plot(arr_iter, sequential_search_func(arr_of_result_f3, f3))
pict_f4.canvas.set_window_title('Графік методу послідовного уточнения для функції №{}'.format(shed_numb))
pylab.xlabel('Номер ітерації')
pylab.ylabel('Значення функції')
pict_f4.show()
input()
