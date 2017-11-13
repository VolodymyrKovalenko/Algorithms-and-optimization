import pylab
import numpy

# Variant data
n = 13.0  # Variant number
eps = 1e-3 # given accuracy
k_max = 20 # max amount of iterations

def f1(x1, x2):
    return (x1 - n) ** 2 + (2 * x2 - n) ** 2

def f2(x1, x2):
    return 5 * n * (x2 - x1 ** 2) ** 2 + (n - x1) ** 2

def golden_section_method(func, a, b, dim, def_val):
    '''Searching for local minimum value
    of one-dimensional function f  in range: [a;b]
    with golden section method
    dim - number of dimension
    def_val - value in other dimension
    returns point (tuple of coordinates)'''
    def f(x):
        if dim == 1:
            return func(x, def_val)
        else:
            return func(def_val, x)
    ak, bk = a, b
    #f_values = []
    pk = ak + (1 - 0.618) * (bk - ak)
    qk = ak + 0.618 * (bk - ak)
    fpk = f(pk)
    fqk = f(qk)
    #k = 1
    #f_values.append(f(bk));
    while bk - ak > eps * 0.1:
       if fpk > fqk:
           ak = pk
           bk = bk
           pk = qk
           qk = ak + 0.618 * (bk - ak)
           fpk = fqk
           fqk = f(qk)
       else:
           ak = ak
           bk = qk
           qk = pk
           pk = ak + 0.382 * (bk - ak)
           fqk = fpk
           fpk = f(pk)
       #k = k + 1
       #f_values.append(f(bk))
    if dim == 1:
        return (bk, def_val)
    else:
        return (def_val, bk)
def cyclic_coordinate_decscent(f, a, b, c, d, start):
    """Searching for local mininmum value
    of two-dimensional function f in range: 1d - [a;b], 2d - [c;d]
    with cyclic coordinate decsent method
    start - start approximation(point) (tuple of coordinates)"""
    x_values = [start]
    f_values = [f(start[0], start[1])]
    iterations = 0
    cur = f_values[0]
    prev = cur + 2 * eps
    while abs(prev - cur) > eps and iterations < k_max:
        iterations += 1

        # move along x1
        along_x1 = golden_section_method(f, a, b, 1, x_values[len(x_values) - 1][1])
        x_values.append(along_x1)
        f_values.append(f(along_x1[0], along_x1[1]))
        # cutting current uncertainty interval
        delta = b - a
        delta_next = (x_values[len(x_values) - 1][0] - x_values[len(x_values) - 2][0]) / 2
        if delta_next <= delta / 3:
            delta_next = delta / 3
        a_next = x_values[len(x_values) - 2][0] - delta_next
        if a_next > a:
            a = a_next
        b_next = x_values[len(x_values) - 2][0] + delta_next
        if b_next > b:
            b = b_next

        # move along x2
        along_x2 = golden_section_method(f, c, d, 2, along_x1[0])
        x_values.append(along_x2)
        f_values.append(f(along_x2[0], along_x2[1]))
        # cutting current uncertainty interval
        delta = d - c
        delta_next = (x_values[len(x_values) - 1][1] - x_values[len(x_values) - 2][1]) / 2
        if delta_next <= delta / 3:
            delta_next = delta / 3
        c_next = x_values[len(x_values) - 2][1] - delta_next
        if c_next > c:
            c = c_next
        d_next = x_values[len(x_values) - 2][1] + delta_next
        if d_next > d:
            d = d_next

        prev = cur
        cur = f_values[len(f_values) - 1]

    return (x_values, f_values)

def Main():
    x1 = -1.2 * n   # First axis start point
    x2 = n  # First axis start point
    search_range = (-2 * n, 2 * n) # [0] - Min and [1] - Max values of the researching area
    def draw_level_lines(f, a, b, c, d, n):
       """Draws level lines graph from f = val1 till f = val2. There are n levels on graph"""
       def makeData():
           x = numpy.arange(a, b, 0.5)
           y = numpy.arange(c, d, 0.5)
           xgrid, ygrid = numpy.meshgrid(x, y)

           zgrid = f(xgrid, ygrid)
           return xgrid, ygrid, zgrid

       if __name__ == '__main__':
           x, y, z = makeData()
           min = float(str(z.min()))
           max = float(str(z.max()))
           levels = [min + i * (max - min) / 20 for i in range(1, 11)]
           pylab.contour(x, y, z, levels)

       pylab.show()

    res1 = cyclic_coordinate_decscent(f1, search_range[0], search_range[1], search_range[0], search_range[1], (x1, x2))
    for k, i, j in zip(range((len(res1[0]) - 1)), res1[0], res1[1]):
        print("k = {0:2d}; F1({1:8.4f};{2:8.4f}) = {3:8.4f}".format(k, i[0], i[1], j))

    draw_level_lines(f1, search_range[0], search_range[1], search_range[0], search_range[1], 10)
    print()

    search_range = (-2 * n, 2 * n + n * n)
    res2 = cyclic_coordinate_decscent(f2, search_range[0], search_range[1], search_range[0], search_range[1], (x1, x2))
    for k, i, j in zip(range((len(res2[0]) - 1)), res2[0], res2[1]):
        print("k = {0:2d}; F2({1:8.4f};{2:8.4f}) = {3:8.4f}".format(k, i[0], i[1], j))
    draw_level_lines(f2, search_range[0], search_range[1], search_range[0], search_range[1], 20)

if __name__ == "__main__":
    Main()