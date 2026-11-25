from random import randrange  #im using this tamagothc itutorial and they tell us to improt this, nto sure what its used fo ryet.1

import time

class tamagotchi:

    def cicadasciidisplay(self):
      with open("assetsicada/cicada_normal.txt", "r", encoding="utf-8") as file:
        art = file.read()
        print(art)

    def __init__(self):
        self.name="baker"
        self.hunger = 50
        self.happy=50
        self.nrg = 50

    def feed(self):
        self.hunger -= 10

    def run(self):
        self.cicadasciidisplay()
        while True:
            print("1, feed")
            print("2, play")
            print("3, status")
            print("4, quit")
            choice = input("")

            if choice == "1":
                self.feed()
                print("fed successful") 
                print(self.hunger)
            elif choice == "2":
                print( "play successful")
            elif choice == "3":
                print(f"your pets name is {self.name}")
            elif choice == "4":
                break
            else:
                print("invaild")


game = tamagotchi()
game.run()