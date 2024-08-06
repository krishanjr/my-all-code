from tkinter import*
root = Tk()


def show_password():
    if a.get() == 1:
        ent.config(show="")
    else:
        
        ent.config(show="*")

lbl = Label(text="password")
lbl.place(x=20, y=10)
ent = Entry(show="*")
ent.place(x=20, y=30)
a = IntVar()
chk = Checkbutton(
    text="show password", variable=a, onvalue=1, offvalue=0, command=show_password
)
chk.place(x=20, y=50)
btn= Button(text="submit")
btn.place(x=20, y=100)
root.mainloop()
