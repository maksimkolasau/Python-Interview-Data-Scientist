def makeitblue(func):

    def bluecolor(color='Blue'):
        print('Painting into Blue <3')
        func(color='Blue')

    return bluecolor

