rom tkinter import *
window=Tk()
window.maxsize(width=300,height=300)
window.minsize(width=300,height=300)
def func():
    print("Button is clicked")
btn= Button(window,text="Login",command=func)
btn.pack(side="top")
window.mainloop()