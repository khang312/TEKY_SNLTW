# import tkinter
# import os
# from tkinter import messagebox
# from tkinter import ttk
# from tkinter import PhotoImage
# from tkinter import Menu
# def quit():
#     window.destroy()

# def login():
#     ten = name.get()
#     ngaysinh = date.get()
#     country = quoc_tich.get()
#     gender = gender_var.get()
#     if ten and ngaysinh and country and gender!='none':
#         f = open(r"/Users/mac/Documents/TEKY_SNLTW/day7/survery_info.txt", "a")
#         f.writelines('ten, ngaysinh, country,gender') #This line of code is wrong
#         f.close()
#         messagebox.showinfo('Login successfull', 'Login successfull')
        
        
        
#         if country == 'Thailand':
#             image_label=tkinter.Label(window, image= image_thai)
        
#         elif country == 'Vietnam':
#             image_label=tkinter.Label(window, image= image_vn)
#         else:
#             image_label=tkinter.Label(window, image= image_china)
#         image_label.place(x=300,y=300)
#     else:
#         messagebox.showerror('bruh','complete the survery please' )

# window = tkinter.Tk()
# window.title('Survey')
# window.geometry('700x500')

# menubar = Menu(window)
# window.config(menu=menubar)

# file = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label = 'File', menu = file)
# file.add_command(label='new')
# file.add_command(label='open')

# tool = Menu(menubar, tearoff = 0 )
# menubar.add_cascade(label='Edit', menu = tool)
# tool.add_command(label='Delete')
# tool.add_command(label='Close')

# btn = tkinter.Button(window, command= login, text = 'register')
# btn2 = tkinter.Button(window, command= quit, text = 'Quit')

# name = tkinter.Entry(window)
# date = tkinter.Entry(window)

# quoc_tich = ttk.Combobox(window)
# quoc_tich['value'] = ('Vietnam',  'China',  'Thailand')
# name1 = tkinter.Label(window, text= 'Ho va Ten')
# date1 = tkinter.Label(window, text= 'Ngay Sinh')
# quoc_tich1= tkinter.Label(window, text= 'Quoc Tich')
# quoc_tich.current(0)
# image_china = PhotoImage(file=r"/Users/mac/Documents/TEKY_SNLTW/day7/china.png")
# image_vn = PhotoImage(file=r'/Users/mac/Documents/TEKY_SNLTW/day7/name.png')
# image_thai = PhotoImage(file=r'/Users/mac/Documents/TEKY_SNLTW/day7/thai.png')

# gender_var = tkinter.StringVar(value = 'none')
# radio_female =tkinter.Radiobutton(window, text = 'nữ', variable= gender_var, value= 'female')
# radio_male =tkinter.Radiobutton(window, text = 'nam', variable= gender_var, value= 'male')

# radio_male.place(x=500, y=50)
# radio_female.place(x=500,y=100)
# name.place(x=150,y=50)
# name1.place(x=50,y=50)
# date.place(x=150,y=100)
# date1.place(x=50,y=100)
# quoc_tich.place(x=150,y=150)
# quoc_tich1.place(x=50,y=150)
# btn2.place(x=250,y=200)
# btn.place(x=150,y=200)

# window.mainloop()
import tkinter
import os
from tkinter import messagebox
from tkinter import Menu

def quit():
    window.destroy()

def login():
    ten = name.get()
    ngaysinh = date.get()
    country = quoc_tich.get()
    gender = gender_var.get()
    
    if ten and ngaysinh and country and gender != 'none':
        with open(r"/Users/mac/Documents/TEKY_SNLTW/day7/survery_info.txt", "a") as f:
            f.writelines(f'{ten}, {ngaysinh}, {country}, {gender}\n')  # Corrected this line
        
        messagebox.showinfo('Login successful', 'Login successful')
        
        if country == 'Thailand':
            image_label = tkinter.Label(window, image=image_thai)
        elif country == 'Vietnam':
            image_label = tkinter.Label(window, image=image_vn)
        else:
            image_label = tkinter.Label(window, image=image_china)
        
        image_label.place(x=300, y=300)
    else:
        messagebox.showerror('Error', 'Complete the survey please.')

def delete_user_info():
    # Clear the input fields
    name.delete(0, tkinter.END)
    date.delete(0, tkinter.END)
    quoc_tich.set('')  # Assuming quoc_tich is a StringVar
    gender_var.set('none')  # Assuming gender_var is a StringVar

    # Optionally delete the user data file
    if os.path.exists(r"/Users/mac/Documents/TEKY_SNLTW/day7/survery_info.txt"):
        os.remove(r"/Users/mac/Documents/TEKY_SNLTW/day7/survery_info.txt")
        messagebox.showinfo('Deleted', 'User information deleted successfully.')

window = tkinter.Tk()
window.title('Survey')
window.geometry('700x500')

menubar = Menu(window)
window.config(menu=menubar)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='new')
file.add_command(label='open')

tool = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=tool)
tool.add_command(label='Delete', command=delete_user_info)  # Added the delete command
tool.add_command(label='Close', command=quit)

btn = tkinter.Button(window, command=login, text='Register')
btn.pack()  # Add this button to the window
btn2 = tkinter.Button(window, command=quit, text='Quit')
btn2.pack()  # Add this button to the window

name = tkinter.Entry(window)
name.pack()  # Add this entry to the window
date = tkinter.Entry(window)
date.pack()  # Add this entry to the window

# Assuming you have defined quoc_tich and gender_var as StringVars
quoc_tich = tkinter.StringVar(window)
gender_var = tkinter.StringVar(window)
quoc_tich.set('')  # Default value
gender_var.set('none')  # Default value

# Don't forget to initialize your image variables
# image_thai = PhotoImage(file='path_to_thai_image')
# image_vn = PhotoImage(file='path_to_vietnam_image')
# image_china = PhotoImage(file='path_to_china_image')

window.mainloop()
