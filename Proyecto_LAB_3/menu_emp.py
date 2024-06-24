from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class Empleado:
    def __init__(self):
        self.empleados = tk.Tk()
        fondo = "#F0FFFF"
        self.empleados.title("Empleados")
        self.empleados.config(bg=fondo)
        self.empleados.resizable(0, 0)
        self.empleados.geometry("450x400")
        self.empleados.iconbitmap("imagenes/empleado.ico")

        # FRAME SUP
        self.frame_superior = tk.Frame(self.empleados, bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)

        # FRAME INF
        self.frame_inferior = tk.Frame(self.empleados, bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)

        # BOTONES ARRIBA
        #btn 1
        self.img = Image.open("Paquetes_de_iconos/comanda2.png")
        self.img = self.img.resize((100,100))
        icono = ImageTk.PhotoImage(self.img)

        btn_pedido = tk.Button(self.frame_superior, image=icono, text="Tomar pedido", bg=fondo, borderwidth=3, relief='solid', command=self.pedidos)
        btn_pedido.grid(row=1, column=1, padx=50, pady=30)

        #btn 2
        self.img2 = Image.open("Paquetes_de_iconos\cocinero.png")
        self.img2 = self.img2.resize((100,100))
        icono2 = ImageTk.PhotoImage(self.img2)

        btn_comanda = Button(self.frame_superior, image=icono2, text="Tomar pedido", relief='solid', borderwidth=3, bg=fondo)
        btn_comanda.grid(row=1, column=2, padx=80, pady=30)

        #btn 3
        self.img3 = Image.open("Paquetes_de_iconos\delivery.png")
        self.img3 = self.img3.resize((100,100))
        icono3 = ImageTk.PhotoImage(self.img3)

        btn_comanda = Button(self.frame_inferior, image=icono3, text="Tomar pedido", relief='solid', borderwidth=3, bg=fondo)
        btn_comanda.grid(row=1, column=1, padx=50, pady=30)

        #btn atras
        self.img4 = Image.open("Paquetes_de_iconos\hacia-atras.png")
        self.img4 = self.img4.resize((100,100))
        icono4 = ImageTk.PhotoImage(self.img4)

        btn_comanda = Button(self.frame_inferior, image=icono4, text="Tomar pedido", relief='solid', borderwidth=3, bg=fondo)
        btn_comanda.grid(row=1, column=2, padx=80, pady=30)



        #LABEL
        #label 1
        self.label1 = Label(self.frame_superior, text="Tomar pedido", font=('Helvetica', 12, 'bold'), bg= fondo)
        self.label1.grid(row=1, column=1, sticky= "s")

        #label 2
        self.label2 = Label(self.frame_superior, text="Mandar comanda", font=('Helvetica', 12, 'bold'), bg= fondo)
        self.label2.grid(row=1, column=2, sticky= "s")

        #label 3
        self.label3 = Label(self.frame_inferior, text="Enviar pedido", font=('Helvetica', 12, 'bold'), bg= fondo)
        self.label3.grid(row=1, column=1, sticky= "s")

        #label atras
        self.label4 = Label(self.frame_inferior, text="Atrás", font=('Helvetica', 12, 'bold'), bg= fondo)
        self.label4.grid(row=1, column=2, sticky= "s")




        self.center_window(self.empleados)
        self.empleados.mainloop()


    #FUNCION PEDIDOS
    def pedidos(self):
        self.ventana = tk.Toplevel(self.empleados)
        fondo = "#8A2BE2"
        self.ventana.title("Pedidos")
        self.ventana.config(bg=fondo)
        self.ventana.resizable(0, 0)
        self.ventana.geometry("450x300")
        self.ventana.iconbitmap("imagenes/hacer-un-pedido.ico")

        self.ventana.transient(self.empleados)
        self.ventana.grab_set()

        titulo = tk.Label(self.ventana, text="Tomar pedidos", font=("Calisto MT", 20), bg=fondo, fg="white")
        titulo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        self.menu = tk.StringVar()
        cantidad = tk.IntVar()

        etiquetas = ["Nombre(s): ", "Dirección: ", "Menu: ", "Cantidad: "]
        for i, texto in enumerate(etiquetas, start=1):
            tk.Label(self.ventana, text=texto, bg=fondo, fg="white").grid(row=i, column=0, padx=10, pady=10)

        self.entrada_nombre = tk.Entry(self.ventana)
        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.entrada_direcc = tk.Entry(self.ventana)
        self.entrada_direcc.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        lista = ["Milanga", "Empanadas", "Pizza", "Asado", "Hamburguesa Veggie", "Milanesas de soja", "Ensalada XL", "Fideos"]
        self.menu.set("Seleccione un menu....")
        opciones = tk.OptionMenu(self.ventana, self.menu, *lista)
        opciones.config(width=40, activebackground="gray", bd=0, cursor="hand2")
        opciones.grid(row=3, column=1, padx=10, pady=10)

        spin_cantidad = tk.Spinbox(self.ventana, textvariable=cantidad, from_=1, to=50, increment=1)
        spin_cantidad.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        boton = tk.Button(self.ventana, text="Agregar", width=30, cursor="hand2", command=self.datos)
        boton.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.center_window(self.ventana)



    def datos(self):
        nombre = self.entrada_nombre.get()
        direccion = self.entrada_direcc.get()
        menu = self.menu.get()

        if nombre == '' or direccion == '':
            return messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        
        elif  nombre and direccion and menu != "Seleccione un menu....":
            messagebox.showinfo("Registro", "Su pedido fue agregado a la lista de espera.")
            self.ventana.destroy()



            

    def center_window(self, window):
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

if __name__ == "__main__":
    Empleado()
