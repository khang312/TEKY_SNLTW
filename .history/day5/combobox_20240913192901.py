import tkinter
from tkinter import messagebox
from tkinter import ttk

def login():
    Ho_va_ten = get()
    Ngay_sinh = get()
    Quoc_tich = get()

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

name.place(x= 50, y= 50)


window.mainloop()