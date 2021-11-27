from tkinter import *  #Importamos todas las funciones que contiene tkinter

#Creamos el objeto que será la raiz de la aplicación
window = Tk()
#Le agregamos un título
window.title("Bienvenido a la aplicación de Ensaladas Gourmet")
#Determinamos si se podrá cambiar su tamaño
window.resizable(1,1)
#Asignamos un logotipo
window.iconbitmap('foco.ico')
#Asignamos un color
window.config(bg="#87CEEB")

#Para incluir imágenes de otros formatos utilizamos la librería PIL
from PIL import ImageTk, Image
#Cargamos la imágen
img = ImageTk.PhotoImage(Image.open("Captura3.jpg"))
#Y la desplegamos
Label(window, image=img).pack(side="left")

#Creamos las etiquetas para solicitar el nombre y apellido, ademas el CURP y RFC

frame1 = Frame(window)
frame1.pack()
label1 = Label(frame1, text="Nombre y Apellido")
label1.grid(row=0, column=0)
entry1 = Entry(frame1)
entry1.grid(row=0, column=1)
label2 = Label(frame1, text="CURP")
label2.grid(row=1, column=0)
entry2 = Entry(frame1)
entry2.grid(row=1, column=1)
label3 = Label(frame1, text="RFC")
label3.grid(row=2, column=0)
entry3 = Entry(frame1)
entry3.grid(row=2, column=1)

#creamos los radiobutton para determinar el género.

#Con esta función le indicamos que obtenga el valor de la opción que marque el usuario
def seleccionar():
	monitor.config(text="{}".format(genero.get()))

#Con esta función reseteamos el valor de la opción que ha elegido el usuario
def reset():
	genero.set(None) #Establecemos el valor en nulo
	monitor.config(text="")
genero = IntVar()
#Cada Radiobutton debe tener asignado un valor diferente
Radiobutton(window, text="Femenino", variable=genero, value=1, command=seleccionar).pack()
Radiobutton(window, text="Masculino", variable=genero, value=2, command=seleccionar).pack()

monitor = Label(window)
Button(window, text="Reiniciar", command=reset).pack()

#Creamos las opciones del cliente por medio de checkbutton
def seleccionar():
	cadena = ""
	if (verdura.get()):
		cadena += "Con lechuga, jitomate y betabel"
	else:
		cadena += " Sin verdura"

	if (pollo.get()):
		cadena += " ,Con pollo"
	else:
		cadena += " Sin pollo"

	if (aderezo.get()):
		cadena += " y con aderezo"
	else:
		cadena += " y sin aderezo"
	

	monitor.config(text=cadena)


verdura = IntVar() 	# 1 si, 0 no
pollo = IntVar()	# 1 si, 0 no
aderezo = IntVar()

frame = Frame(window)
frame.pack(side="left")

Label(frame, text="¿Que lleva la ensalada?").pack(anchor="w")
Checkbutton(frame, text="Verdura", variable=verdura, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Pollo", variable=pollo, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Aderezo", variable=aderezo, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

window.mainloop()

