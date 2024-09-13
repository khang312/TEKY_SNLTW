import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
def login():
    ten = name.get()
    ngaysinh = date.get()
    country = quoc_tich.get()
    if ten and ngaysinh and country:
        messagebox.showinfo('Login successfull', 'Login successfull')
    if country == 'Thailand':
        image_label=tkinter.Label(window, image= image_thai)
        
    elif country == 'Vietnam':
        image_label=tkinter.Label(window, image= image_vn)
    else:
        image_label=tkinter.Label(window, image= image_china)
    image_label.place(250, 200)
window = tkinter.Tk()
window.title('Survey')
btn = tkinter.Button(window, command= login, text = 'LOGIN')
name = tkinter.Entry(window)
date = tkinter.Entry(window)
quoc_tich = ttk.Combobox(window)
quoc_tich['value'] = ('Vietnam',  'China',  'Thailand')
name1 = tkinter.Label(window, text= 'Ho va Ten')
date1 = tkinter.Label(window, text= 'Ngay Sinh')
quoc_tich1= tkinter.Label(window, text= 'Quoc Tich')
quoc_tich.current(0)
image_china = PhotoImage(file=r"/Users/mac/Desktop/TEKY_SNLTW/day5/china.png")
image_vn = PhotoImage(file=r'/Users/mac/Desktop/TEKY_SNLTW/day5/name.png')
image_thai = PhotoImage(file=r'/Users/mac/Desktop/TEKY_SNLTW/day5/thai.png')




name.place(x=150,y=50)
name1.place(x=50,y=50)
date.place(x=150,y=100)
date1.place(x=50,y=100)
quoc_tich.place(x=150,y=150)
quoc_tich1.place(x=50,y=150)
btn.place(x=150,y=200)
window.mainloop()