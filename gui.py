from tkinter import *


app = Tk()
app.geometry("500x170")
app.title('IP-Practice')


def callback():
    print("called the callback!")


# create a menu
menu = Menu(app)
app.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Settings", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

Label(app, text="For the IP-adress 192.168.1.1/24 calculate the following:").grid(row=0, column=0, columnspan=40)
#Create the input forms
Label(app, text="Network-ID").grid(row=10,column=0)
e1 = Entry(app)
e1.grid(row=10,column=10)

Label(app, text="Netmask").grid(row=20,column=0)
e2 = Entry(app)
e2.grid(row=20,column=10)

Label(app, text="First host").grid(row=10,column=30)
e3 = Entry(app)
e3.grid(row=10,column=40)

Label(app, text="Last host").grid(row=20,column=30)
e4 = Entry(app)
e4.grid(row=20,column=40)

Label(app, text="Possible hosts").grid(row=30,column=0)
e4 = Entry(app)
e4.grid(row=30,column=10)

Label(app, text="Broadcast address").grid(row=30,column=30)
e4 = Entry(app)
e4.grid(row=30,column=40)

Label(app, text="Possible subnets").grid(row=40,column=0)
e4 = Entry(app)
e4.grid(row=40,column=10)

Label(app, text="Is the address valid").grid(row=40,column=30)
Label(app, text="for use on the internet?").grid(row=50,column=30)

v=0
Radiobutton(app, text='Ja ', padx = 20, variable=v, value=1).grid(row=40, column=40)
Radiobutton(app, text='Nej', padx = 20, variable=v, value=1).grid(row=50, column=40)

# create a toolbar
toolbar = Frame(app)
b = Button(toolbar, text="New test", width=6, command=callback).grid(row=0, column=0, padx=2, pady=2)
b = Button(toolbar, text="Show all", width=6, command=callback).grid(row=0, column=1, padx=2, pady=2)
b = Button(toolbar, text="Clear all", width=6, command=callback).grid(row=0, column=2, padx=2, pady=2)
toolbar.grid(row=100, column=0, columnspan=40)


app.mainloop()
