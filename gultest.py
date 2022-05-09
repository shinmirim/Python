from tkinter import *

root = Tk()


L1 = Label(root, text="화씨")
L2 = Label(root, text="섭씨")

L1.pack()
L2.pack()

e1 = Entry(root)
e2 = Entry(root)

e1.pack()
e2.pack()

def ftemp(): 
        ctemp = float(e1.get())
        ftemp = round((ctemp-32)*5/9,2)
        e2.delete(0, END)
        e2.insert(0,ftemp)# 내가 계산한 것을 e2에 넣겠다
def ctemp():
        ftemp = float(e2.get())
        ctemp = round((ftemp*9/5)+32,2)
        e1.delete(0,END)
        e1.insert(0,ctemp)# 내가 계산한 것을 e2에 넣겠다


b1 = Button(root, text="화씨->섭씨",command=ftemp)
b2 = Button(root, text="섭씨->화씨",command=ctemp)

b1.pack()
b2.pack()










root.mainloop()