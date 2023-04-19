#GUI Calculator
#button, entry

from tkinter import *
#from tkinter.ttk import *

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equalpress():
    global expression

    total = str(eval(expression))

    equation.set(total)

    expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":

    root = Tk()

    root.title("Calculator")
    root.geometry('300x285')

    frame =  Frame(root)
    frame.pack()

    equation = StringVar()

    label1 = Label(frame, text = "")
    label1.grid(row = 0, columnspan = 3)
    button1 = Button(frame, text = "    1   ", command = lambda: press(1))
    #button1.pack()
    button2 = Button(frame, text = "    2   ", command = lambda: press(2))
    #button2.pack()
    button3 = Button(frame, text = "    3   ", command = lambda: press(3))
    #button3.pack()
    button4 = Button(frame, text = "    4   ", command = lambda: press(4))
    #button4.pack()
    button5 = Button(frame, text = "    5   ", command = lambda: press(5))
    #button5.pack()
    button6 = Button(frame, text = "    6   ", command = lambda: press(6))
    #button6.pack()
    button7 = Button(frame, text = "    7   ", command = lambda: press(7))
    #button7.pack()
    button8 = Button(frame, text = "    8   ", command = lambda: press(8))
    #button8.pack()
    button9 = Button(frame, text = "    9   ", command = lambda: press(9))
    #button9.pack()
    button0 = Button(frame, text = "    0   ", command = lambda: press(0))
    #button0.pack()
    button10 = Button(frame, text = "   +   ", command = lambda: press("+"))
    #button1.pack()
    button11 = Button(frame, text = "   -   ", command = lambda: press("-"))
    #button1.pack()
    button12 = Button(frame, text = "   *   ", command = lambda: press("*"))
    #button1.pack()
    button13 = Button(frame, text = "   /   ", command = lambda: press("/"))
    #button1.pack()
    button14 = Button(frame, text = "   =   ", command = equalpress)
    #button1.pack()
    button15 = Button(frame, text = "   C   ", command = clear)
    #button1.pack()

    button1.grid(row = 1,  column = 0,    pady = 5)
    button2.grid(row = 1,  column = 1,    pady = 5)
    button3.grid(row = 1,  column = 2,    pady = 5)
    button4.grid(row = 2,  column = 0,    pady = 5)
    button5.grid(row = 2,  column = 1,    pady = 5)
    button6.grid(row = 2,  column = 2,    pady = 5)
    button7.grid(row = 3,  column = 0,    pady = 5)
    button8.grid(row = 3,  column = 1,    pady = 5)
    button9.grid(row = 3,  column = 2,    pady = 5)
    button0.grid(row = 4,  column = 1,    pady = 5)
    button10.grid(row = 6,  column = 0,    pady = 5)
    button14.grid(row = 6,  column = 1,    pady = 5)
    button11.grid(row = 6,  column = 2,    pady = 5)
    button12.grid(row = 7,  column = 0,    pady = 5)
    button15.grid(row = 7,  column = 1,    pady = 5)
    button13.grid(row = 7,  column = 2,    pady = 5)

    label = Label(frame, text = "input:           ")
    label.grid(row = 5, column = 0, pady = 6)
    entry = Entry(frame, textvariable = equation)
    entry.grid(row = 5, column = 1, pady = 6)

    root.mainloop()