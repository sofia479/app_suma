# Se imprta la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

# -----------------------------
# funciones de la app
# -----------------------------

def sumar():
    c = int(a.get()) + int (b.get())
    t_resultados.insert(INSERT, "La suma de " + a.get() + " + " + b.get() + " casi siempre es " + str(c) + "\n")
        

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

# -----------------------------
# Ventana principal de la app
# -----------------------------

# Se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto de tipo Tk()

ventana_principal = Tk()

# Titulo de la ventana
ventana_principal.title("sofia galvis cuellar")

# Tamaño de la ventana
ventana_principal.geometry("800x500")

# deshabilitar boton maximizar de la ventana
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="black")

# ------------------------
# Variables globales
#-------------------------
a = StringVar()
b = StringVar()
c = IntVar()

# ------------------
# Frame 1
# ------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="ivory2", width=780, height=240)
frame_1.place(x=10,y=10)

# Etiqueta para subtitulo 1 de la app
subtitulo1 = Label(frame_1, text="Especialidad en Sistemas")
subtitulo1.config(bg="yellow", fg="blue", font=("Arial",12))
subtitulo1.place(x=390,y=40)

# Etiqueta para subtitulo 2 de la app
subtitulo2 = Label(frame_1, text="SUMA DE DOS ENTEROS")
subtitulo2.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=390,y=70)

# Etiqueta para el valor - a
Label_a = Label(frame_1, text = "a = ")
Label_a.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
Label_a.place(x=390, y=120)

# Entry para el primer valor - a
entry_a = Entry(frame_1, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487, y= 120)

# Etiqueta para el valor - b
Label_b = Label(frame_1, text = "b = ")
Label_b.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
Label_b.place(x=585, y=120)

# Entry para el primer valor - b
entry_b = Entry(frame_1, width=4, textvariable=b)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.place(x=682, y= 120)

# imagen - logo de la app
logo = PhotoImage(file="img/btn-suma.png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=10, y=10)

# Etiqueta para el titulo de la app
titulo = Label(frame_1, text="Colegio san jose delguanenta")
titulo.config(bg="yellow", fg= "blue", font=("Arial", 16))
titulo.place(x=390,y=10)

# ------------------
# Frame 2 - operaciones
# ------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg="ivory2", width=780, height=120)
frame_2.place(x=10,y=260)

#boton de sumar
img_bt_sumar = PhotoImage(file="img/boton_sumar.png")
bt_sumar = Button(frame_2, image = img_bt_sumar, width=105, height=105, command=sumar)
# bt_sumar = Button(frame_2, text="Sumar", width=10)
bt_sumar.place(x=116, y=7)

# boton para borrar entrada y resultados
img_bt_borrar = PhotoImage(file="img/boton_borrar.png")
bt_borrar = Button(frame_2, image = img_bt_borrar, width=105, height=105, command=borrar)
# bt_sumar = Button(frame_2, text="Sumar", width=10)
bt_borrar.place(x=337, y=7)

# boton para cerrar la app
img_bt_salir = PhotoImage(file="img/boton_salir.png")
bt_salir = Button(frame_2, image = img_bt_salir, width=105, height=105, command=salir)
# bt_sumar = Button(frame_2, text="Sumar", width=10)
bt_salir.place(x=558, y=7)

# ------------------
# Frame 3 - resultado
# ------------------

frame_3 = Frame(ventana_principal)
frame_3.config(bg="ivory2", width=780, height=100)
frame_3.place(x=10,y=390)

# Area de texto
t_resultados = Text(frame_3, width=50, height=100)
t_resultados.config(bg="green", fg="white", font=("Courier",20))
t_resultados.pack()

# Metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()