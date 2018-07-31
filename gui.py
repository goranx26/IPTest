from tkinter import *
import core


app = Tk()
app.geometry("500x170")
app.title('IP-Practice')


def get_testip():
    testip = core.get_test_ip()
    answers = core.Answer(testip['addr'], testip['mask'])
    return answers


get_testip()





answers = get_testip()


def show_all():
    e1.insert(0, answers.nw.network_address)
    e2.insert(0, answers.nw.netmask)
    e3.insert(0, answers.all_hosts[0])
    e4.insert(0, answers.all_hosts[-1])
    e5.insert(0, str(answers.nw.num_addresses - 2))
    e6.insert(0, answers.nw.broadcast_address)
    e7.insert(0, 'Only in paid version')

def clear_all():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)



# create a menu
menu = Menu(app)
app.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Settings", menu=filemenu)
filemenu.add_command(label="New", command=core.callback)
filemenu.add_command(label="Open...", command=core.callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=core.callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=core.callback)


Label(app, text="For IP-adress: " + str(answers.nw) + " calculate the following:").grid(row=0, column=1)
#Create the input forms
form = Frame(app)
Label(form, text="Network-ID").grid(row=10,column=0)
e1 = Entry(form)
e1.grid(row=10,column=10)


Label(form, text="Netmask").grid(row=20,column=0)
e2 = Entry(form)
e2.grid(row=20,column=10)


Label(form, text="First host").grid(row=10,column=30)
e3 = Entry(form)
e3.grid(row=10,column=40)

Label(form, text="Last host").grid(row=20,column=30)
e4 = Entry(form)
e4.grid(row=20,column=40)

Label(form, text="Possible hosts").grid(row=30,column=0)
e5 = Entry(form)
e5.grid(row=30,column=10)

Label(form, text="Broadcast address").grid(row=30,column=30)
e6 = Entry(form)
e6.grid(row=30,column=40)

Label(form, text="Possible subnets").grid(row=40,column=0)
e7 = Entry(form)
e7.grid(row=40,column=10)

Label(form, text="Is the address valid").grid(row=40,column=30)
Label(form, text="for use on the internet?").grid(row=50,column=30)

v=0
Radiobutton(form, text='Ja ', padx = 20, variable=v, value=1).grid(row=40, column=40)
Radiobutton(form, text='Nej', padx=20, variable=v, value=1).grid(row=50, column=40)
form.grid(row=2, column=1)



# create a toolbar
toolbar = Frame(app)
b = Button(toolbar, text="New test", width=6, command=clear_all).grid(row=0, column=0, padx=2, pady=2)
b = Button(toolbar, text="Show all", width=6, command=show_all).grid(row=0, column=1, padx=2, pady=2)
b = Button(toolbar, text="Clear all", width=6, command=clear_all).grid(row=0, column=2, padx=2, pady=2)
toolbar.grid(row=100, column=0, columnspan=40)


app.mainloop()
