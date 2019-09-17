
from tkinter import *
from tkinter import messagebox, ttk

id = 100000
employees = []

class Employees:

    def __init__(self, n, d, p, r):
        self.n = n
        self.d = d
        self.p = p
        self.r = r


def add():
    global id
    id += 1

    n = e1.get()
    d = e2.get()
    p = e3.get()
    r = e4.get()

    if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "":

        messagebox.showerror("Error", "Please fill in all the fields")

    else:

        employees.append(Employees(n, d, p, r))

        tview.insert('', "end", text=id, values=(n, d, p, r))

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

        messagebox.showinfo("Add", "Successfully added")

def delete():
    try:
     selected_item = tview.selection()[0]
     tview.delete(selected_item)

     e1.delete(0, END)
     e2.delete(0, END)
     e3.delete(0, END)
     e4.delete(0, END)

     messagebox.showinfo("Delete", "Entry deleted successfully")

    except IndexError:
        messagebox.showerror("Error","Select the row you want to delete")
def updatetreeview():
    try:
        selected_item = tview.selection()[0]
        tview.item(selected_item, values=(e1.get(), e2.get(), e3.get(), e4.get()))
        messagebox.showinfo("updated", "Updated successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

    except IndexError:
        messagebox.showerror("Error","Select the row you want to update")


def clearfields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def transfertext(onClickRowTreeview):
    selected_item = tview.selection()[0]

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    e1.insert(0, tview.item(selected_item)["values"][0])
    e2.insert(0, tview.item(selected_item)["values"][1])
    e3.insert(0, tview.item(selected_item)["values"][2])
    e4.insert(0, tview.item(selected_item)["values"][3])

master = Tk().title("Employee management system")

Label(master, text='Name').grid(row=0, column=0)
Label(master, text='Department').grid(row=0, column=2)
Label(master, text='Position').grid(row=1, column=0)
Label(master, text='Rate').grid(row=1, column=2)
tview = ttk.Treeview(master, columns=('ID', 'Name', 'Position','Department'))
tview.bind('<ButtonRelease-1>', transfertext)
tview.grid(row=7, column=0, columnspan=10)

tview.heading('#0', text="ID")
tview.heading('#1', text="Name")
tview.heading('#2', text="Department")
tview.heading('#3', text="Position")
tview.heading('#4', text="Rate")


e1 = Entry(master, width="30")
e2 = Entry(master, width="30")
e3 = Entry(master, width="30")
e4 = Entry(master, width="30")

e1.grid(row=0, column=1, pady=10)
e2.grid(row=0, column=3, pady=10)
e3.grid(row=1, column=1, pady=10)
e4.grid(row=1, column=3, pady=10)

b1 = Button(master, text="Add", width="25", command=add)
b1.grid(row=3, column=0, pady=10)
b2 = Button(master, text="Update", width="25", command=updatetreeview)
b2.grid(row=3, column=1, pady=10)
b3 = Button(master, text="Delete", width="25", command=delete)
b3.grid(row=3, column=2, pady=10)
b4 = Button(master, text="Clear fields", width="25", command=clearfields)
b4.grid(row=3, column=3, pady=10)
mainloop()