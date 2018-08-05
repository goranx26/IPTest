from tkinter import *
import core

app = Tk()
app.geometry("400x340")
app.title('Subnetting practice')
answers = core.get_test_ip()


def get_new_ip():
    clear_all()
    new_ip = core.get_test_ip()
    return new_ip


def show_all():
    clear_all()
    e[1].insert(0, answers.nw.network_address)
    e[2].insert(0, answers.nw.netmask)
    e[3].insert(0, answers.all_hosts[0])
    e[4].insert(0, answers.all_hosts[-1])
    e[5].insert(0, answers.nw.broadcast_address)
    e[6].insert(0, str(answers.nw.num_addresses - 2))
    # e[7].insert(0, 'Only in paid version')
    app.update_idletasks()


def clear_all():
    e[1].delete(0, END)
    e[2].delete(0, END)
    e[3].delete(0, END)
    e[4].delete(0, END)
    e[5].delete(0, END)
    e[6].delete(0, END)
    e[7].delete(0, END)

    for i in range(1, 9):
        grade[i] = Label(form, text="").grid(row=(i * 10), column=40)
        i += 1
    app.update()


def show_this(num, val):
    e[num].insert(0, val)


def show_grade(num, val):
    if e[num].get() == val:
        grade[num] = Label(form, text="CORRECT").grid(row=(num * 10), column=40)
    else:
        grade[num] = Label(form, text="WRONG").grid(row=(num * 10), column=40)







# create a menu
menu = Menu(app)
app.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Settings", menu=filemenu)
filemenu.add_command(label="New", command=core.callback)
filemenu.add_command(label="Choose IP", command=core.callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=lambda: exit())

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=core.callback)

labelIP = Label(app, text="For IP-adress: " + str(answers.nw) + " calculate the following:").grid(row=0, column=1)


# Create the input forms
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


# create the input validation text (right/wrong answer)
grade = {}
for i in range(1, 9):
    grade[i] = Label(form, text="").grid(row=(i * 10), column=40)
    i += 1

# Create the 'show' buttons
show_button1 = Button(form, text="Check", width=5, command=lambda: show_grade(1, str(answers.nw.network_address))).grid(row=10, column=30, padx=2, pady=2)
show_button2 = Button(form, text="Check", width=5, command=lambda: show_grade(2, str(answers.nw.netmask))).grid(row=20, column=30, padx=2, pady=2)
show_button3 = Button(form, text="Check", width=5, command=lambda: show_grade(3, str(answers.all_hosts[0]))).grid(row=30, column=30, padx=2, pady=2)
show_button4 = Button(form, text="Check", width=5, command=lambda: show_grade(4, str(answers.all_hosts[-1]))).grid(row=40, column=30, padx=2, pady=2)
show_button5 = Button(form, text="Check", width=5, command=lambda: show_grade(5, str(answers.nw.broadcast_address))).grid(row=50, column=30, padx=2, pady=2)
show_button6 = Button(form, text="Check", width=5, command=lambda: show_grade(6, str(answers.nw.num_addresses - 2))).grid(row=60, column=30, padx=2, pady=2)
# show_button7 = Button(form, text="Check", width=5, command=lambda: show_grade(7)).grid(row=70, column=30, padx=2, pady=2)
# show_button8 = Button(form, text="Check", width=5, command=lambda: show_this(1, answers.nw.network_address)).grid(row=80, column=30, padx=2, pady=2)




# create a toolbar
toolbar = Frame(app)
b1 = Button(toolbar, text="New test", width=6, command=get_new_ip).grid(row=0, column=0, padx=2, pady=2)
b2 = Button(toolbar, text="Show all", width=6, command=show_all).grid(row=0, column=1, padx=2, pady=2)
b3 = Button(toolbar, text="Clear all", width=6, command=clear_all).grid(row=0, column=2, padx=2, pady=2)
toolbar.grid(row=100, column=0, columnspan=40)


app.mainloop()
