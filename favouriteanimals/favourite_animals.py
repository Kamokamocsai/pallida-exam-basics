from sys import argv

class FavAnimals():
    def __init__(self):
        user_input = argv
        if len(user_input) == 1:
            self.print_instructions()

        elif len(user_input) == 2:
            with open('favourites.txt', 'a') as file:
                file.write(str(user_input[1:]) + "\n")

    
    def print_instructions(self):
        print("fav_animals [animal] [animal]")


controller = FavAnimals()
    