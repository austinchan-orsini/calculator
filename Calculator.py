from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""
    except TypeError:
        equation_label.set("type error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Calculator")
window.geometry("303x478")
window.resizable(False, False)

window.configure(bg='black')
equation_text = ""
equation_label = StringVar()



frame = Frame(window, bg='black')
frame.pack()


label = Label(frame, textvariable=equation_label, width = 12, height =2, font=('consolas',30), bg="black", fg="white")
label.grid(row=0, column=0, columnspan=4, sticky="news")

button1 = Button(frame, text=1, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25), command=lambda: button_press(1))
button1.grid(row=1, column=0)

button2 = Button(frame, text=2, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(2))
button2.grid(row=1, column=1)

button3 = Button(frame, text=3, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(3))
button3.grid(row=1, column=2)

button4 = Button(frame, text=4, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(4))
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(5))
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(6))
button6.grid(row=2, column=2)

button7 = Button(frame, text=7, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(7))
button7.grid(row=3, column=0)

button8 = Button(frame, text=8, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(8))
button8.grid(row=3, column=1)

button9 = Button(frame, text=9, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(9))
button9.grid(row=3, column=2)

button0 = Button(frame, text=0, width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press(0))
button0.grid(row=4, column=1)

plus = Button(frame, text='+', width = 3, height = 1, bg = 'dark orange', fg = 'white', font=("Helvetica", 25),command=lambda: button_press('+'))
plus.grid(row=4, column=3)

minus = Button(frame, text='–', width = 3, height = 1, bg = 'dark orange', fg = 'white', font=("Helvetica", 25),command=lambda: button_press('-'))
minus.grid(row=3, column=3)

multiply = Button(frame, text='×', width = 3, height = 1, bg = 'dark orange', fg = 'white', font=("Helvetica", 25),command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='÷', width = 3, height = 1, bg = 'dark orange', fg = 'white', font=("Helvetica", 25),command=lambda: button_press('/'))
divide.grid(row=1, column=3)

equal = Button(frame, text='=', width = 3, height = 1, bg = 'dark orange', fg = 'white', font=("Helvetica", 25),command=equals)
equal.grid(row=5, column=3)

decimal = Button(frame, text='.', width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25),command=lambda: button_press('.'))
decimal.grid(row=5, column=2)

clear_button = Button(frame, text='C', width = 3, height = 1, font=("Helvetica", 25), command=clear)
clear_button.grid(row=5, column=1)

right_parenthesis = Button(frame, text=')', width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25), command=lambda: button_press(')'))
right_parenthesis.grid(row=4, column=2)

left_parenthesis = Button(frame, text='(', width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25), command=lambda: button_press('('))
left_parenthesis.grid(row=4, column=0)

clear_button = Button(frame, text='C', width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25), command=clear)
clear_button.grid(row=5, column=1)

mod = Button(frame, text='Mod', width = 3, height = 1, bg = 'gray', fg = 'white', font=("Helvetica", 25), command=lambda: button_press('%'))
mod.grid(row=5, column=0)

window.mainloop()