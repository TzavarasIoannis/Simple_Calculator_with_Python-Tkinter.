#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox


win = tk.Tk()  # create window 


win.title("Calculator") #windows title 
win.geometry("880x350") #fix the size of the window
win.resizable(True, True)  #make it resizable



number = tk.IntVar()  # Declare the type of number var 


window = Entry(win , width = 100 , font = ('Verdana',10))  # Main box 
window.pack(ipady=9)

window.grid(row = 0 , column = 0 , columnspan = 30 , pady = 10)  # specify the place of the main window

#def for buttom equal 
def button_equal():   
    sec = window.get()   #get the last typed number 
    window.delete(0,END) # clear the window
    # if maths is add : 
    if   calc == 'add': 
    # insert into window the addition of the global variable number_1 ( the previous number ) plus the current number sec
        
        window.insert(0, float(sec) + float( number_1) )
    # if maths is add :         
    elif calc == 'substract':
    # insert into window the substract of the global variable number_1 ( the previous number ) - the current number sec

        window.insert(0,(   float( number_1)  - float(sec)) )
    # if maths is deviation : 
    elif calc == 'dev':
    # insert into window the deciation of the global variable number_1 ( the previous number )  /  the current number sec
        if sec != 0 : # YOU CANT'T devide with 0
            messagebox.showwarning('Warning','ERROR: think twice before devide with zero  :-) ') #pop up an Warning message 
        else: 
            window.insert(0, float(number_1 ) / float( sec)  ) 
    # if maths is multiply : 
    elif calc == 'mult':
    # insert into window the calculation of the global variable number_1 ( the previous number )  multiplied by  the current number sec

        window.insert(0,float (sec) * float(number_1))
    # if maths is frequency : 
    elif calc == 'freq':
    # insert into window the  global variable number_1 devided by 100 

        window.insert(0,float ( number_1 / 100 ))

# function for the numbers 
def button_click(num):
    now =window.get()    # get the  number 
    window.delete(0,END) #clear th window
    window.insert(0,str(now) + str(num))  # show the number , if the user type another number type the newest number 1st

# function for button clear
def button_clear():
    window.delete(0,END)  #delete everything in  window

#function for addition button 
def button_add():
    global calc # declare a global variable for the type of the calculation 

    calc = 'add' #if the + button clicked then the calc variable is equal to  'add'
    eq = '+'      #declare a string to show in window 

    global number_1  # declare a global variable for the fisrt number 
    number1 = window.get()  #get the number
    number_1 = float(number1) # make sure that is a float number  (or a number )
    window.insert(0,eq)   # show the calculation type 
    window.delete(0,END)  # delete everything on the window
    
def button_deduction():
    global calc

    calc = 'substract'
    eq = '-'
    
    global number_1
    number1 = window.get()
    number_1 = float(number1)
    window.insert(0,eq)
    window.delete(0,END) 
    
    
def button_dev():
    global calc

    calc = 'dev'
    eq = '/'
    global number_1

    number1 = window.get()
    number_1 = float(number1)
    window.insert(0,str (eq) )
    window.delete(0,END)
    
def button_mult():
    global calc

    calc = 'mult'
    eq = '*'
    global number_1

    number1 = window.get()
    number_1 = float(number1)
    window.insert(0,eq)
    window.delete(0,END) 

def button_freq():
    global calc

    calc = 'freq'
    eq = '%'  
    global number_1

    number1 = window.get()
    number_1 = float(number1)
    window.insert(0,eq)
    window.delete(0,END) 
    window.insert(0,float ( number_1 / 100 ))  # show the % 

    
#set the style for the buttons
style = Style()  
style.configure('W.TButton', font =
               ('calibri', 12, 'bold'), 
                foreground = 'black') 

#results = ttk.Label(win , text = 'return_the_res'  )
# Demostrate the numbers as buttons 
# only with the lambda function we can give an entry in the button_click() function 
number0 = ttk.Button(win, text='0' , width= 15 , padding  =8 ,style='W.TButton' , command = lambda :button_click(0))
#specify the place on the window 
number0.grid(row = 4 , column = 1)

number1 = ttk.Button(win, text='1' , width= 15 , padding =15 ,style='W.TButton',command = lambda :button_click(1))
number1.grid(row =1 , column =0 )

number2 = ttk.Button(win, text='2' , width= 15 , padding =15 ,style='W.TButton', command = lambda :button_click(2))
number2.grid(row =1 , column = 1)

number3 = ttk.Button(win, text='3' , width= 15 , padding =15  ,style='W.TButton',command = lambda :button_click(3))
number3.grid(row =1 , column = 2)

number4 = ttk.Button(win, text='4' , width= 15 , padding =15   ,style='W.TButton', command = lambda :button_click(4))
number4.grid(row = 2, column = 0 )

number5 = ttk.Button(win, text='5' , width= 15 , padding =15,style='W.TButton', command = lambda :button_click(5))
number5.grid(row = 2, column = 1)

number6 = ttk.Button(win, text='6' , width= 15 , padding = 15,style='W.TButton', command = lambda :button_click(6))
number6.grid(row = 2, column = 2)

number7 = ttk.Button(win, text='7' , width= 15, padding = 15 ,style='W.TButton', command = lambda :button_click(7))
number7.grid(row = 3, column = 0)

number8 = ttk.Button(win, text='8' , width= 15, padding =15 ,style='W.TButton', command = lambda :button_click(8) )
number8.grid(row = 3, column = 1)

number9 = ttk.Button(win, text='9' , width= 15 , padding = 15,style='W.TButton', command = lambda :button_click(9))
number9.grid(row = 3, column = 2)

                       
#demostrate the math symbols 

#addition button
add_button = ttk.Button( win , text= '+' , width = 25 , padding = 8 , style='W.TButton' ,  command=button_add)
#specify the place on the window 
add_button.grid(row = 1 ,  column =4 )

#deviation button
dev_button = ttk.Button( win , text= '/' , width = 25 , padding = 8,style='W.TButton' ,  command=button_dev)
dev_button.grid(row = 2  ,  column =  4)

#multiply button
mult_button = ttk.Button( win , text= '*' , width = 25 , padding =   8,style='W.TButton' ,   command=button_mult)
mult_button.grid(row = 3   ,  column =  4)

#substract button
deduction_button = ttk.Button( win , text= '-' , width = 25 , padding =  8,style='W.TButton' ,  command = button_deduction)
deduction_button.grid(row = 4 ,  column = 0)

#frequency button
freq_button = ttk.Button(  win , text= '%' , width = 25 , padding = 8,style='W.TButton' , command = button_freq)
freq_button.grid(row = 4 ,  column = 2 )

#equal button
eq_button = ttk.Button(  win , text= '=' , width = 25 , padding = 8 ,style='W.TButton' , command = button_equal)
eq_button.grid(row = 4 ,  column = 4)

#clear button
clear_button = ttk.Button(  win , text= 'Clear' , width = 25 , padding = 8   ,style='W.TButton' , command =  button_clear)
clear_button.grid(row = 5 ,  column = 0 , columnspan = 3)




# loop for main class 
win.mainloop()


# In[ ]:





# In[ ]:




