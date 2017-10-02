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
#print(arr_of_x)

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


def method2(arr_func):
    curent_arr = []
    minFunc = min(arr_func)
    minRight = arr_func.index(minFunc)+1
    minLeft = arr_func.index(minFunc)-1

    curent_arr.append(arr_func[minLeft])
    curent_arr.append(minFunc)
    curent_arr.append(arr_func[minRight])

    return curent_arr





print(method2(arr_of_result_f1))
print(method2(arr_of_result_f2))
print(method2(arr_of_result_f3))
