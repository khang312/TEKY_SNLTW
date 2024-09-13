import tkinter
from tkinter import messagebox
from tkinter import ttk

def login():
    ten = name.get()
    ngaysinh = date.get()
    country = quoc_tich.get()

window = tkinter.Tk()
window.title('Survey')
btn = tkinter.Button(window, command= login, text = 'LOGIN')
name = tkinter.Entry(window)
date = tkinter.Entry(window)
quoc_tich = ttk.Combobox(window)
quoc_tich['value'] = ('Vietnam, China, Thailand')
name1 = tkinter.Label(window, text= 'Ho va Ten')
date1 = tkinter.Label(window, text= 'Ngay Sinh')
quoc_tich1= tkinter.Label(window, text= 'Quoc Tich')

name.place(x= 150, y= 50)
date.place(x=150,y=100)

window.mainloop()