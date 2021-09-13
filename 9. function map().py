def add_three(x):
    return x + 3


li = [1, 2, 3]
list_data = [i for i in map(add_three, li)]
print(list_data)

a = [-1, 2, -3, 4, 5, 6]
b = list(map(abs, a))  # эти две строчки делают одно и то же
c = [abs(i) for i in a]  # эти две строчки делают одно и то же
print(c)


# https://www.youtube.com/watch?v=2ghKShXWuSs

def f(x):
    return x ** 2


d = [12, 23, 45, 67, 98]
e = list(map(f, d))
print(e)

g = ['hello', 'hi', 'good bye']
h = list(map(len, g))
h2 = list(map(str.upper, g))
h3 = list(map(lambda x: x[::-1], g))  # эти две строчки делают одно и то же
h4 = [i[::-1] for i in g]  # эти две строчки делают одно и то же
h5 = list(map(lambda x: x + '!!!!!', g))
h6 = list(map(list, g))

print(h3)
print(h2)
print(h)
print(h4)
print(h5)
print(h6)

s = input().split()
s2 = list(map(int, input().split()))
print(s)
print(s2)
