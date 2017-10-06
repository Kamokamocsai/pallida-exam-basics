from sys import argv

class FavAnimals():
    def __init__(self):
        user_input = argv
        if len(user_input) == 1:
            print("fav_animals [animal] [animal]")

        elif len(user_input) == 2:
            with open('favourites.txt', 'a') as file:
                file.write(str(user_input[1]) + "\n")
            
        elif len(user_input) == 3:
            with open('favourites.txt', 'a') as file:
                file.write(str(user_input[1]) + "\n" + str(user_input[2]) + "\n")
                 

FavAnimals()    