
#print('Hi ankith i\'m deleting this line of code')
# from _typeshed import SupportsKeysAndGetItem

#importing needed modules

import tkinter
import random
from tkinter import *


#The Timer Function
# :


# FUNCTION

def ClearKey(event):
    Entry_of_text.delete(0, 'end')
    second_label.config(text=random.choice(choices))
    
#The random choices of text that will be displayed to the user:


choices = ['laptop','cat','elephant','monkey','abandon','ability','abortion','about','above','abroad','absence','absolute','absorb','abuse','academic','accident','accuse','achievement','acknowledge','acquire','across','action','addition','partner','perception','performance','permanent','permission','zone','young','vegetable','versus','violation','temperature','telescope','telephone','sweet','survive','suspect','summit','suggestion','struggle','studio','strengthen','symptom',]

# '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
# '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
# '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',]






# The main window
win = Tk()
win.geometry("500x500+200+200")
win.title("Typing test")
# win.configure

# Then entry box

data_of_theEntry = StringVar()
Entry_of_text = Entry(win, bg ="#808080",fg = "#7DF9FF" ,font = ("Verdana","45","bold","italic") , relief = GROOVE,textvariable = data_of_theEntry,  )
Entry_of_text.pack(fill = X)
Entry_of_text.place(x = 100, y = 450,height = 100,width = 1200)

# Some display Labels
#1:

a_label_1 = Label(win, fg = "black", font = ("Verdana",30,"bold","italic"), text = "Test your Typing speed here!")
a_label_1.place(x = 400, y = 50)

#2:


second_label = Label(win, fg = "black", font = ("Verdana",35,"bold","italic"), text = "YO can u read this;)")
second_label.place(x = 400,y = 300)


#3:

timer_label = Label(win, fg = "black", font = ("Verdana",60,"bold","italic"), text = "30")
timer_label.place(x = 620,y = 565)


#4:


timer_label2 = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = "Time left : ")
timer_label2.place(x = 370,y = 590)
#Commands

def instructions_command():
    win2 = Tk()
    win2.title("Instructions")
    win2.geometry("400x200")
    win2.resizable(False,False)

    label_of_small_window = Label(win2,text = "Instructions:\n A Random word will be displayed on your screen. \n What you're going to do is, type that word in the textbox and hit \"enter\" \n There will be 30 words. \n You can increase the amount by your choice. \n Your result will be displayed after the timer ends!")
    label_of_small_window.place(x = 0,y = 0)


    win2.mainloop()







# Buttons --------------------------------------------------------------------

instructions_btn = Button(win, text="Instructions(click)",command = instructions_command , font = ("Verdana",20,'bold','italic'), relief = RIDGE, border = 0,activebackground = "#FFA500")
instructions_btn.place(x = 0, y = 100)


#Binding of key

win.bind('<Return>',ClearKey)


#Running of mainloop

win.mainloop()
