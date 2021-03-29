
  

#print('Hi ankith i\'m deleting this line of code')
# from _typeshed import SupportsKeysAndGetItem



#importing needed modules

import tkinter
import random
from tkinter import *
from tkinter import messagebox
from tkinter import font





# FUNCTION

def start_of_words():
    second_label.config(text= f"{random.choice(choices)}")





def ClearKey(event):
    data = Entry_of_text.get()
    print(data)
    if(data == second_label['text']):
        pass
    

    

    
    Entry_of_text.delete(0, 'end')
    second_label.config(text=random.choice(choices))
    
    
    
time = 30
def start():
    try:
        global time

        if time > 0:

            timer_label.config(text = time)
            time -= 1
            timer_label.after(1000,start)

        elif time == 0:

            timer_label.config(text="TIME'S UP!!!!")
            reponse = messagebox.askquestion("Time's up!","this is your score : ")
            if reponse == 0:
                win.destroy()

            elif reponse == 1:
                win3 = Tk()
                win3.geometry("100x100")
                win3.title("Your score!!")


                win3.mainloop()
    except:
        start_of_words()



#now its time for the data storing and evaluation:
# data = StringVar()




#The random choices of text that will be displayed to the user:


choices = ['laptop','cat','elephant','monkey','abandon','ability','abortion','about','above','abroad','absence','absolute','absorb','abuse','academic','accident','accuse','achievement','acknowledge','acquire','across','action','addition','partner','perception','performance','permanent','permission','zone','young','vegetable','versus','violation','temperature','telescope','telephone','sweet','survive','suspect','summit','suggestion','struggle','studio','strengthen','symptom',
'Rabbies','Anthrax','site','Respiration','syntax','error','Smile','Reverse','keyboard','dog','google','hire','saviour','english','french','portugal','land','ocean','monument','stand','stage','commit','window','search','bar','typing','fast','slow','beast','ostrich','cannon','canyon','branch','arguments','provide','overloads','wildcard','library','allow','match','saturated','solution','chemistry',
]






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


second_label = Label(win, fg = "black", font = ("Verdana",40,"bold","italic"), text = "")
second_label.place(x = 620,y = 330)


#3:

timer_label = Label(win, fg = "black", font = ("Verdana",60,"bold","italic"), text = "30")
timer_label.place(x = 620,y = 565)


#4:


timer_label2 = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = "Time left : ")
timer_label2.place(x = 370,y = 590)

#5:

display_label_of_words = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = "Your Word : ")
display_label_of_words.place(x = 370 , y =340 )



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
#1:
instructions_btn = Button(win, text="Instructions(click)",command = instructions_command , font = ("Verdana",20,'bold','italic'), relief = RIDGE, border = 0,activebackground = "#FFA500", state= NORMAL)
instructions_btn.place(x = 0, y = 100)

#2:

start_button = Button(win , text="Start!",command = start , font = ("Verdana",20,'bold','italic'), relief = RIDGE, border = 0,activebackground = "#FFA500")
start_button.place(x = 0, y = 150)



#Binding of key

win.bind('<Return>',ClearKey)


#Running of mainloop

win.mainloop()
