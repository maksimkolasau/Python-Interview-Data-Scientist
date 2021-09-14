from modules.sportcardecorator import sportcardecorator
from modules.additionalsettings import makeitblue


class Car_like:

    @makeitblue
    @sportcardecorator
    def __init__(self, model, color):
        self.model = model
        self.color = color


cartype1 = Car_like('Tesla', 'White')

tesla_model = cartype1.model
tesla_color = cartype1.color

print(tesla_model)
print(tesla_color)

