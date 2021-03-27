import keyboard
#print('Hi ankith i\'m deleting this line of code')
# from _typeshed import SupportsKeysAndGetItem
import tkinter

from tkinter import *


# FUNCTION

def ClearKey(event):
    Entry_of_text.delete(0, 'end')
    Entry_of_text.insert(0,"")
    #done

# The main window
win = Tk()
win.geometry("500x500+200+200")
win.title("Typing test")

# Then entry box

data_of_theEntry = StringVar()
Entry_of_text = Entry(win, bg ="#808080",fg = "#7DF9FF" ,font = ("Verdana","45","bold","italic") , relief = GROOVE,textvariable = data_of_theEntry,  )
Entry_of_text.pack(fill = X)
Entry_of_text.place(x = 100, y = 450,height = 100,width = 1200)

# Some display Labels

a_label_1 = Label(win, fg = "black", font = ("Verdana",30,"bold","italic"), text = "Test your Typing speed here!")
a_label_1.place(x = 400, y = 50)


#Commands

def instructions_command():
    win2 = Tk()
    win2.title("Instructions")
    win2.geometry("400x200")
    win2.resizable(width=0,height=0)

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

