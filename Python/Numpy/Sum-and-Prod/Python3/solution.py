import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)

print(numpy.product(numpy.sum(a, axis = 0), axis = 0))
