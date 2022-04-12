import random
from tkinter import *
from  pygame import mixer

mixer.init()
mixer.music.load('fun-kids-playful.mp3')
mixer.music.play(-1)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Acertou!", fg="green", font=("Arial", 36, "bold"))
        correct.place(relx=0.20, rely=0.15)
    else:
        wrong = Label(app, text="Errou!", fg="red", font=("Arial", 36, "bold"))
        wrong.place(relx=0.29, rely=0.15)


def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    newQ = Label(
        app, text=f"{try_again.num1update}+{try_again.num2update}",background="#edc5e4", font=("Arial", 36, "bold")
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update


app = Tk()
app.title("Matemática Para Crianças")
# canvas = Canvas(app, width=240, height=300)
# canvas.pack()
app.geometry("300x300")
app.configure(bg='#edc5e4')
app.resizable(False, False)
start = Button(app, text="START", command=try_again, font='bold', width=10, foreground="white", bg="#db3db6")
start.place(relx=0.35, rely=0.25)
solving = Entry(app, font=("Arial", 36, "bold", ),foreground="white", bg="#db3db6")
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
submit = Button(app, text="VERIFICAR", font='bold', command=lambda: submt(solving),foreground="white", bg="#db3db6")
submit.place_configure(relx=0.35, rely=0.67, relwidth=0.34, relheight=0.1)
try_again = Button(app, text="TENTE NOVAMENTE!",font='bold', command=try_again, foreground="white", bg="#db3db6")
try_again.place(relx=0.24, rely=0.83,relwidth=0.57, relheight=0.1 )
app.mainloop()