from tkinter import *
from tkinter import font
import customtkinter


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
    
    entry = customtkinter.CTkEntry(root, textvariable=display, font=('size',32),corner_radius=50)
    entry.place_configure(x=23, y=20, width=353, height=52)

    num0 =customtkinter.CTkButton(root, text="0", command = lambda:press(0), font=('size',32),corner_radius=50)
    num0.place_configure( x = 23, y = 382, width=58, height=65)

    num1 = customtkinter.CTkButton(root, text="1", command=lambda:press(1), font=('size',32),corner_radius=50)
    num1.place_configure( x = 23, y = 300, width=58, height=65)

    num2 = customtkinter.CTkButton(root, text="2", command=lambda:press(2), font=('size',32),corner_radius=50)
    num2.place_configure( x = 121, y = 300, width=58, height=65)

    num3 = customtkinter.CTkButton(root, text="3", command=lambda:press(3), font=('size',32),corner_radius=50)
    num3.place_configure( x = 220, y = 300, width=58, height=65)

    num4 = customtkinter.CTkButton(root, text="4", command=lambda:press(4), font=('size',32),corner_radius=50)
    num4.place_configure( x = 23, y = 216, width=58, height=65)

    num5 = customtkinter.CTkButton(root, text="5", command=lambda:press(5), font=('size',32),corner_radius=50)
    num5.place_configure( x = 121, y = 216, width=58, height=65)

    num6 = customtkinter.CTkButton(root, text="6", command=lambda:press(6), font=('size',32),corner_radius=50)
    num6.place_configure( x = 220, y = 216, width=58, height=65)

    num7 = customtkinter.CTkButton(root, text="7", command=lambda:press(7), font=('size',32),corner_radius=50)
    num7.place_configure( x = 23, y = 132, width=58, height=65)

    num8 = customtkinter.CTkButton(root, text="8", command=lambda:press(8), font=('size',32),corner_radius=50)
    num8.place_configure( x = 121, y = 132, width=58, height=65)

    num9 = customtkinter.CTkButton(root, text="9", command=lambda:press(9), font=('size',32),corner_radius=50)
    num9.place_configure( x = 220, y = 132, width=58, height=65)

    numadd = customtkinter.CTkButton(root, text="+", command=lambda: press('+'), font=('size',32),corner_radius=50)
    numadd.place_configure( x = 318, y = 132, width=58, height=65)

    numsub = customtkinter.CTkButton(root, text="-", command=lambda: press('-'), font=('size',32),corner_radius=50)
    numsub.place_configure( x = 318, y = 216, width=58, height=65)

    nummul = customtkinter.CTkButton(root, text="*", command=lambda: press('*'), font=('size',32),corner_radius=50)
    nummul.place_configure( x = 318, y = 300, width=58, height=65)

    numdiv = customtkinter.CTkButton(root, text="/", command=lambda: press('/'), font=('size',32),corner_radius=50)
    numdiv.place_configure( x = 318, y = 384, width=58, height=65)

    numequip = customtkinter.CTkButton(root, text="=", command=equal, font=('size',32),corner_radius=50)
    numequip.place_configure( x = 121, y = 384, width=157, height=63)

    root.mainloop()

