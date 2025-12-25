from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter

expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)
    
def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

# def clear():
#     global expr
#     expr = ""
#     display.set("")


if __name__ == "__main__":
    
    root = Tk()
    root.title("Calculator")
    root.geometry("400x500")
    
    
    display = StringVar()
    
    entry = Entry(root, textvariable=display, font=font.Font(size=32))
    entry.place(x=23, y=20, width=353, height=52)

    num0 =Button(root, text="0", command = lambda:press(0), font=font.Font(size=32))
    num0.place( x = 23, y = 382, width=58, height=65)

    num1 = Button(root, text="1", command=lambda:press(1), font=font.Font(size=32))
    num1.place( x = 23, y = 300, width=58, height=65)

    num2 = Button(root, text="2", command=lambda:press(2), font=font.Font(size=32))
    num2.place( x = 121, y = 300, width=58, height=65)

    num3 = Button(root, text="3", command=lambda:press(3), font=font.Font(size=32))
    num3.place( x = 220, y = 300, width=58, height=65)

    num4 = Button(root, text="4", command=lambda:press(4), font=font.Font(size=32))
    num4.place( x = 23, y = 216, width=58, height=65)

    num5 = Button(root, text="5", command=lambda:press(5), font=font.Font(size=32))
    num5.place( x = 121, y = 216, width=58, height=65)

    num6 = Button(root, text="6", command=lambda:press(6), font=font.Font(size=32))
    num6.place( x = 220, y = 216, width=58, height=65)

    num7 = Button(root, text="7", command=lambda:press(7), font=font.Font(size=32))
    num7.place( x = 23, y = 132, width=58, height=65)

    num8 = Button(root, text="8", command=lambda:press(8), font=font.Font(size=32))
    num8.place( x = 121, y = 132, width=58, height=65)

    num9 = Button(root, text="9", command=lambda:press(9), font=font.Font(size=32))
    num9.place( x = 220, y = 132, width=58, height=65)

    numadd = Button(root, text="+", command=lambda: press('+'), font=font.Font(size=32))
    numadd.place( x = 318, y = 132, width=58, height=65)

    numsub = Button(root, text="-", command=lambda: press('-'), font=font.Font(size=32))
    numsub.place( x = 318, y = 216, width=58, height=65)

    nummul = Button(root, text="*", command=lambda: press('*'), font=font.Font(size=32))
    nummul.place( x = 318, y = 300, width=58, height=65)

    numdiv = Button(root, text="/", command=lambda: press('/'), font=font.Font(size=32))
    numdiv.place( x = 318, y = 384, width=58, height=65)

    numequip = Button(root, text="=", command=equal, font=font.Font(size=32))
    numequip.place( x = 121, y = 384, width=157, height=63)

    root.mainloop()

