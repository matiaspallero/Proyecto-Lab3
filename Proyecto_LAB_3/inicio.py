from tkinter import Tk, Label, Button, Entry, Frame, messagebox, StringVar, IntVar, mainloop, OptionMenu, Spinbox, Menu, Frame
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

def limpiarPantalla():
    os.system("cls")


class Login():
    def __init__(self):
        self.loginn = Tk()
        self.loginn.title("Login")
        self.loginn.geometry("550x600")
        self.loginn.resizable(0,0)
        self.loginn.iconbitmap("imagenes/usuarioo.ico")

        fondo = "#87CEFA"

        #FRAMES
        #parte superior
        self.frame_superior = Frame(self.loginn)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)

        #parte inferior
        self.frame_inferior = Frame(self.loginn)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)
        
        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)



        #TITULO
        self.titulo = Label(self.frame_superior, text="Login",font=("Calisto MT", 36, "bold"), bg=fondo)
        self.titulo.pack(side="top", pady=20)



        #IMÁGENES
        self.img = Image.open("imagenes/usuario.png")
        self.img = self.img.resize((150,165))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image= self.render, bg= fondo)
        self.fondo.pack(expand=True, fill="both", side="top")


        #PARTE DE DATOS
        self.label_user = Label(self.frame_inferior, text="Usuario:", 
                                font=("Arial", 18), 
                                bg=fondo, 
                                fg="black")
        self.label_user.grid(row=0, column=0, padx=10, sticky="e")

        self.entry_user = Entry(self.frame_inferior, 
                                bd=0, 
                                width=14, 
                                font=("Arial", 18))
        self.entry_user.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        self.label_pass = Label(self.frame_inferior, text="Contraseña:", 
                                font=("Arial", 18), 
                                bg=fondo, 
                                fg="black")
        self.label_pass.grid(row=1, column=0, padx=10, sticky="e")

        self.entry_pass = Entry(self.frame_inferior, 
                                bd=0, width=14, 
                                font=("Arial", 18),
                                show="*")
        self.entry_pass.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")

        #Boton
        self.boton_ingresar = Button(self.frame_inferior, text="Ingresar",
                                     width=16,
                                     font=("Arial", 12),
                                     command = self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=35)

        center_window(self.loginn)
        mainloop()


    def entrar(self):
        login = self.entry_user.get()
        clave = self.entry_pass.get()

        valid_pass = ['12345']

        login_emp = ['admin','carlos','jose','lucas','jorge']
        clave_emp = ['123',"111","222","333"]

        if login in login_emp[0:1]:
                if clave in valid_pass:
                        messagebox.showinfo("Acceso correcto","Bienvenido Jefe.")
                        self.loginn.destroy()
                        menu_ad()
                        
                else:
                        messagebox.showinfo("Acceso Incorrecto","Intente nuevamente.")
                

        if login in login_emp[1:]:
                if clave in clave_emp:
                        messagebox.showinfo("Acceso correcto","Bienvenido Empleado.")
                        self.loginn.destroy()
                        Empleado()

                else:
                        messagebox.showinfo("Acceso Incorrecto","Intente nuevamente.")


class Gui:
    def __init__(self):
        self.ventana = Tk()
        fondo = "#8A2BE2"
        self.ventana.title("Pedidos")
        self.ventana.config(bg=fondo)
        self.ventana.resizable(0,0)
        self.ventana.geometry("450x300")

        self.titulo = Label(self.ventana, text="Tomar pedidos", font=("Calisto MT", 20), bg=fondo, fg="white")

        self.menu = StringVar()
        cantidad = IntVar()

        self.etiqueta1 = Label(self.ventana, text="Nombre(s): ", bg=fondo, fg="white")
        self.etiqueta2 = Label(self.ventana, text="Apellido(s): ", bg=fondo, fg="white")
        self.etiqueta3 = Label(self.ventana, text="Menu: ", bg=fondo, fg="white")
        self.etiqueta4 = Label(self.ventana, text="Cantidad: ", bg=fondo, fg="white")

        self.entrada_nombre = Entry(self.ventana)
        self.entrada_apellido = Entry(self.ventana)

        self.boton = Button(self.ventana, text="Agregar", width=30, cursor="hand2", command=self.datos)

        self.lista = ["Milanga","Empanadas","Pizza","Asado","Hamburguesa Veggie","Milanesas de soja","Ensalada XL","Fideos"]

        self.opciones = OptionMenu(self.ventana, self.menu, *self.lista)
        self.opciones.configure(width=40,
                                activebackground="gray", 
                                bd=0, cursor="hand2")
        self.menu.set("Seleccione un menú...")
        self.spin_cantidad = Spinbox(self.ventana, textvariable=cantidad,
                                 from_=1, to=50, increment=1)

        self.titulo.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        self.boton.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.etiqueta1.grid(row=1, column=0, padx=10, pady=10)
        self.etiqueta2.grid(row=2, column=0, padx=10, pady=10)
        self.etiqueta3.grid(row=3, column=0, padx=10, pady=10)
        self.etiqueta4.grid(row=4, column=0, padx=10, pady=10)

        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.entrada_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.opciones.grid(row=3, column=1, padx=10, pady=10)

        self.spin_cantidad.grid(row=4, column=1, padx=10, pady=10, sticky="w")


        center_window(self.ventana)
        mainloop()

    def datos(self):
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()
        menu = self.menu.get()


        messagebox.showinfo("Registro", "Su pedido fue agregado a la lista de espera.")



class menu_ad:
    def __init__(self):
        self.menu_adm = Tk()
        self.menu_adm.title("Administración")
        self.menu_adm.geometry("900x700")
        self.menu_adm.resizable(0,0)
        self.menu_adm.iconbitmap("imagenes/administracion.ico")
        

        fondo = "#F0FFFF"

        self.menu1 = Menu(self.menu_adm)
        self.menu_adm.config(menu = self.menu1)        
        
        #Barra
        Empleados = Menu(self.menu1, tearoff=0)
        Empleados.add_command(label = "Ver lista de empleados")
        Empleados.add_command(label = "Agregar empleado")
        Empleados.add_command(label = "Eliminar empleado")
        Empleados.add_command(label = "Cambiar contraseña")

        Platos = Menu(self.menu1, tearoff=0)
        Platos.add_command(label = "Ver lista de platos")
        Platos.add_command(label = "Editar platos")
        Platos.add_command(label = "Eliminar platos")
        
        Ganancias = Menu(self.menu1, tearoff=0)
        Ganancias.add_command(label = "Costo fijo")
        Ganancias.add_command(label = "Ver ganancias mensuales")

        
        Ayuda = Menu(self.menu1, tearoff=0)
        Ayuda.add_command(label = "Contáctame")
        Ayuda.add_command(label = "Notificar un error")
        Ayuda.add_separator()
        Ayuda.add_command(label = "Salir",command = exit)
        
        
        self.menu1.add_cascade(label = "Empleados", menu = Empleados)
        self.menu1.add_cascade(label = "Platos", menu = Platos)
        self.menu1.add_cascade(label = "Ganancias", menu = Ganancias)
        self.menu1.add_cascade(label = "Ayuda", menu = Ayuda)

        #Frame
        self.frame = Frame(self.menu_adm)
        self.frame.configure(bg = fondo)
        self.frame.pack(fill = "both", expand = True)

        #Botones
        #btn 1
        self.img = Image.open("Paquetes_de_iconos\esqueleto-clave-izquierda-derecha.png")
        self.img = self.img.resize((50,50))
        icono1 = ImageTk.PhotoImage(self.img)
        
        self.boton1 = Button(self.frame, image= icono1, width=70, height=70, cursor= "hand2", bg=fondo)
        self.boton1.grid(row=1 , column=1, columnspan= 3, padx= 40, pady= 40)

        #btn 2
        self.img2 = Image.open("Paquetes_de_iconos/cambio-empleado.png")
        self.img2 = self.img2.resize((50,50))
        icono2 = ImageTk.PhotoImage(self.img2)
        
        self.boton2 = Button(self.frame, image= icono2, width=70, height=70, cursor= "hand2", bg=fondo)
        self.boton2.grid(row=2 , column=1, columnspan= 3, padx= 40, pady= 40)
        
        #btn 3
        self.img3 = Image.open("Paquetes_de_iconos/restaurante.png")
        self.img3 = self.img3.resize((50,50))
        icono3 = ImageTk.PhotoImage(self.img3)
        
        self.boton3 = Button(self.frame, image= icono3, width=70, height=70, cursor= "hand2", bg=fondo)
        self.boton3.grid(row=3 , column=1, columnspan= 3, padx= 40, pady= 40)

        #btn 4
        self.img4 = Image.open("Paquetes_de_iconos/grafico-histograma.png")
        self.img4 = self.img4.resize((50,50))
        icono4 = ImageTk.PhotoImage(self.img4)
        
        self.boton4 = Button(self.frame, image= icono4, width=70, height=70, cursor= "hand2", bg=fondo)
        self.boton4.grid(row=4 , column=1, columnspan= 3, padx= 40, pady= 40)

        #btn salida
        self.img5 = Image.open("Paquetes_de_iconos/atras (1).png")
        self.img5 = self.img5.resize((50,50))
        icono5 = ImageTk.PhotoImage(self.img5)

        self.btn_salida = Button(self.frame, image= icono5, width=60, height=60, cursor= "hand2", bg=fondo, command = self.menu_adm.destroy)
        self.btn_salida.grid(row=1 , column=10, columnspan= 16, padx= 190, pady= 40)
        
        #LABELS
        #Label 1
        self.label1 = Label(self.frame, text="Cambiar contraseñas", font=("Arial", 25, "bold"), bg= fondo)
        self.label1.grid(row=1, column=4, columnspan= 3,padx=40)

        #Label 2
        self.label2 = Label(self.frame, text="Administrar empleados", font=("Arial", 25, "bold"), bg= fondo)
        self.label2.grid(row=2, column=5, columnspan= 3,padx=40)

        #Label 3
        self.label3 = Label(self.frame, text="Administrar platos", font=("Arial", 25, "bold"), bg= fondo)
        self.label3.grid(row=3, column=5, columnspan= 3,padx=40)

        #Label 4
        self.label4 = Label(self.frame, text="Administrar ganancias", font=("Arial", 25, "bold"), bg= fondo)
        self.label4.grid(row=4, column=5, columnspan= 3,padx=40)



        center_window(self.menu_adm)
        mainloop()



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

        btn_comanda = Button(self.frame_inferior, image=icono4, relief='solid', borderwidth=3, bg=fondo, command= self.empleados.destroy)
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




        center_window(self.empleados)
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

        center_window(self.ventana)



    def datos(self):
        nombre = self.entrada_nombre.get()
        direccion = self.entrada_direcc.get()
        menu = self.menu.get()

        if nombre == '' or direccion == '':
            return messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        
        elif  nombre and direccion and menu != "Seleccione un menu....":
            messagebox.showinfo("Registro", "Su pedido fue agregado a la lista de espera.")
            self.ventana.destroy()






def volver(self):
        self.menu_ad.destroy()
        menu_ad()


def regresar(self):
        self.loginn.destroy()
        Login()



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


Login()