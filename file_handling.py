import tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
#getting text from entry


win = Tk()
win.config(bg="red")
#Lable frame
lbl1 = Label(win, text="My weekend activities")
lbl1.place(x=225)

#Global file name
global filename
filename = 'My_weekend_activities.txt'

#define Create textfile
def clicked():
    global filename
    if filename == 'My_weekend_activities.txt':
        filename = filedialog.asksaveasfile(mode='w')
    if filename != None:
        data = entry1.get('1.0','end')
        filename.write(data)

def display():
    global filename
    filename = filedialog.askopenfile(mode='r')
    if filename != None:
        text = filename.read()
        entry1.insert('0.0', text)
        entry1.focus()

def append():
    with open('My_weekend_activities.txt', 'a') as text:
        text.write(entry1.get('1.0','end'))

def clear():
    entry1.delete('1.0', END)
    entry1.update()

def quit():
    win.destroy()


entry1 = Text(win, height=10, width=40)
entry1.place(x=140, y=40)
#Buttons
b1 = Button(win, text="Create textfile", command=clicked)
b2 = Button(win, text="Display", command=display)
b3 = Button(win, text="Append Data", command=append)
b4 = Button(win, text="Clear", command=clear)
b5 = Button(win, text="Quit", command=quit)
b1.place(x=10, y=250)
b2.place(x=185, y=250)
b3.place(x=315, y=250)
b4.place(x=450, y=250)
b5.place(x=535, y=250)


#window title and Geometry
win.geometry('600x300')
win.title("My_weekend_activities")
win.mainloop()
