from tkinter import *
import backend
'''
FUNCTIONS TO CONNECT BACKEND AND FRONTEND
'''
def view_command():
    list.delete(0,END)
    for row in backend.view_all():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(e1val.get(),e2val.get(),e3val.get(),e4val.get()):
        list.insert(END,row)

def add_entry():
    backend.insert(e1val.get(),e2val.get(),e3val.get(),e4val.get())
    view_command()

def get_selected_row(event):
    global selected_tuple
    index = list.curselection()[0]
    selected_tuple=list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def command_delete():
    backend.delete(selected_tuple[0])
    view_command()

def command_update():
    backend.update(selected_tuple[0],e1val.get(),e2val.get(),e3val.get(),e4val.get())
    view_command()



'''
FRONT END SECTION CONSITS OF BUTTONS
'''
window = Tk()

l1 = Label(window,text="BOOK NAME")
l1.grid(row=0,column=0)
l2 = Label(window,text="AUTHOR")
l2.grid(row=0,column=2)
l3 = Label(window,text="YEAR")
l3.grid(row=1,column=0)
l4 = Label(window,text="UNIQ NO.")
l4.grid(row=1,column=2)

e1val = StringVar()
e1 = Entry(window,textvariable=e1val)
e1.grid(row=0,column=1)
e2val = StringVar()
e2 = Entry(window,textvariable=e2val)
e2.grid(row=0,column=3)
e3val = StringVar()
e3 = Entry(window,textvariable=e3val)
e3.grid(row=1,column=1)
e4val = StringVar()
e4 = Entry(window,textvariable=e4val)
e4.grid(row=1,column=3)

list = Listbox(window,height=6 , width = 35)
list.grid(row=2,column=0,rowspan = 6,columnspan=2 )

sb = Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

list.bind("<<ListboxSelect>>",get_selected_row)

b1 = Button(window,text = "VIEW ALL",width=12,command=view_command)
b1.grid(row=2,column=3)
b2 = Button(window,text = "SEARCH",width=12,command=search_command)
b2.grid(row=3,column=3)
b3 = Button(window,text = "ADD ENTRY",width=12,command=add_entry)
b3.grid(row=4,column=3)
b4 = Button(window,text = "UPDATE",width=12,command=command_update)
b4.grid(row=5,column=3)
b5 = Button(window,text = "DELETE",width=12,command=command_delete)
b5.grid(row=6,column=3)
b6 = Button(window,text = "CLOSE",width=12,command = window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
