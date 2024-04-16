import random
from tkinter import *

win = Tk()
win.title("Guess The Number")
win.geometry("370x310")
win.configure(background= 'black')
tries = 0

def randomize():
    # 1. reset ta tries
    global tries
    global rnd
    tries = 0
    trieslbl.config(text="Tries: " + str(tries))
    # 2. eikona to zari
    piclbl.config(image=dice)
    # 3. dialegei random number (analoga tin diskolia) otan pataw to koumpi randomize
    if difficulty.get() == 1:
        rnd = random.randint(0,50)
    if difficulty.get() == 2:
        rnd = random.randint(0,100)
    if difficulty.get() == 3:
        rnd = random.randint(0,200)
    print(rnd)



def game(*args):
    global tries
    global rnd
    # 1. check entry number me to random number tou pc
    answer=int(txt.get())
    #   1a. mikrotero ? deikse panw velaki
    if answer < rnd:
        piclbl.configure(image=up)
    #   1b. megalytero ? deikse katw velaki
    elif answer > rnd:
        piclbl.configure(image=down)
    elif answer==rnd:
        piclbl.configure(image=check)
    #   1c. iso ? deikse check
    # 2. clear entry
    txt.delete(0,END)
    # 3. auksanontai ta tries
    tries = tries + 1 # tries += 1
    if tries <= 5:
        trieslbl.configure(text="Tries: "+str(tries), foreground = "green")
    elif 6<=tries<=10:
        trieslbl.configure(text="Tries: "+str(tries), foreground = "yellow")
    elif 10<tries<=15:
        trieslbl.configure(text="Tries: " + str(tries), foreground="red")
    elif tries > 15 and tries < 50:
            trieslbl.configure(text="Tries: " + str(tries), foreground="brown")
    elif tries>50:
            trieslbl.configure(text="Tries: " + str(tries), foreground="SpringGreen")

up = PhotoImage(file = "uparrow.png")
down = PhotoImage(file = "downarrow.png")
dice = PhotoImage(file = "die.png")
check = PhotoImage(file = "correct.png")

title = Label(win,text="Guess the number", background='black',foreground="white",font=('Tahoma', 20), justify= CENTER)
title.grid(column=0, columnspan=3, row=0)
instructions = Label(win, text="In this Game you will try to find a secret number"
                                "\nthat is randomly chosen every round"
                                "\nTry to guess it with the least possible tries!", background='black', font=('Tahoma', 12), foreground= "orange")
instructions.grid(column=0, columnspan=3, row=2)

difficulty = IntVar()
difficulty.set(2)
rad1 = Radiobutton(win, text="Easy (0-50)", var=difficulty, value=1, background='black', foreground = "Teal", font=('Tahoma', 12) )
rad2 = Radiobutton(win, text="Normal (0-100)", value=2, var=difficulty, background='black', foreground = "Teal", font=('Tahoma', 12))
rad3 = Radiobutton(win, text="Hard (0-200)", value=3, var=difficulty, background='black', foreground = "Teal", font=('Tahoma', 12))

rad1.grid(column=0,row=1)
rad2.grid(column=1,row=1)
rad3.grid(column=2,row=1)

txt = Entry(win,justify = CENTER)
txt.grid(column=0, row=3,columnspan = 3)

piclbl = Label(win, image = dice, background='black')
piclbl.grid(column=0, row=3,rowspan = 2)

exitbtn = Button(win, text="Exit", background='black',foreground = "#ff33cc", font=('Tahoma', 12), command=win.destroy)
exitbtn.grid(column=2, row=3)

randombtn = Button(win, text="Randomize", command = randomize, background='black', foreground="SteelBlue", font=('Tahoma', 12))
randombtn.grid(column=2, row=4)

trieslbl = Label(win,text = "Tries: 0", background='black', foreground="green", font=('Tahoma', 12))
trieslbl.grid(column=0, row=4,columnspan = 3)
win.bind('<Return>', game)

win.mainloop()