from tkinter import*
root=Tk()
def click():
    text1="address:" + mytext.get('1.0',END)
    lbl.config(text=str(text))
mytext=Text(root) 