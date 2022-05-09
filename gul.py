from tkinter import *
from xml.dom.minidom import Entity
root =Tk()#TK라는 클래스를 가지고 와 root에 넣어주기
root.title("신미림")
e= Entry(root)#e라는 엔트리를 만들어줌 
e.pack()#이것을 써야지만 엔트리가 나타난다.만들고 나서 보여줘라
e.insert(0,"hello")

L =Label(root,text="hello")#레이블로 하는 방법
L.pack()

b= Button(root,text="hello")#버튼 생성 
b.pack()

def hello():
    print("만점입니다.")

b= Button(root,text="A",command=hello)#버튼 생성  COMMAND:어떤 함수로 연결되도록 하여라
b.pack()


root.mainloop()