# from tkinter import *
# window = Tk()

# window.configure(background='red')
# window.geometry("1000x500")

# label = Label(window, text="hueqwhrqr")
# label.pack()

# # window.configure(background='white')
# # window.geometry("1000x500")

# # label = Label(window, text ="me")
# # label.pack()
# window.mainloop()

from tkinter import *
def label(a,b,text):
    window = Tk()
    window.title("hello")
    window.geometry('300x300+'+str(a+'+'+str(b)))
    label=Label(window,text=text)
    label.pack()
    window.mainloop()

for i in range(1000):
    label(300,300,'ur ugly fat computer got infected by virus')