from tkinter import Tk, mainloop, OptionMenu, Label, StringVar, Entry, Button, Spinbox, IntVar, messagebox
import sys

class Gui:
    def __init__(self):
        ventana = Tk()
        fondo = "#8A2BE2"
        ventana.title("Pedidos")
        ventana.config(bg=fondo)
        ventana.resizable(0,0)
        ventana.geometry("450x300")
        self.ventana.iconbitmap("imagenes/empleado.ico")

        self.titulo = Label(ventana, text="Tomar pedidos", font=("Calisto MT", 20), bg=fondo, fg="white")

        self.menu = StringVar()
        cantidad = IntVar()

        self.etiqueta1 = Label(ventana, text="Nombre(s): ", bg=fondo, fg="white")
        self.etiqueta2 = Label(ventana, text="Dirección: ", bg=fondo, fg="white")
        self.etiqueta3 = Label(ventana, text="Menu: ", bg=fondo, fg="white")
        self.etiqueta4 = Label(ventana, text="Cantidad: ", bg=fondo, fg="white")

        self.entrada_nombre = Entry(ventana)
        self.entrada_direcc = Entry(ventana)

        self.boton = Button(ventana, text="Agregar", width=30, cursor="hand2", command=self.datos)

        self.lista = ["Milanga","Empanadas","Pizza","Asado","Hamburguesa Veggie","Milanesas de soja","Ensalada XL","Fideos"]

        self.opciones = OptionMenu(ventana, self.menu, *self.lista)
        self.opciones.configure(width=40,
                                activebackground="gray", 
                                bd=0, cursor="hand2")
        self.menu.set("Seleccione un menú...")
        self.spin_cantidad = Spinbox(ventana, textvariable=cantidad,
                                 from_=1, to=50, increment=1)

        self.titulo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        self.boton.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.etiqueta1.grid(row=1, column=0, padx=10, pady=10)
        self.etiqueta2.grid(row=2, column=0, padx=10, pady=10)
        self.etiqueta3.grid(row=3, column=0, padx=10, pady=10)
        self.etiqueta4.grid(row=4, column=0, padx=10, pady=10)

        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.entrada_direcc.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.opciones.grid(row=3, column=1, padx=10, pady=10)

        self.spin_cantidad.grid(row=4, column=1, padx=10, pady=10, sticky="w")


        center_window(ventana)
        mainloop()

    def datos(self):
        nombre = self.entrada_nombre.get()
        direccion = self.entrada_direcc.get()
        menu = self.menu.get()


        messagebox.showinfo("Registro", "Su pedido fue agregado a la lista de espera.")
        sys.exit()


def center_window(window):
        window.update_idletasks()
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2*frm_width
        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth()//2 - win_width//2
        y = window.winfo_screenheight()//2 - win_height//2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.deiconify()





Gui()









