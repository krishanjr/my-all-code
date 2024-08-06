from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("LOGIN")
my_image=Image.open("gaming.jpg")
resized_image=my_image.resize((1000,750))
converted_image=ImageTk.PhotoImage(resized_image)
mylabel=Label(window,image=converted_image)
mylabel.pack()
window.mainloop() 