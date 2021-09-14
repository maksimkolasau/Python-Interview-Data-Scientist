def func():
    print("I'm a function")


def func3():
    print("Cool")


func1 = func
func2 = func3

print(func3())
print(func1)
""" 
func - это объект, представляющий функцию, которую можно присвоить переменной или передать другой функции. 
func() с круглыми скобками - вызывает функцию и возвращает то, что находится в return.
"""
