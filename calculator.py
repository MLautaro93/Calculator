# Import library
import tkinter as tk
from tkinter import ttk

# Create window
root = tk.Tk()
root.resizable = (False, False)
root.title('Calculator')

# ----------------------------------------Functions--------------------------------------------

def write(x):
    display.insert(tk.END, x)

def backspace():
    length = len(display.get())
    display.delete(length - 1)


def clear():
    display.delete(0, tk.END)

def equal(*args):
    try:
        result = eval(display.get())
        if result == int(result):
            result = int(result)
        display.delete(0, tk.END)
        display.insert(tk.END, result) 
    except:
        tk.messagebox.showinfo('Error', 'Syntax error.') 

# ----------------------------------------UI Design--------------------------------------------

# Entry
display = tk.Entry(justify = 'right')
display.grid(row = 0, columnspan = 4, sticky = 'WE')

# Buttons
class input_button(ttk.Button):
    def __init__(self, character):
        super().__init__(text = character, command = lambda: write(character))

input_button('0').grid(row = 5, column = 0)
input_button('1').grid(row = 4, column = 0)
input_button('2').grid(row = 4, column = 1)
input_button('3').grid(row = 4, column = 2)
input_button('4').grid(row = 3, column = 0)
input_button('5').grid(row = 3, column = 1)
input_button('6').grid(row = 3, column = 2)
input_button('7').grid(row = 2, column = 0)
input_button('8').grid(row = 2, column = 1)
input_button('9').grid(row = 2, column = 2)
input_button('.').grid(row = 5, column = 1)
input_button('+').grid(row = 5, column = 3)
input_button('-').grid(row = 4, column = 3)
input_button('*').grid(row = 3, column = 3)
input_button('/').grid(row = 2, column = 3)
input_button('(').grid(row = 1, column = 0)
input_button(')').grid(row = 1, column = 1)

backspace_button = ttk.Button(text = '←', command = backspace).grid(row = 1, column = 2)
clear_button = ttk.Button(text = 'AC', command = clear).grid(row = 1, column = 3)
equal_button = ttk.Button(text = '=', command = equal).grid(row = 5, column = 2)
root.bind('<Return>', equal)

root.mainloop()