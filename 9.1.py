def hello(x):
    return x ** 2


list1 = [1, 2, 3]
l1 = list(map(hello, list1))
print(l1)

