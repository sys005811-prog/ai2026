'''
#GUI 기본형식 
from tkinter import *

window = Tk()

   # +GUI code

window.mainloop()


from tkinter import *

window = Tk() 

window.title(121212)
window.geometry("200x200")
window.resizable(width=False, height=False) #창 크기 고정 

window.mainloop()



from tkinter import *

window = Tk()
label1=Label(window, text = 'abc')
label2=Label(window, text='afe',bg='red',font=('궁서체',20),fg='blue')

label1.pack()
label2.pack()

window.mainloop()


from tkinter import *

window = Tk()

photo1=PhotoImage(file='white-dog-shaking.gif')
photo2=PhotoImage(file='ricardo.gif')
label1=Label(window,image=photo1)
label2=Label(window,image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()

#
from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("버튼1","애옹")

window = Tk()

photo1=PhotoImage(file='ricardo.gif')
button1=Button(window,image=photo1, command=myFunc)

button1.pack()


window.mainloop()

#
from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc():
    if chk.get() ==0:
        messagebox.showinfo("","체크버튼이 꺼짐.")
    else:
        messagebox.showinfo("","체크버튼 켜짐.")
        

chk=IntVar()
cb1=Checkbutton(window,text='클릭하셈', variable=chk, command=myFunc)

cb1.pack()

 
window.mainloop()


#
from tkinter import *

btnList=[None]*9
fnameList=["ricardo.gif"]*9
photoList=[None]*9
i,k=0,0
xPos,yPos=0,0
num=0

window = Tk()
window.geometry("600x600")

for i in range(0,9):
    photoList[i]=PhotoImage(file=fnameList[i])
    btnList[i]=Button(window,image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos,y=yPos)
        num+=1
        xPos+= 200
    xPos=0
    yPos+= 200
 
window.mainloop()

'''



from tkinter import *
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo('마우스','좌클릭')

window=Tk()

window.bind('<Button-1>',clickLeft)

window.mainloop()





















