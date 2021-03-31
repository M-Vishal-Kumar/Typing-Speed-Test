
  




#importing needed modules

import tkinter
import random
from tkinter import *
from tkinter import messagebox
from tkinter import font
# import time



#Variables : 
points_correct = 0 #initially it is 0.
points_incorrect = 0
points_score = 0  #this will be words per minute
len_of_characters = 0 #the amount of characters you typed.



# FUNCTION

def start_of_words():
    second_label.config(text= f"{random.choice(choices)}")





def ClearKey(event):
    #The global variables

    global points_incorrect
    global points_correct
    global len_of_characters
    
    #The main code: 

    data = Entry_of_text.get()
    if(data == second_label['text']):
        w = len(second_label['text'])
        len_of_characters += w
        show_of_characs_typed.config(text= f"Characters : {len_of_characters}")
        
        points_correct += 1
        label_of_points.config(text= f"Correct : {points_correct}")
        
    else:
        points_incorrect += 1
        label_of_incorrect.config(text= f"Incorrect : {points_incorrect}")
        

        
        
    Entry_of_text.delete(0, 'end')
    second_label.config(text=random.choice(choices))
    
    
    
time = 60
def start():
    #Dont add "second label.config" here, cause it just keeps changing the text every 1 second.
    try:
        global time

        if time > 0:

            timer_label.config(text = f"{time}")
            time -= 1
            timer_label.after(1000,start)

        elif time == 0:
            
            timer_label.config(text="Nope")
            reponse = messagebox.showinfo("Time's up!",f"this is your score : \n Correct : {points_correct} \n Incorrect : {points_incorrect} \n Your overall all speed : {round(len_of_characters / 5)} words/minute!! \n To retry, close and reopen the programe!" )
            if reponse == 1:
                exit()
                

            elif reponse == 0:
                exit()
                
    except:
        start_of_words()








#The random choices of text that will be displayed to the user:


choices = ['laptop','cat','elephant','monkey','abandon','ability','abortion','about','above','abroad','absence','absolute','absorb','abuse','academic','accident','accuse','achievement','acknowledge','acquire','across','action','addition','partner','perception','performance','permanent','permission','zone','young','vegetable','versus','violation','temperature','telescope','telephone','sweet','survive','suspect','summit','suggestion','struggle','studio','strengthen','symptom',
'Rabbies','Anthrax','site','Respiration','syntax','error','Smile','Reverse','keyboard','dog','google','hire','saviour','english','french','portugal','land','ocean','monument','stand','stage','commit','window','search','bar','typing','fast','slow','beast','ostrich','cannon','canyon','branch','arguments','provide','overloads','wildcard','library','allow','match','saturated','solution','chemistry',
]






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
#1:

a_label_1 = Label(win, fg = "black", font = ("Verdana",35,"bold","italic"), text = "Test your Typing speed here!")
a_label_1.place(x = 330, y = 40)

#2:


second_label = Label(win, fg = "black", font = ("Verdana",60,"bold","italic"), text = "snakes")
second_label.place(x = 620,y = 300)


#3:

timer_label = Label(win, fg = "black", font = ("Verdana",60,"bold","italic"), text = "1 Min")
timer_label.place(x = 620,y = 565)


#4:


timer_label2 = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = "Time left : ")
timer_label2.place(x = 370,y = 590)

#5:

display_label_of_words = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = "Your Word : ")
display_label_of_words.place(x = 370 , y =340 )

#6:
# points = 0
label_of_points = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = f"Correct : {points_correct}")
label_of_points.place(x = 0,y = 250)


#7:

label_of_incorrect = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = f"Incorrect : {points_incorrect}")
label_of_incorrect.place(x = 0, y = 300)

#8:
show_of_characs_typed = Label(win, fg = "black", font = ("Verdana",25,"bold","italic"), text = f"Characters : 0")
show_of_characs_typed.place(x = 0, y = 350)
#Commands

def instructions_command():
    win2 = Tk()
    win2.title("Instructions")
    win2.geometry("400x200")
    win2.resizable(False,False)
    win.option_add('*Dialog.msg.font', 'Helvetica 12')
    label_of_small_window = Label(win2,text = "Instructions:\n A Random word will be displayed on your screen. \n To test your speed, type that word in the textbox and hit \"enter\" \n Don't forget to press 'start' before you do so. \n There is no word limit. You get 60s , make the most of it!!. \n Your result will be displayed after the timer ends!\n Made by Vishy")
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
