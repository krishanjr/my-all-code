from tkinter import *

root = Tk()
root.iconbitmap("taxi.ico")#for inserting logo on top
root.title("login")#for title changes
root.geometry("300x400")# for length and width purposes
root.resizable(0,0)# for not maximizing the page
root.maxsize(width=300,height=300)
root.minsize(width=300,height=200)
redbutton=Button(root,text="LEFT",fg="green")
redbutton.pack(side=LEFT)
greenbutton=Button(root,text="RIGHT",fg="black")
greenbutton.pack(side=RIGHT)
bluebutton=Button(root,text="TOP",fg="blue")
bluebutton.pack(side=TOP)
blackbutton=Button(root,text="BOTTOM",fg="red")
blackbutton.pack(side=BOTTOM)
mainloop()