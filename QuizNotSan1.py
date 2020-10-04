import random
from tkinter import *

window = Tk()
window.title("QuizNotSan1")
window.geometry("600x450")

questions = [["Was sind Nutzen und Effekte eines QM-Systems?",
"Planung","Identifikation","Wirtschaftlichkeit,Kundenzufriedenheit,Rechtssicherheit"]]

def clear():
    list = window.grid_slaves()
    for n in list:
        n.destroy()

class Quiz():
    def __init__(self,quest):
        clear()
        self.Fragen = []
        for n in quest:
            self.Fragen.append(n)
            self.a1=""
            self.a1=""
            self.a1=""
            self.a1=""
            self.a1=""

class Menu():
    def __init__(self):
        clear()
        self.Quiz = Button(window, text="Quiz NotSan QM", font=("Arial", 14),command=quizCreator, width=15, height=3)
        self.Quiz.grid(column=0,row=0,padx=218,pady=170)

def menuCreator():
    m = Menu()

def quizCreator():
    q = Quiz(questions)
    
menuCreator()
window.mainloop()


