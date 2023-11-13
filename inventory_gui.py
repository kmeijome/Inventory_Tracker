#  Kevin Meijome, CIS 345, icourse Spring B, GUI Project

from tkinter import *
from PIL import Image, ImageTk
import inventory

user = {"kmeijome": {"password": '9999'}, "selin2": {"password": '1234'}}

# main window
win = Tk()
win.title('Inventory Tracker')
win.geometry('900x600')
win.columnconfigure(0, weight=1)
win.config(bg='#0040ff')

# variables used in GUI
username = StringVar()
password = StringVar()
item_num = StringVar()
item_data = StringVar()
add_item_num = StringVar()
add_item_desc = StringVar()
add_item_cost = DoubleVar()
add_item_qty = IntVar()


# displays successful login
def login_button():
    global username, password, log_label

    un = username.get()
    pw = password.get()

    if un not in user:
        log_label.config(text=username.get() + ' invalid User')
    elif pw != user[un]["password"]:
        log_label.config(text='Invalid Password')
    else:
        log_label.config(text=username.get() + ' logged in')
        search_button['state'] = NORMAL
        add_button['state'] = NORMAL


# search function of GUI that returns data for item # lookup
def item_search():
    global item_num, item_data, search_result
    # KeyError exception if not valid item number
    while True:
        try:
            item = inventory.get_item(str(item_num.get()))
            print(item)
            item_data.set(f'{item}')
            break
        except KeyError:
            item_data.set(f'Not a valid item number')
            break


# add item to inventory using Item class instance
def add_item():
    global add_item_num, add_item_desc, add_item_cost, add_item_qty
    item = inventory.Item(add_item_num.get(), add_item_desc.get(),
                          float(add_item_cost.get()), int(add_item_qty.get()))
    inventory.add_item(item)
    inventory.save()


# exits application and saves data to inventory
def close():
    global exit_button
    exit_button.config(win.quit())
    inventory.save()


# add company logo top left of gui
# logo = Image.open('../../../OneDrive/Desktop/Lowes.png')
# logo = ImageTk.PhotoImage(logo)
# logo_label = Label(image=logo)
# logo_label.image = logo
# logo_label.place(x=0, y=0)

# add a Menu to window
menubar = Menu(win)

# add File menu and exit command
filemenu = Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=win.quit)

# username label
username_label = Label(win, text='Username', bg='white', fg='black',
                       font=("Arial", 16), relief=RAISED)
username_label.place(x=250, y=20)

# username entry
username_entry = Entry(win, textvariable=username)
username_entry.place(x=355, y=20)

# password label
password_label = Label(win, text='Password', bg='white', fg='black',
                       font=("Arial", 16), relief=RAISED)
password_label.place(x=255, y=50)

# password entry
password_entry = Entry(win, textvariable=password)
password_entry.place(x=357, y=50)

# submit button for user login
login = Button(win, command=login_button,
               font=('Arial', 16, 'bold'), text='Login', width=10, relief=RAISED)
login.place(x=300, y=80)

# login result displayed
log_label = Label(win, text='', font=('Arial', 16), width=20)
log_label.place(x=300, y=130)

# search inventory label
search_button = Button(win, command=item_search, text='Item Lookup',
                       font=('Arial', 16, 'bold'), relief=RAISED, state=DISABLED)
search_button.place(x=10, y=250)

# entry field to input item number
search_entry = Entry(win, textvariable=item_num)
search_entry.place(x=160, y=250)

# label for look up result
result_label = Label(win, text='Inventory Lookup Result',
                     font=('Arial', 16), width=44, relief=RAISED)
result_label.place(x=300, y=210)

# will display item information based on num provided
search_result = Label(win, textvariable=item_data, width=75, height=5,
                      relief=SUNKEN, justify=LEFT)
search_result.place(x=300, y=250)

# add additional inventory
add_button = Button(win, command=add_item, text='Add Item',
                    font=('Arial', 16, 'bold'), relief=RAISED, width=10, state=DISABLED)
add_button.place(x=10, y=350)

# add entry for item number
add_item_num = Entry(win, textvariable=add_item_num)
add_item_num.place(x=160, y=350)

# label for add item num
add_item_label = Label(win, text='Item #', font=('Arial', 16), width=5)
add_item_label.place(x=160, y=370)

# add entry for item description
add_item_desc = Entry(win, textvariable=add_item_desc)
add_item_desc.place(x=290, y=350)

# label for add item desc
add_desc_label = Label(win, text='Description', font=('Arial', 16), width=10)
add_desc_label.place(x=290, y=370)

# add entry for item cost
add_item_cost = Entry(win, textvariable=add_item_cost)
add_item_cost.place(x=420, y=350)

# label for add item cost
add_cost_label = Label(win, text='Cost $', font=('Arial', 16), width=10)
add_cost_label.place(x=420, y=370)

# add entry for item qty
add_item_qty = Entry(win, textvariable=add_item_qty)
add_item_qty.place(x=550, y=350)

# label for add item qty
add_qty_label = Label(win, text='Qty', font=('Arial', 16), width=10)
add_qty_label.place(x=550, y=370)

# add entry for item number
exit_button = Button(win, command=close, font=('Arial', 16, "bold"), text='Exit')
exit_button.place(x=775, y=350)

win.config(menu=menubar)
win.mainloop()
