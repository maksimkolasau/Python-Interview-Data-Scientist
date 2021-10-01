from functools import reduce


def love(x, y):
    return x + y


list1 = ['Vasya', '+', 'Petya', '=', 'LOVE']
print(len(reduce(love, list1)))
