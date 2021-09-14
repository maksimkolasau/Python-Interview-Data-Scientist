# декоратор для обозначения всех авто спортивными
def sportcardecorator(func):

    def sportcars(*args, **kwargs):
        print('I love this combination of the car: ')
        func(*args, **kwargs)

    return sportcars
