import tkinter as tk
import urllib
import requests
import shutil




def setup_gui():
    window = tk.Tk(className=" -Hello Niggerino!-")
    window.geometry("300x100")
    tk.Label(window, text="  Image URL").grid(row=0)
    e1 = tk.Entry(window)
    e1.grid (row=0, column=1, pady=10)

    tk.Button(window, text='download')

    window.mainloop()

setup_gui()