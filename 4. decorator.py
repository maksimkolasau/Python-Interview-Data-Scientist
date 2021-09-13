def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


# *args **kwargs - чтобы функция отработала с произвольным количеством аргументов позиционных и именованных


@table
@header
def say(name, surname, mother_name):
    print('Hello', name, surname, mother_name)


say('Vasya', 'Ivanov', 'Valentina')


# decorator - это функция, которая принимает другую функцию и возвращает функцию. декораторы нужны, что бы в нашу
# функцию добавилось новое поведение или для расширения функционала
