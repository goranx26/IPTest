from tkinter import *
import core

app = Tk()
app.geometry("420x340")
app.title('Subnetting practice')

answers = core.get_test_ip()

def show_all():
    e[1].insert(0, answers.nw.network_address)
    e[2].insert(0, answers.nw.netmask)
    e[3].insert(0, answers.all_hosts[0])
    e[4].insert(0, answers.all_hosts[-1])
    e[5].insert(0, answers.nw.broadcast_address)
    e[6].insert(0, str(answers.nw.num_addresses - 2))
    e[7].insert(0, 'Only in paid version')


def clear_all():
    e[1].delete(0, END)
    e[2].delete(0, END)
    e[3].delete(0, END)
    e[4].delete(0, END)
    e[5].delete(0, END)
    e[6].delete(0, END)
    e[7].delete(0, END)


def show_this(num):
    e[num].insert(0, str(answers.nw.network_address))



# create a menu
menu = Menu(app)
app.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Settings", menu=filemenu)
filemenu.add_command(label="New", command=core.callback)
filemenu.add_command(label="Choose IP", command=core.callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=core.callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=core.callback)

Label(app, text="For IP-adress: " + str(answers.nw) + " calculate the following:").grid(row=0, column=1)


#Create the input forms
e = {}
form = Frame(app)
Label(form, text="Network-ID").grid(row=10, column=10)
e[1] = Entry(form)
e[1].grid(row=10, column=20)

Label(form, text="Netmask").grid(row=20, column=10)
e[2] = Entry(form)
e[2].grid(row=20, column=20)

Label(form, text="First host").grid(row=30, column=10)
e[3] = Entry(form)
e[3].grid(row=30, column=20)

Label(form, text="Last host").grid(row=40, column=10)
e[4] = Entry(form)
e[4].grid(row=40, column=20)

Label(form, text="Broadcast address").grid(row=50, column=10)
e[5] = Entry(form)
e[5].grid(row=50, column=20)

Label(form, text="Nr of possible hosts").grid(row=60, column=10)
e[6] = Entry(form)
e[6].grid(row=60, column=20)

Label(form, text="Possible subnets").grid(row=70, column=10)
e[7] = Entry(form)
e[7].grid(row=70, column=20)

Label(form, text="Is the address valid\nfor use on the internet?").grid(row=80, column=10)
Label(form, text="").grid(row=90, column=10)


reserved = ''
Radiobutton(form, text='Ja ', padx=20, variable=reserved, value='n').grid(row=80, column=20)
Radiobutton(form, text='Nej', padx=20, variable=reserved, value='j').grid(row=90, column=20)
form.grid(row=2, column=1)


#Create the 'show' buttons
for i in range(1, 8):
    show_button = Button(
        form, text="Check", width=5, command=show_this(i)).grid(row=(i * 10), column=30, padx=2, pady=2)
    i += 1

#create the input validation text (right/wrong answer)
grade = {}
for i in range(1, 9):
    grade[i] = Label(form, text="").grid(row=(i * 10), column=40)
    i += 1


# create a toolbar
toolbar = Frame(app)
b = Button(toolbar, text="New test", width=6, command=clear_all).grid(row=0, column=0, padx=2, pady=2)
b = Button(toolbar, text="Show all", width=6, command=show_all).grid(row=0, column=1, padx=2, pady=2)
b = Button(toolbar, text="Clear all", width=6, command=clear_all).grid(row=0, column=2, padx=2, pady=2)
toolbar.grid(row=100, column=0, columnspan=40)


app.mainloop()
