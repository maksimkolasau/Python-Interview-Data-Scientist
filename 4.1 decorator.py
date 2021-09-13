def decorator_car_color(func):
    def car_color(v):
        print('start to paint...')
        func(v)
        print('finish to paint!')

    return car_color


def car_model(model):
    print('bmw', model)


car_model = decorator_car_color(car_model)
car_model('Lamba')

"""def car_model():
    print('toyota')


def change_color():
    print('black')


car_model = decorator_car_color(car_model)
car_model()

change_color = decorator_car_color(change_color)
change_color() """

