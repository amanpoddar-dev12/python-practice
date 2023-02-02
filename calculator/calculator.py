from ast import Expression
from logging import root
from tkinter import *

from numpy import equal, multiply, number
from pyparsing import col
#pyhton gui project by  Aman Poddar
exp=''   #this variable to store user enterned expression

#this  function for store the value and expression by user
def press(number):
    global exp
    exp+=str(number)
    equation.set(exp)
def equalpress():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        expression=''
    except:
        equation.set("syntax error")
        exp=""
def clear():
    global exp
    exp=''
    equation.set('')
#to create root window
tk=Tk()
tk.configure(bg='grey')
tk.title('calculator by  aman poddar')
tk.geometry('180x180')

equation=StringVar()

Text_Entry_Box=Entry(tk,textvariable=equation,width=20)
Text_Entry_Box.grid(columnspan=8,ipadx=100)
button1=Button(tk,text='1',fg='black',bg='#8f8f8f',command=lambda:press(1),height=2,width=7)
button1.grid(row=2,column=0)

button2=Button(tk,text='2',fg='black',bg='#8f8f8f',command=lambda:press(2),height=2,width=7)
button2.grid(row=2,column=1)

button3=Button(tk,text='3',fg='black',bg='#8f8f8f',command=lambda:press(3),height=2,width=7)
button3.grid(row=2,column=2)

button4=Button(tk,text='4',fg='black',bg='#8f8f8f',command=lambda:press(4),height=2,width=7)
button4.grid(row=3,column=0)

button5=Button(tk,text='5',fg='black',bg='#8f8f8f',command=lambda:press(5),height=2,width=7)
button5.grid(row=3,column=1)

button6=Button(tk,text='6',fg='black',bg='#8f8f8f',command=lambda:press(6),height=2,width=7)
button6.grid(row=3,column=2)

button7=Button(tk,text='7',fg='black',bg='#8f8f8f',command=lambda:press(7),height=2,width=7)
button7.grid(row=4,column=0)

button8=Button(tk,text='8',fg='black',bg='#8f8f8f',command=lambda:press(8),height=2,width=7)
button8.grid(row=4,column=1)

button9=Button(tk,text='9',fg='black',bg='#8f8f8f',command=lambda:press(9),height=2,width=7)
button9.grid(row=4,column=1)
button0=Button(tk,text='0',fg='black',bg='#8f8f8f',command=lambda:press(0),height=2,width=7)
button0.grid(row=5,column=0)
plus=Button(tk,text='+',fg='black',bg='#8f8f8f',command=lambda:press('+'),height=2,width=7)
plus.grid(row=2,column=3)

minus=Button(tk,text='-',fg='black',bg='#8f8f8f',command=lambda:press('-'),height=2,width=7)
minus.grid(row=3,column=3)

multiply=Button(tk,text='x',fg='black',bg='#8f8f8f',command=lambda:press('*'),height=2,width=7)
multiply.grid(row=4,column=3)

devide=Button(tk,text='/',fg='black',bg='#8f8f8f',command=lambda:press('/'),height=2,width=7)
devide.grid(row=5,column=3)
equal=Button(tk,text='=',fg='black',bg='#8f8f8f',command=equalpress,height=2,width=7)
equal.grid(row=5,column=2)
clear=Button(tk,text='clear',fg='black',bg='#8f8f8f',command=clear,height=2,width=7)
clear.grid(row=5,column=1)


tk.mainloop()


        


