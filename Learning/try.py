def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

print(f(2))
print(f(3,[3,2,1]))
print(f(3))
