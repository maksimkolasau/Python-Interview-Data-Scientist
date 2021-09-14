class Real_estate:

    def __init__(self, square_meters, floor, bhk_number, available_number_of_people):
        self.square_meters = square_meters
        self.floor = floor
        self.bhk_number = bhk_number
        self.available_number_of_people = available_number_of_people

    def bhk1(self):
        print(f"I would like to buy {self.bhk_number}-BHK room on the {self.floor}th floor with a {self.square_meters} "
              f"square meters!")

    @staticmethod
    def rooms():
        print("1 room is available for you now for only 50$ per night.")

    @classmethod
    def not_available_now(cls, available_number_of_people):
        cls.available_number_of_people = available_number_of_people
        print(f"Rooms are not available now because it is {available_number_of_people} places in the hotel. Sorry.")


available_real_estate = Real_estate(120, 20, 1, 89)
print(available_real_estate.bhk1())
print(available_real_estate.rooms())
print(available_real_estate.not_available_now(0))

