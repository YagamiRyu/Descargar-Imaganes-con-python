import tkinter as tk
from tkinter import ttk, messagebox
import urllib.request
from PIL import Image
from io import BytesIO

class ImageDownloader:
    def __init__(self, master):
        self.master = master
        self.master.title("Descargar imágenes")
        
        # Configurar el estilo
        self.style = ttk.Style()
        self.theme_choice = "clam"  # selecciona aquí el tema que quieras
        self.style.theme_use(self.theme_choice)
        
        # Crear los widgets
        self.label_url = ttk.Label(self.master, text="URL de la imagen:")
        self.entry_url = ttk.Entry(self.master, width=50)
        self.label_name = ttk.Label(self.master, text="Nombre de archivo:")
        self.entry_name = ttk.Entry(self.master, width=50)
        self.button_download = ttk.Button(self.master, text="Descargar", command=self.download_image, state="disabled")
        self.button_exit = ttk.Button(self.master, text="Salir", command=self.exit_program)
        
        # Colocar los widgets en la ventana
        self.label_url.grid(row=0, column=0, padx=5, pady=5)
        self.entry_url.grid(row=0, column=1, padx=5, pady=5)
        self.label_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)
        self.button_download.grid(row=2, column=0, padx=5, pady=5)
        self.button_exit.grid(row=2, column=1, padx=5, pady=5)
        
        # Verificar que los campos estén llenos antes de habilitar el botón de descarga
        self.entry_url.bind("<KeyRelease>", self.check_entries)
        self.entry_name.bind("<KeyRelease>", self.check_entries)
    
    def check_entries(self, event):
        if self.entry_url.get() and self.entry_name.get():
            self.button_download.configure(state="enabled")
        else:
            self.button_download.configure(state="disabled")
        
    def download_image(self):
        # Obtener la URL de la imagen y el nombre de archivo
        url = self.entry_url.get()
        filename = self.entry_name.get()
        
        # Descargar la imagen
        with urllib.request.urlopen(url) as url_response:
            img_data = url_response.read()
            
        # Abrir la imagen con PIL
        img = Image.open(BytesIO(img_data))
        
        # Borrar los datos anteriores de los Entry
        self.entry_url.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        
        # Guardar la imagen
        img.save(filename)
        
        # Mostrar un mensaje de éxito
        messagebox.showinfo("Descarga exitosa", f"La imagen se ha descargado como {filename}")
        
    def exit_program(self):
        self.master.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDownloader(root)
    root.mainloop()
