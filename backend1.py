from tkinter import *
import sqlite3
root=Tk()
label_username = Label(root, text="Username", font=("Arial Bold", 20))
label_username.place(x=0, y=90)
label_address = Label(root, text="Address", font=("Arial Bold", 20))
label_address.place(x=0, y=140)
label_role = Label(root, text="Role", font=("Arial Bold", 20))
label_role.place(x=0, y=190)
label_salary = Label(root, text="Salary", font=("Arial Bold", 20))
label_salary.place(x=0, y=250)
 
username = Entry(root, width=30)
username.place(x=170, y=100, height=30)
address = Entry(root, width=30)
address.place(x=170, y=150, height=30)
role = Entry(root, width=30)
role.place(x=170, y=200, height=30)
salary = Entry(root, width=30)
salary.place(x=170, y=250, height=30)
delete_box = Entry(root, width=30)
delete_box.place(x=210, y=370, height=30)
 
lbl = Label(root, text="")
lbl.place(x=500, y=40)
 
btn_add = Button(root, text="Add", font=("Arial Bold", 20), command=add)
btn_add.place(x=0, y=300)  
btn_retrieve = Button(root, text="Retrieve", font=("Arial Bold", 20), command=retrieve)
btn_retrieve.place(x=100, y=300)
btn_delete = Button(root, text="Delete", font=("Arial Bold", 20), command=delete)
btn_delete.place(x=250, y=410)
btn_update = Button(root, text="Update", font=("Arial Bold", 20), command=edit)
btn_update.place(x=380, y=410)
 
 
# retrieve()
 
root.mainloop()