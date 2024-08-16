import tkinter
window = tkinter.Tk()

window.title('hello world')
window.configure(background='blue')
window.geometry("1000x500")

label = tkinter.Label(window, text ="me")
label.pack()
window.mainloop()