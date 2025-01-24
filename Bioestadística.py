# Proyecto de bioestadística básico -

# Importamos las librerías
from customtkinter import *
import matplotlib.pyplot as plt
import pandas as pd 
import scipy
from tkinter import *
import scipy.stats
import seaborn as sns 
import tkinter.messagebox

class Interfaz():
    def __init__(self, Frank):

        # Características que llevará la interfaz del programa de bioestadística
        self.Frank=Frank
        self.Frank.geometry("700x700")
        self.Frank.title("Programa de bioestadística")
        self.Frank.resizable(0,0)
        self.Frank._set_appearance_mode("dark")

        self.contenido_interfaz()

# Método para agregar el contenido de la interfaz 
    def contenido_interfaz(self):

        Titulo=CTkLabel(self.Frank, text="¡Bienvenido a este programa!",
                        font=("Arial", 20,"bold"),
                        text_color="blue",
                         fg_color="#282625",
                         corner_radius=0)
        Titulo.place(x=200, y=70)

        Titulo2=CTkLabel(self.Frank, text="Aquí podrás generar gráficos estadísticos.",
                        font=("Arial", 20,"bold"),
                        text_color="blue",
                         fg_color="#282625",
                         corner_radius=0)
        Titulo2.place(x=150, y=100)

        BotonCajas=CTkButton(self.Frank, text="Gráfico de cajas",bg_color="blue",corner_radius=3, font=("Arial",18), width=220, height=40,
                             command=self.mostrar_entrada_cajas)
        BotonCajas.place(x=250, y=180)

        BotonViolin=CTkButton(self.Frank, text="Gráfico de Violín",bg_color="blue",corner_radius=3,font=("Arial",18), width=220, height=40,
                              command=self.ventana_violin)
        BotonViolin.place(x=250, y=280)

        BotonHistograma=CTkButton(self.Frank, text="Gráfico de Histograma",bg_color="blue",corner_radius=3,font=("Arial",18), width=220, height=40,
                                  command=self.ventana_histograma)
        BotonHistograma.place(x=250, y=380)

        BotonRegresion=CTkButton(self.Frank, text="Regresión lineal",bg_color="blue",corner_radius=3,font=("Arial",18), width=220, height=40,
                                 command=self.ventana_regresion)
        BotonRegresion.place(x=250, y=480)

        BotonDensidad=CTkButton(self.Frank, text="Gráfico de Densidad", bg_color="blue", corner_radius=3, font=("Arial",18), width=220, height=40,
                                command=self.Ventana_Densidad)
        BotonDensidad.place(x=250, y=580)

# Generamos el método para abrir una nueva ventana para el gráfico de cajas 
    def mostrar_entrada_cajas(self):
        # Crear una nueva ventana usando Toplevel
        ventana_grafico = Toplevel(self.Frank)
        ventana_grafico.geometry("700x800")
        ventana_grafico.title("Gráfico de Cajas")
        ventana_grafico.resizable(0, 0)

        # Etiqueta para instrucciones
        Instrucciones = CTkLabel(ventana_grafico, text="Ingresa tus datos (separados por comas):", font=("Arial", 18))
        Instrucciones.place(x=50, y=70)

        # Entrada de datos
        entrada_datos = CTkEntry(ventana_grafico, font=("Arial", 18), width=300)
        entrada_datos.place(x=50, y=150)

        # Botón para generar gráfico de cajas
        BotonGenerar = CTkButton(ventana_grafico, text="Generar Gráfico de Cajas", bg_color="blue", corner_radius=3,
                                 font=("Arial", 18), width=220, height=40, command=lambda: self.generar_grafico_cajas(entrada_datos))
        BotonGenerar.place(x=250, y=250)


# Método para generar el gráfico de cajas desde la ventana secundaria 
    def generar_grafico_cajas(self, entrada_datos):
        # Obtener los datos de la entrada
        try:
            datos = list(map(float, entrada_datos.get().split(',')))
            plt.figure(figsize=(6, 4))
            sns.boxplot(data=datos)
            plt.title("Gráfico de Cajas")
            plt.show()
        except ValueError:
            tkinter.messagebox.showerror("Error", "Por favor, ingresa datos válidos separados por comas.")

# Método para agregar una nueva ventana para el gráfico de histograma 
    def ventana_histograma(self):
        # Crear una nueva ventana usando Toplevel
        ventana_grafico = Toplevel(self.Frank)
        ventana_grafico.geometry("700x800")
        ventana_grafico.title("Gráfico de Cajas")
        ventana_grafico.resizable(0, 0)

        # Etiqueta para instrucciones
        Instrucciones = CTkLabel(ventana_grafico, text="Ingresa tus datos (separados por comas):", font=("Arial", 18))
        Instrucciones.place(x=50, y=70)

        # Entrada de datos
        entrada_datos1 = CTkEntry(ventana_grafico, font=("Arial", 18), width=300)
        entrada_datos1.place(x=50, y=150)

        # Botón para generar el histograma 
        Boton_Histograma=CTkButton(ventana_grafico, text="Generar histograma",bg_color="blue", corner_radius=3,
                                 font=("Arial", 18), width=220, height=40, command=lambda: self.generar_histograma(entrada_datos1))
        Boton_Histograma.place(x=250, y=250)

    def generar_histograma(self, entrada_datos1):
        # Obtener los datos de la entrada: 
        try:
            datos=list(map(float, entrada_datos1.get().split(',')))
            plt.figure(figsize=(10, 6))
            sns.histplot(datos)
            plt.title('Gráfico de Histograma')
            plt.xlabel('Datos')
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()
        except ValueError:
            tkinter.messagebox.showerror("Error", "Por favor, ingresa datos válidos separados por comas.")

    def ventana_violin(self):

        # Crear una nueva ventana usando Toplevel
        ventana_grafico = Toplevel(self.Frank)
        ventana_grafico.geometry("700x800")
        ventana_grafico.title("Gráfico de Violín ")
        ventana_grafico.resizable(0, 0)

        # Etiqueta para instrucciones
        Instrucciones = CTkLabel(ventana_grafico, text="Ingresa tus datos (separados por comas):", font=("Arial", 18))
        Instrucciones.place(x=50, y=70)

        # Entrada de datos
        entrada_datos2 = CTkEntry(ventana_grafico, font=("Arial", 18), width=300)
        entrada_datos2.place(x=50, y=150)

        # Botón para generar el histograma 
        Boton_Violin=CTkButton(ventana_grafico, text="Generar histograma",bg_color="blue", corner_radius=3,
                                 font=("Arial", 18), width=220, height=40, command=lambda: self.generar_violin(entrada_datos2))
        Boton_Violin.place(x=250, y=250)

    def generar_violin(self, entrada_datos2):
        datos=list(map(float,entrada_datos2.get().split(",")))
        sns.violinplot(data=datos)  
        plt.title('Gráfico de Violín')
        plt.xlabel('Datos')
        plt.ylabel('Densidad')
        plt.grid(True)
        plt.show()

    def ventana_regresion(self):
        # Crear una nueva ventana usando Toplevel
        ventana_grafico = Toplevel(self.Frank)
        ventana_grafico.geometry("700x800")
        ventana_grafico.title("Regresión lineal")
        ventana_grafico.resizable(0, 0)

        # Etiqueta para instrucciones
        Instrucciones = CTkLabel(ventana_grafico, text="Ingresa los valores de x (separados por comas):", font=("Arial", 18))
        Instrucciones.place(x=50, y=70)

        Instrucciones_y=CTkLabel(ventana_grafico, text=" Ingresa los valores de y (separados por comas):", font=("Arial",18))
        Instrucciones_y.place(x=50, y=220)

        # Entrada de datos
        entrada_datos_x = CTkEntry(ventana_grafico, font=("Arial", 18), width=300)
        entrada_datos_x.place(x=50, y=150)

        entrada_datos_y= CTkEntry(ventana_grafico, font=("Arial", 18), width=300)
        entrada_datos_y.place(x=50, y=260)

        # Botón para generar la regresión lineal 
        Boton_Regresion=CTkButton(ventana_grafico, text="Generar Regresión",bg_color="blue", corner_radius=3,
                                 font=("Arial", 18), width=220, height=40, command=lambda: self.Generar_Regresion(entrada_datos_x,entrada_datos_y))
        Boton_Regresion.place(x=250, y=350)
    
    def Generar_Regresion(self, entrada_datos_x,entrada_datos_y):
        datos_x=list(map(float, entrada_datos_x.get().split(",")))
        datos_y=list(map(float, entrada_datos_y.get().split(",")))

        dict={"Datos_x":datos_x, "Datos_y":datos_y}
        Dataframe=pd.DataFrame(dict)

        p= sns.regplot(data=Dataframe, x=Dataframe.Datos_x, y=Dataframe.Datos_y)

        slope, intercept, r, p, sterr = scipy.stats.linregress(x=p.get_lines()[0].get_xdata(),
                                                       y=p.get_lines()[0].get_ydata())
        plt.text(min(datos_x), max(datos_y), 'y = ' + str(round(intercept,3)) + ' + ' + str(round(slope,3)) + 'x')
        plt.show()

    def Ventana_Densidad(self):
        
        # Crear una nueva ventana usando Toplevel
        ventana_grafico = Toplevel(self.Frank)
        ventana_grafico.geometry("700x800")
        ventana_grafico.title("Gráfico de Densidad")
        ventana_grafico.resizable(0, 0)

        # Etiqueta para instrucciones
        Instrucciones = CTkLabel(ventana_grafico, text="Ingresa los valores (separados por comas):", font=("Arial", 18))
        Instrucciones.place(x=50, y=70)

        # Entrada de datos
        entrada_datos6 = CTkEntry(ventana_grafico, font=("Arial", 18), width=300)
        entrada_datos6.place(x=50, y=150)

        # Botón para generar la regresión lineal 
        Boton_Regresion=CTkButton(ventana_grafico, text="Generar gráfico",bg_color="blue", corner_radius=3,
                                 font=("Arial", 18), width=220, height=40, command=lambda: self.Generar_Densidad(entrada_datos6))
        Boton_Regresion.place(x=250, y=350)

    def Generar_Densidad(self, entrada_datos6):
        datos=list(map(float, entrada_datos6.get().split(",")))
        dict={"Datos":datos}
        Dataframe=pd.DataFrame(dict)

        sns.kdeplot(data=Dataframe, x="Datos", multiple="stack")
        plt.show()

Frank=CTk()
frank=Interfaz(Frank)
Frank.mainloop()
