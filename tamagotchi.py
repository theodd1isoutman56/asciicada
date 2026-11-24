from random import randrange  #im using this tamagothc itutorial and they tell us to improt this, nto sure what its used fo ryet.
import time

class tamagotchi:
    def __init__(self):
        self.name="baker"

    def run(self):
        while True:
            print("1, feed")
            print("2, play")
            print("3, status")
            print("4, quit")
            choice = input("")

            if choice == "1":
                print("fed successful")
            elif choice == "2":
                print( "play successful")
            elif choice == "3":
                print(f"your pets name is {self.name}")
            elif choice == "4":
                break
            else:
                print("invaild")

env = tamagotchi()
env.run()