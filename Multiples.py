import urllib.request

# Lista de URLs de las imágenes que quieres descargar
urls = [
    'https://toon.toomics.com/toon/yTs25CC-xA4jFdhDvpm12wviQeU4IlJNnEQQqhrdGzKU7NjEQ-d70hDe_8pOTr-xXvJer7gLkG9WBzCuYf9-qPITKZptck8Tj3eNVg7_ojc',
    'https://toon.toomics.com/toon/6vfP8pUXTe1ev86nmXCJfSlzofdLWU8nMSbgtp_QgaUt-VNhs-OYRA0_eX0oRkUbfPdbcTRsP1SGeBXo9DQRfaszCL66Ra5jTt1KbpoWo5I',
    'https://toon.toomics.com/toon/1sr3FSLkQIUsDSToCiKC8_jBFHGCwtviKAXwJKu-OKiYjQMUdKMo8rBuLDKhFSBemvFa_jZWCXrqM8FjdPxz7bPcqWjUlI6hBcG84N0UcKQ',
]

# Nombres de los archivos donde quieres guardar las imágenes
nombres_archivos = [
    'imagen1.jpg',
    'imagen2.jpg',
    'imagen3.jpg',
]

# Itera sobre las URLs y descarga cada imagen
for url, nombre_archivo in zip(urls, nombres_archivos):
    urllib.request.urlretrieve(url, nombre_archivo)