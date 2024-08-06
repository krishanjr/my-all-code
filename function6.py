from tkinter import *
root= Tk()
root.title("GUI")
root.maxsize(width=600,height=300)
root.minsize(width=600,height=300)
#function
def add():
    x=var.get()
    print(x)
    mylabell.config(text=x,bg="green")
mylabel=Label(root,text="User Name",fg="red",bg="yellow")#label 1
mylabel.place(x=10,y=120)
mylabell=Label(root,text="Nothing",fg="red",bg="yellow")#Label 2
mylabell.place(x=40,y=120)
var= StringVar()
ent=Entry(root,bg="black",fg='white',textvariable=var)
ent.place(x=80,y=10)
btn=Button(root,text="Submit",bg="green",fg="white",command=add)
btn.place(x=20,y=80)
root.mainloop()