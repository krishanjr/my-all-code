from tkinter import*
## import MessageBox
top =Tk()
def add():
    label.config(text=CheckVar1.get())
CheckVar1 = IntVar()

C1 = Checkbutton(top, text="Music", variable = CheckVar1, \
               onvalue =1, offvalue = 0, heigh=5, \
                width = 20
                )

C1.pack()
btn=Button(top,text="CLick",command=add)
label=Label(top,text="")
label.pack()
btn.pack()
top.mainloop()