from tkinter import *
from tkinter import filedialog
from PIL import Image

# Función para cargar y decodificar la imagen
def cargar_imagen():
    # Abre el cuadro de diálogo para seleccionar una imagen
    ruta_imagen = filedialog.askopenfilename(initialdir='/', title='Seleccionar imagen', filetypes=(('Archivos de imagen', '*.png *.jpg *.jpeg'), ('Todos los archivos', '*.*')))
    # Si se selecciona una imagen, carga y decodifica los datos ocultos
    if ruta_imagen:
        imagen = Image.open(ruta_imagen)
        formato = var_formato.get()
        if formato == 'RGB':
            datos_ocultos = imagen.getdata()
        elif formato == 'RGBA':
            datos_ocultos = imagen.getdata(3)
        elif formato == 'RED':
            datos_ocultos = [pixel[0] for pixel in imagen.getdata()]
        elif formato == 'GREEN':
            datos_ocultos = [pixel[1] for pixel in imagen.getdata()]
        elif formato == 'BLUE':
            datos_ocultos = [pixel[2] for pixel in imagen.getdata()]
        elif formato == 'ALPHA':
            datos_ocultos = [pixel[3] for pixel in imagen.getdata()]
        # Muestra los datos ocultos en la interfaz de usuario
        txt_datos.delete('1.0', END)
        txt_datos.insert(END, datos_ocultos)

# Crea la interfaz de usuario
root = Tk()
root.title('Decodificador de imágenes')
root.geometry('400x400')

# Crea una lista de opciones de formato
opciones_formato = ['RGB', 'RGBA', 'RED', 'GREEN', 'BLUE', 'ALPHA']

# Crea una variable para almacenar el formato seleccionado
var_formato = StringVar(root)
var_formato.set(opciones_formato[0])

# Crea un menú desplegable para seleccionar el formato
menu_formato = OptionMenu(root, var_formato, *opciones_formato)
menu_formato.pack()

# Crea un botón para cargar la imagen
btn_cargar = Button(root, text='Cargar imagen', command=cargar_imagen)
btn_cargar.pack()

# Crea un cuadro de texto para mostrar los datos ocultos
txt_datos = Text(root)
txt_datos.pack()

root.mainloop()