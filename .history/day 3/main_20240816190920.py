from tkinter import *
window = Tk()

window.title('hello world')
window.configure(background='white')
window.geometry("1000x500")

label = Label(window, text ="me")
label.pack()
window.mainloop()