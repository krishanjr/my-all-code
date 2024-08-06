from tkinter import * 
window=Tk()
e=Entry(window,width=50,bg="blue",fg="white",borderwidth=5,font=20)
e.pack()
def myClick():
    myLabel=Label(window,text="Hello"+e.get())
    myLabel.pack()
btn=Button(window,text="Click me",padx=10,pady=10,command=myClick)
btn.pack()
window.mainloop()