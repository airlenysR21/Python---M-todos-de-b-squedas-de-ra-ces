from tkinter import *
import tkinter as tk
from sympy import *
from math import *
import sympy as sp
import numpy as np
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox as MessageBox  
from setuptools import Command 

   
class tkinterApp(tk.Tk): 

    def __init__(self, *args, **kwargs):  
       
        tk.Tk.__init__(self, *args, **kwargs) 
 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        self.frames = {}   
   
        for F in (StartPage, Page1, Page2): 
            frame = F(container, self) 
            self.frames[F] = frame  
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(StartPage) 
   
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
   
class StartPage(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.config(bg="#DFEFF0")

        Titulo=tk.Label (self, text="Métodos para encontrar raíces", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",40 ))
        Titulo.place(x=15, y=60)

        Titulo2=tk.Label (self, text="Métodos Cerrado y Abierto", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black",33 ))
        Titulo2.place(x=130, y=120)

        Subtitulo=tk.Label (self, text="Bisección - Raphson", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",28))
        Subtitulo.place(x=250, y=180)

        ##Info
        Info=tk.Label (self, text="Selecciona con que método deseas buscar la raíz", fg="#002060", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",20))
        Info.place(x=100, y=260)
        
        
        Info=tk.Label (self, text="Digite la función (con variable x): Multipicación (*) - Potencia (**) Por ejemplo: x**3-x*2+1 ", fg="#002060", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",13))
        Info.place(x=30, y=300)

        Info=tk.Label (self, text="Creadores", fg="#7D9C9F", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",12))
        Info.place(x=340, y=565)

        Info=tk.Label (self, text="Airlenys Recuero , Gabriela Vásquez", fg="#7D9C9F", bg="#DFEFF0") 
        Info.config(font=("Segoe UI Black",12))
        Info.place(x=240, y=600)
        
        ##Botones 
        MCerrado=tk.Button(self, text="Método Cerrado: Bisección", foreground="#002060" , background="#D5F4FF", width=40, height=8 ,command = lambda : controller.show_frame(Page1)) 
        MCerrado.place(x=100, y=360)
        
        MAbierto=tk.Button(self, text="Método Abierto: Raphson", foreground="#002060" , background="#D5F4FF", width=40 , height=8 , command = lambda : controller.show_frame(Page2))
        MAbierto.place(x=500, y=360)

        Cerrar=tk.Button(self, text="Cerrar", width=10, command= self.cerrar)
        Cerrar.place(x=750, y=590) 
    
    def cerrar(self):
        self.quit()  
  
class Page1(tk.Frame): 
      
    def __init__(self, parent, controller): 
          
        self.vent = tk.Frame.__init__(self, parent)
        self.config(bg="#DFEFF0")
        self.function=tk.StringVar()
        self.ValorA=tk.StringVar()
        self.ValorB=tk.StringVar()
        self.MAraiz=tk.StringVar()

        #Titulos
        Titulo=tk.Label (self, text="Métodos de búsqueda de raíces", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",30 ))
        Titulo.place(x=130, y=10)

        Titulo2=tk.Label (self, text="Método Cerrado", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black", 20 ))
        Titulo2.place(x=290, y=60)

        Subtitulo=tk.Label (self, text="Bisección", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",18))
        Subtitulo.place(x=350, y=100)

        #Entrada
        info=tk.Label (self, text="Ingresar la Función:", fg="#20664A", bg="#DFEFF0") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=60, y=180)
 
        self.Entradafunc=Entry(self, textvariable= self.function)
        self.Entradafunc.config(insertbackground="#002060" , justify=CENTER, font=("Times",15))
        self.Entradafunc.place(x=90, y=225 , width=210, height=30)

        
        info=tk.Label (self, text="Valores iniciales:", fg="#20664A", bg="#DFEFF0") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=90, y=280)

        info=tk.Label (self, text="a=", fg="#20664A", bg="#DFEFF0") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=80, y=320)

        self.EntradaXA=Entry(self, textvariable= self.ValorA)
        self.EntradaXA.config(insertbackground="#002060" , justify=CENTER, font=("Times",12))
        self.EntradaXA.place(x=115, y=325 , width=40, height=30)

        info2=tk.Label (self, text="b=", fg="#20664A", bg="#DFEFF0") 
        info2.config(font=("Segoe UI Black",15))
        info2.place(x=200, y=320)
        
        self.EntradaXB=Entry(self, textvariable= self.ValorB)
        self.EntradaXB.config(insertbackground="#002060" , justify=CENTER, font=("Times",15))
        self.EntradaXB.place(x=235, y=325 , width=40, height=30)
        
        #Gráfica
        self.Gráfica=tk.LabelFrame(self)
        self.Gráfica.place(x=370, y=190)
        self.Gráfica.config( width=435, height=370, borderwidth = 5, relief="groove")


        #Botón
        Convertir=tk.Button(self, text="Convertir", width=15, command=self.MAbierto) 
        Convertir.place(x=130, y=375)

        Resetear=tk.Button(self, text="Resetear", width=15 , command=self.reset)
        Resetear.place(x=425, y=595)
        
        regresar=tk.Button(self, text="Regresar", width=15, command = lambda : [controller.show_frame(StartPage), self.reset()])
        regresar.place(x=625, y=595)

        #Salida
        Salidainfo=tk.Label (self, text="La raíz de la función es:", fg="#20664A", bg="#DFEFF0") 
        Salidainfo.config(font=("Segoe UI Black",15))
        Salidainfo.place(x=30, y=450)
    
        self.Pantalla2 = tk.Label(self, textvariable= self.MAraiz) 
        self.Pantalla2.config(foreground="white", background="black", width=35, height=3)
        self.Pantalla2.place(x=60, y=495)
    
    def calcular(self):

        x = Symbol('x')
        ecu= parse_expr(self.function.get())
        fx=sp.lambdify(x,ecu)
 

        self.x = range( -3, 9, 1)
        self.figura = Figure(figsize=(6, 5), dpi=70)
        self.figura.add_subplot(111).plot(self.x, [fx(i) for i in self.x], '-o')

        self.canvas = FigureCanvasTkAgg(self.figura, master=self.Gráfica)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=0)
    

    def MAbierto(self):
        
        try:
            self.calcular()
            x = Symbol('x')

            fx= parse_expr(self.function.get())
            a= float(self.ValorA.get())
            b= float(self.ValorB.get())

            tolera = 0.001
            fx= sp.lambdify(x,fx)
            # PROCEDIMIENTO
            tramo = abs(b-a)
            while not(tramo<=tolera):
                fa = fx(a)
                fb = fx(b)
                c = float(b - fb*(a-b)/(fa-fb))
                fc = fx(c)
                cambia = np.sign(fa)*np.sign(fc)
                if (cambia > 0):
                    tramo = abs(c-a)
                    a = c
                else:
                    tramo = abs(b-c)
                    b = c
            raiz = c
            return self.MAraiz.set(raiz)

        except ValueError:
                MessageBox.showerror("Error", "Ingrese un valor valido")




    #----------------------------------------------------------------------

    def reset(self):
        self.Entradafunc.delete(0 , "end")
        self.EntradaXA.delete(0 , "end")
        self.EntradaXB.delete(0 , "end")
        self.MAraiz.set(' ')
        for item in self.canvas.get_tk_widget().find_all(): self.canvas.get_tk_widget().delete(item)
        
class Page2(tk.Frame):  
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.config(bg="#DFEFF0")
        self.function=tk.StringVar()
        self.interseccion=tk.StringVar()
        self.MCderivada=tk.StringVar()
        self.MCraiz=tk.StringVar()

        #Titulos
        Titulo=tk.Label (self, text="Métodos de búsqueda de raíces", fg="#002060", bg="#DFEFF0" )
        Titulo.config(font=("Cooper Black",30 ))
        Titulo.place(x=130, y=10)

        Titulo2=tk.Label (self, text="Método Abierto", fg="#20664A", bg="#DFEFF0" )
        Titulo2.config(font=("Segoe UI Black", 20 ))
        Titulo2.place(x=290, y=60)

        Subtitulo=tk.Label (self, text="Raphson", fg="#20664A", bg="#DFEFF0") 
        Subtitulo.config(font=("Segoe UI Black",18))
        Subtitulo.place(x=350, y=100)

        #Entrada
        info=tk.Label (self, text="Ingresa la función:", fg="#20664A", bg="#DFEFF0") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=60, y=180)
 
        self.Entradafunc=Entry(self, textvariable= self.function)
        self.Entradafunc.config(insertbackground="#002060" , justify=CENTER, font=("Times",15))
        self.Entradafunc.place(x=90, y=225 , width=210, height=30, )
        
        info=tk.Label (self, text="Intersección: ", fg="#20664A", bg="#DFEFF0") 
        info.config(font=("Segoe UI Black",15))
        info.place(x=60, y=280)
        
        self.EntradaDeri=Entry(self, textvariable= self.interseccion)
        self.EntradaDeri.config(insertbackground="#002060" , justify=CENTER, font=("Times",15))
        self.EntradaDeri.place(x=200, y=285 , width=105, height=30, )
        
        #Gráfica
        self.Gráfica=tk.LabelFrame(self)
        self.Gráfica.place(x=370, y=190)
        self.Gráfica.config( width="435", height="370", borderwidth = 5, relief="groove")
        

        #Botón
        Convertir=tk.Button(self, text="Convertir", width=15, command=self.MCerrado)
        Convertir.place(x=130, y=340)

        Resetear=tk.Button(self, text="Resetear", width=10 , command=self.reset)
        Resetear.place(x=425, y=595)
        
        Graficar=tk.Button(self, text="Graficar", width=10 , command=self.calcular)
        Graficar.place(x=700, y=150)
        
        regresar=tk.Button(self, text="Regresar", width=15, command = lambda : [controller.show_frame(StartPage), self.reset()])
        regresar.place(x=625, y=595)

        #Salida
        Salidader=tk.Label (self, text="La derivada es:", fg="#20664A", bg="#DFEFF0") 
        Salidader.config(font=("Segoe UI Black",15))
        Salidader.place(x=30, y=410)

        self.Pantalla1 = tk.Label(self, foreground="black", width=18, height=1, borderwidth = 1, relief="raised", textvariable= self.MCderivada) 
        self.Pantalla1.place(x=200, y=420)

        Salidainfo=tk.Label (self, text="La raíz de la función es:", fg="#20664A", bg="#DFEFF0") 
        Salidainfo.config(font=("Segoe UI Black",15))
        Salidainfo.place(x=30, y=470)
    
        self.Pantalla2 = tk.Label(self, textvariable= self.MCraiz) 
        self.Pantalla2.config(foreground="white", background="black", width=35, height=3)
        self.Pantalla2.place(x=70, y=520)

    def calcular(self):
        # x**3-2*x-5 
        x = Symbol('x')

        ecu= parse_expr(self.function.get())
        fx=sp.lambdify(x,ecu)

        self.x = range( -4, 5, 1)
        self.figura = Figure(figsize=(6, 5), dpi=70)
        self.figura.add_subplot(111).plot(self.x, [fx(i) for i in self.x], '-o')
    
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.Gráfica)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=0)
        #890101

    def MCerrado(self):
        try:
            self.calcular()
            x = Symbol('x')
            fx= parse_expr(self.function.get())
            xi= float(self.interseccion.get())
            y = fx
            derivada = sp.diff(y,x) 
            tolera = 0.001
            tramo = abs(2*tolera)
            while (tramo >= tolera):
                
                fxx  = fx.subs(x,xi)
                dfx = derivada.subs(x,xi)
                xnuevo = float((xi) - (fxx / dfx))

                tramo  = abs(xnuevo - xi)
                xi = xnuevo

            np.set_printoptions(precision = 4)
            return (self.MCraiz.set(xi) , self.MCderivada.set(derivada))
        
        except ValueError:
                MessageBox.showerror("Error", "Ingrese un valor valido")

    #----------------------------------------------------------------------

    def reset(self):
        self.Entradafunc.delete(0 , "end")
        self.EntradaDeri.delete(0 , "end")
        self.MCderivada.set(' ')
        self.MCraiz.set(' ')
        for item in self.canvas.get_tk_widget().find_all(): self.canvas.get_tk_widget().delete(item)
        
  
app = tkinterApp() 
ancho_ventana = 850
alto_ventana = 750

x_ventana = app.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = app.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
app.geometry(posicion)

app.resizable(0,0)
app.geometry("850x650")
app.title("Búsqueda de raíces")
app.mainloop() 