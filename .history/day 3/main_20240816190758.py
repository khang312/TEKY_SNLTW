import tkinter
window = tkinter.Tk()

window.title('helloworld')
window.configure(background='blue')
window.geometry('500x250')

label = tkinter.Label(window, text ="me")
label.pack()
window.mainloop()