# декоратор для обозначения всех авто спортивными
def cardec(func):

    def sportcars(*args, **kwargs):
        print('Sport car color and speed: ')
        func(*args, **kwargs)

    return sportcars


class Car:

    @cardec
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed


car = Car('Yellow', '100 mph')
var1 = car.color
var2 = car.speed

print(var2, var1)

