import tkinter
import os
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Menu, Toplevel
def quit():
    window.destroy()

def login():
    ten = name.get()
    ngaysinh = date.get()
    country = quoc_tich.get()
    gender = gender_var.get()
    if ten and ngaysinh and country and gender!='none':
        f = open(r"/Users/mac/Desktop/TEKY_SNLTW/day7/survery_info.txt", "a")
        f.writelines('ten, ngaysinh, country,gender') #This line of code is wrong
        f.close()
        messagebox.showinfo('Login successfull', 'Login successfull')
        
        
        
        if country == 'Thailand':
            image_label=tkinter.Label(window, image= image_thai)
        
        elif country == 'Vietnam':
            image_label=tkinter.Label(window, image= image_vn)
        else:
            image_label=tkinter.Label(window, image= image_china)
        image_label.place(x=300,y=300)
    else:
        messagebox.showerror('bruh','complete the survery please' )
def delete_user_info():
    name.delete(0, tkinter.END)
    date.delete(0, tkinter.END)
    quoc_tich.set('')
    gender_var.set(None)

def close_widget():   
    name.place_forget()

def new_window():
    new_window = Toplevel(window)
    new_window.title('Survey')
    new_window.geometry('700x500')

    btn_new = tkinter.Button(new_window, command= login, text = 'register')
    btn2_new = tkinter.Button(new_window, command= quit, text = 'Quit')

    name_new = tkinter.Entry(new_window)
    date_new = tkinter.Entry(new_window)

    quoc_tich = ttk.Combobox(new_window)
    quoc_tich['value'] = ('Vietnam',  'China',  'Thailand')
    name1_new = tkinter.Label(new_window, text= 'Ho va Ten')
    date1_new = tkinter.Label(new_window, text= 'Ngay Sinh')
    quoc_tich1_new= tkinter.Label(new_window, text= 'Quoc Tich')
    quoc_tich.current(0)


    gender_var = tkinter.StringVar(value = 'none')
    radio_female_new =tkinter.Radiobutton(new_window, text = 'nữ', variable= gender_var, value= 'female')
    radio_male_new =tkinter.Radiobutton(new_window, text = 'nam', variable= gender_var, value= 'male')

    radio_male_new.place(x=500, y=50)
    radio_female_new.place(x=500,y=100)
    name_new.place(x=150,y=50)
    name1_new.place(x=50,y=50)
    date_new.place(x=150,y=100)
    date1_new.place(x=50,y=100)
    quoc_tich.place(x=150,y=150)
    quoc_tich1_new.place(x=50,y=150)
    btn2_new.place(x=250,y=200)
    btn_new.place(x=150,y=200)

window = tkinter.Tk()
window.title('Survey')
window.geometry('700x500')

menubar = Menu(window)
window.config(menu=menubar)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = file)
file.add_command(label='new', command= new_window)
file.add_command(label='open')

tool = Menu(menubar, tearoff = 0 )
menubar.add_cascade(label='Edit', menu = tool)
tool.add_command(label='Delete', command=delete_user_info)
tool.add_command(label='Close', command=close_widget)

btn = tkinter.Button(window, command= login, text = 'register')
btn2 = tkinter.Button(window, command= quit, text = 'Quit')

name = tkinter.Entry(window)
date = tkinter.Entry(window)

quoc_tich = ttk.Combobox(window)
quoc_tich['value'] = ('Vietnam',  'China',  'Thailand')
name1 = tkinter.Label(window, text= 'Ho va Ten')
date1 = tkinter.Label(window, text= 'Ngay Sinh')
quoc_tich1= tkinter.Label(window, text= 'Quoc Tich')
quoc_tich.current(0)
image_china = PhotoImage(file=r"/Users/mac/Desktop/TEKY_SNLTW/day7/china.png")
image_vn = PhotoImage(file=r'/Users/mac/Desktop/TEKY_SNLTW/day7/name.png')
image_thai = PhotoImage(file=r'/Users/mac/Desktop/TEKY_SNLTW/day7/thai.png')

gender_var = tkinter.StringVar(value = 'none')
radio_female =tkinter.Radiobutton(window, text = 'nữ', variable= gender_var, value= 'female')
radio_male =tkinter.Radiobutton(window, text = 'nam', variable= gender_var, value= 'male')

radio_male.place(x=500, y=50)
radio_female.place(x=500,y=100)
name.place(x=150,y=50)
name1.place(x=50,y=50)
date.place(x=150,y=100)
date1.place(x=50,y=100)
quoc_tich.place(x=150,y=150)
quoc_tich1.place(x=50,y=150)
btn2.place(x=250,y=200)
btn.place(x=150,y=200)

window.mainloop()

