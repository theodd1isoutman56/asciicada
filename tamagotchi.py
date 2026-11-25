from random import randrange  #im using this tamagothc itutorial and they tell us to improt this, nto sure what its used fo ryet.1
import tkinter as tk
import time

class asciicada:

    def __init__(self):
        self.name="baker"
        self.hunger = 50
        self.happy=50
        self.nrg = 50

    def cicadacli(self):
      with open("assetsicada/cicada_normal.txt", "r", encoding="utf-8") as file:
        art = file.read()
        print(art)


    def cicadagui(self):
        with open("assetsicada/cicada_normal.txt", "r", encoding = "utf-8") as normal:
            normal1 = normal.read()
            return normal1        

    def feed(self):
        self.hunger = max(0, self.hunger - 10)


    def pet(self):
        self.happy = min(100, self.happy + 10)

    def run(self):
        self.cicadacli()
        while True:
            print("1, feed")
            print("2, play")
            print("3, status")
            print("4, quit")
            choice = input("")

            if choice == "1":
                self.feed()
                print("fed successful") 
                if self.hunger == 0:
                    print("you killed baker, you monster")
                print(self.hunger)
            elif choice == "2":
                print( "play successful")
            elif choice == "3":
                print(f"your pets name is {self.name}")
            elif choice == "4":
                break
            else:
                print("invaild")

game = asciicada()

#ui  stuff now

app = tk.Tk()
app.title('you and the cicada. the cicada and you')
app.geometry('600x500')
app.configure(bg = 'light gray')
cicada = tk.Label(app, text = game.cicadagui(), font = ("Consolas" , 12), bg = "light gray", fg = "black", justify="center")
cicada.pack(expand = True, anchor="center")
app.mainloop()