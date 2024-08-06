from tkinter import *
window=Tk()
def myClick():
    myLabel=Label(window,text="Look! I clicked a button", fg="red",bg="#000099",font=50)
    myLabel.pack()
my_button=Button(window,text="Click me",padx=10,pady=10,command=myClick,fg="red",bg="blue")
my_button.pack()
window.mainloop()