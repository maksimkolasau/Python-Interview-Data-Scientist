def makeitblue(func):
    def bluecolor(*args, **kwargs):
        print('What Tesla combination do you like?')
        func(*args, **kwargs)

    return bluecolor
