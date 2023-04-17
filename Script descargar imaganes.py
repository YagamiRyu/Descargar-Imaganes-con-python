import tkinter as tk
import urllib.request
from PIL import Image
from io import BytesIO

class ImageDownloader:
    def __init__(self, master):
        self.master = master
        self.master.title("Descargar imágenes")
        
        # Crear los widgets
        self.label_url = tk.Label(self.master, text="URL de la imagen:")
        self.entry_url = tk.Entry(self.master, width=50)
        self.label_name = tk.Label(self.master, text="Nombre de archivo:")
        self.entry_name = tk.Entry(self.master, width=50)
        self.button_download = tk.Button(self.master, text="Descargar", command=self.download_image)
        self.button_exit = tk.Button(self.master, text="Salir", command=self.exit_program)
        
        # Colocar los widgets en la ventana
        self.label_url.grid(row=0, column=0, padx=5, pady=5)
        self.entry_url.grid(row=0, column=1, padx=5, pady=5)
        self.label_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)
        self.button_download.grid(row=2, column=0, padx=5, pady=5)
        self.button_exit.grid(row=2, column=1, padx=5, pady=5)
        
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
        tk.messagebox.showinfo("Descarga exitosa", f"La imagen se ha descargado como {filename}")
        
    def exit_program(self):
        self.master.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDownloader(root)
    root.mainloop()
