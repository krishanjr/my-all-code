from tkinter import *

root = Tk()
root.iconbitmap("taxi.ico")#for inserting logo on top
root.title("login")#for title changes
root.geometry("300x400")# for length and width purposes
root.resizable(0,0)# for not maximizing the page
root.maxsize(width=300,height=300)
root.minsize(width=300,height=200)
# redbutton=Button(root,text="LEFT",fg="green")
# redbutton.pack(side=LEFT)
# greenbutton=Button(root,text="RIGHT",fg="black")
# greenbutton.pack(side=RIGHT)
# bluebutton=Button(root,text="TOP",fg="blue")
# bluebutton.pack(side=TOP)
# blackbutton=Button(root,text="BOTTOM",fg="red")
# blackbutton.pack(side=BOTTOM)
# e1=Entry(root).grid(row=0,column=1)
# password=Label(root,text="Password").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# submit=Button(root,text="Submit").grid(row=4,column=1)

name=Label(root,text="Name").place(x=30,y=50)
address=Label(root,text="Address").place(x=30,y=93)
contact=Label(root,text="Contact").place(x=30,y=130)
e1=Entry(root).place(x=80,y=50)
e2=Entry(root).place(x=80,y=90)
e3=Entry(root).place(x=95,y=130)

root.mainloop()

