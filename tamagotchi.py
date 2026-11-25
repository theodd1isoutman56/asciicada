from random import randrange  #im using this tamagothc itutorial and they tell us to improt this, nto sure what its used fo ryet.1
import tkinter as tk
import time
import textwrap

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

    def cicadablinksocute(self):
        with open("assetsicada/cicada_blink", "r", encoding = 'utf-8') as blinky:
            blink1 = blinky.read()
            lines = blink1.splitlines()
            padding = (65 - max(len(line) for line in lines)) // 2
            return "\n".join(" " * padding + line for line in lines)

    def cicadagui(self):
        with open("assetsicada/cicada_normal.txt", "r", encoding = "utf-8") as normal:
            normal1 = normal.read()     
            #the next 3 lines needed to be ai generated, its to help with centering, i had no clue why it wouldnt center :/
            lines = normal1.splitlines()
            padding = (65 - max(len(line) for line in lines)) // 2
            return "\n".join(" " * padding + line for line in lines)

            
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
app.resizable(False, False)
app.configure(bg='light gray')
cicada = tk.Text(app, font=("Lucida Console", 9), bg = "light gray", fg='black', relief='flat', borderwidth=0,wrap='none', width=65, height=27, padx=0, pady=0)

cicada.insert("1.0", game.cicadagui())
cicada.configure(state='disabled')

cicada.place(relx=0.5, y=10, anchor='n')

app.mainloop()