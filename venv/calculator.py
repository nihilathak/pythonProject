"""
def validate(self, action, index, value_if_allowed,
           prior_value, text, validation_type, trigger_type, widget_name):
  if value_if_allowed:
         try:
            float(value_if_allowed)
            return True
        except ValueError:
                return False
        else:
            return False
"""

from tkinter import *
#import tkinter as tk

def math_add(var1, var2):
    return var1 + var2
    #print("result:" + var3)

def math_sub(var1, var2):
    return var1 + var2
    #print("result:" + var3)

def math_mult(var1, var2):
    return var1 * var2

def math_div(var1, var2):
    return var1 / var2


def calc_gui():
    def math_add():
        add = int(entry1.get()) + int(entry2.get())
        add_result = Label(frame3, text="Result: " + str(add)).grid(row=5, column=0)

    def math_sub():
        sub = int(entry1.get()) - int(entry2.get())
        sub_result = Label(frame3, text="Result: " + str(sub)).grid(row=5, column=0)

    def math_mult():
        mult = int(entry1.get()) * int(entry2.get())
        mult_result = Label(frame3, text="Result: " + str(mult)).grid(row=5, column=0)

    def math_div():
        div = int(entry1.get()) / int(entry2.get())
        div_result = Label(frame3, text="Result: " + str(div)).grid(row=5, column=0)

    #Setup GUI Object with label and size
    window = Tk()
    window.title("Calculator")
    window.geometry("250x300")
    frame1 = LabelFrame(window, text="Enter your numbers below: ", padx=15, pady=5)
    frame1.pack(padx=5, pady=5)
    #frame1.pack_propagate(False)
    frame2 = LabelFrame(window, text="Select your Operator:", padx=10, pady=10)
    frame2.pack(padx=5, pady=5)
    #frame2.pack_propagate(False)
    frame3 = LabelFrame(window, text="Result: ", padx=10, pady=10)
    frame3.pack(padx=5, pady=5)



    #Setup Labels for entry fields and sections:
    #tk.Label(frame1, text="  Enter Your Numbers Here:").grid(row=0, column=0)

    #tk.Label(frame1, text="Select Your Operator:     ").grid(row=3, column=0)
    entry1 = Entry(frame1, borderwidth=2)
    entry1.grid(row=1, column=0, pady=6)
    entry2 = Entry(frame1, borderwidth=2)
    entry2.grid(row=2, column=0, pady=6)

    add_button = Button(frame2, text="+", width=3, height=1, command=math_add).grid(row=4, column=0)
    sub_button = Button(frame2, text="-", width=3, height=1, command=math_sub).grid(row=4, column=1)
    mul_button = Button(frame2, text="X", width=3, height=1, command=math_mult).grid(row=4, column=2)
    div_button = Button(frame2, text="/", width=3, height=1, command=math_div).grid(row=4, column=3)





    window.mainloop()


calc_gui()

