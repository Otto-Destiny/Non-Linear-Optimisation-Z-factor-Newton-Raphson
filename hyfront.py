from tkinter import *
from math import exp as e
import hyback
def calculate_command():
    t = 1 / float(e2.get())
    p = float(e1.get())
    yi = 0.001
    y = hyback.newton_raphson(yi, p, t)
    # z = compressibility_func(y,p,t)
    z = (0.06125 * p * t * e(-1.2 * (1 - t) ** 2)) / y
    e3.delete(0, END)
    e3.insert(END, "{:.3f}".format(y))
    e4.delete(0, END)
    e4.insert(END, "{:.3f}".format(z))


window = Tk()
window.geometry("500x200")
window.title("Cypher Z-factor")
window.iconbitmap("cyphercrescent.ico")

l1 = Label(window, text="This little app calculates the Z factor based on Hall Yarborough's method")
l1.grid(row=0, column=0, columnspan=6)

l2 = Label(window, text=" Pseudo-reduced Pressure")
l2.grid(row=1, column=0)

pressureentry = StringVar()
e1 = Entry(window, textvariable=pressureentry)
e1.grid(row=1, column=1)

l4 = Label(window, text="Pseudo-reduced Temperature")
l4.grid(row=2, column=0)

tempentry = StringVar()
e2 = Entry(window, textvariable=tempentry)
e2.grid(row=2, column=1)

l5 = Label(window, text="y value")
l5.grid(row=1, column=2)
y_value = StringVar()
e3 = Entry(window, textvariable=y_value)
e3.grid(row=1, column=3)

l6 = Label(window, text="Z Factor")
l6.grid(row=2, column=2)
Zfactor = StringVar()
e4 = Entry(window, textvariable=Zfactor)
e4.grid(row=2, column=3, padx=4, pady=15)

b1 = Button(window, text='Calculate', width=12, height=4, command=calculate_command)
b1.grid(row=4, column=1)
b2 = Button(window, text='Exit', width=12, height=4, command=window.destroy)
b2.grid(row=4, column=2)

window.mainloop()
