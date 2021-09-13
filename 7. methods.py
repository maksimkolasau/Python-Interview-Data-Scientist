class CoffeeShop:
    specialty = 'espresso'

    def __init__(self, coffee_price):
        self.coffee_price = coffee_price

    # instance method
    def make_coffee(self):
        print(f'Making {self.specialty} for ${self.coffee_price}')

    # static method
    @staticmethod
    def check_weather():
        print('Its sunny')

    # class method
    @classmethod
    def change_specialty(cls, specialty):
        cls.specialty = specialty
        print(f'Specialty changed to {specialty}')


coffee_shop = CoffeeShop('5')
print(coffee_shop.make_coffee())
print(coffee_shop.check_weather())
print(coffee_shop.change_specialty('drip coffee'))
print(coffee_shop.make_coffee())
