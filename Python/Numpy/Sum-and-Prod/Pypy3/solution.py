# Enter your code here. Read input from STDIN. Print output to STDOUT
import functools

n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(list(map(int,input().split())))
    
#print(a)

b = [sum(x) for x in zip(*a)]

print(functools.reduce(lambda x,y: x*y, b))
