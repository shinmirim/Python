from tkinter import *
window = Tk()

total= 0

def add():
    global total 
    total+=int(e.get())
    L2.config(text=total)
    e.delete(0,END)

def subtract():
    global total
    total-=int(e.get())
    L2.config(text=total)
    e.delete(0,END)

def clear():
    global total 
    total = 0 
    L2.config(text=total)
    e.delete(0,END)











L=Label(window,text="현재합계:")
L.grid(row=0,column=0)

L2=Label(window,text=total)
L2.grid(row=0,column=1,columnspan=2)


e= Entry(window)
e.grid(row=1,column=0,columnspan=3)


b1=Button(window,text="더하기(+)",command=add)
b1.grid(row=2,column=0)
b2=Button(window,text="뺴기(-)",command=subtract)
b2.grid(row=2,column=1)
b3=Button(window,text="초기화",command=clear)
b3.grid(row=2,column=2)

