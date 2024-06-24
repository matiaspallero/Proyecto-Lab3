from tkinter import Tk, Label, Button, Entry, Frame, messagebox, StringVar, IntVar, mainloop, OptionMenu, Spinbox, Menu
from PIL import Image, ImageTk
import os
import sys

class Comanda:
    def __init__(self):
        self.comandas = Tk()
        fondo = "#F0F8FF"
        self.comandas.title("Cocina")
        self.comandas.config(bg=fondo)
        self.comandas.resizable(0,0)
        self.comandas.geometry("700x500")
        self.comandas.iconbitmap("imagenes/frito.ico")






        center_window(self.comandas)
        mainloop()




def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()



Comanda()