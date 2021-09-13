def decorator(func):

    def h1z1(*args, **kwargs):
        print('H1Z1')
        func(*args, **kwargs)

    return h1z1


@decorator
def hello(name, name2):
    print('is a very nice game, ', name, ' and ', name2, '!')


hello('Ivan', 'Maksim')


