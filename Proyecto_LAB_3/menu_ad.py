from tkinter import *
from PIL import Image, ImageTk

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

menu_ad()



