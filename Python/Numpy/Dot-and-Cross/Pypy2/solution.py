# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n = input()

a, b = (numpy.array([raw_input().split() for _ in xrange(n)], dtype=int) for _ in xrange(2))

print numpy.dot(a,b)
