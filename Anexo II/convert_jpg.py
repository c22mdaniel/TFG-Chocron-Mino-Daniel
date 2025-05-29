import os
import shutil
from PIL import Image

# Carpeta de entrada y salida
carpeta_entrada = "/home/daniel/Pruebas-TFG"
carpeta_salida = "/home/daniel/Pruebas-JPG"

# Crear carpeta de salida si no existe
os.makedirs(carpeta_salida, exist_ok=True)

# Formatos a convertir
formatos_convertibles = ('.png', '.tif', '.tiff', '.bmp')
# Formatos ya en JPEG que se copian tal cual
formatos_jpeg = ('.jpg', '.jpeg')

# Procesar archivos
for archivo in os.listdir(carpeta_entrada):
    ruta_entrada = os.path.join(carpeta_entrada, archivo)
    nombre_base, extension = os.path.splitext(archivo)
    extension = extension.lower()

    if extension in formatos_convertibles:
        imagen = Image.open(ruta_entrada).convert("RGB")
        nombre_salida = nombre_base + ".jpg"
        ruta_salida = os.path.join(carpeta_salida, nombre_salida)
        imagen.save(ruta_salida, format="JPEG", quality=95)
        print(f"[Convertido] {archivo} → {nombre_salida}")

    elif extension in formatos_jpeg:
        ruta_salida = os.path.join(carpeta_salida, archivo)
        shutil.copy2(ruta_entrada, ruta_salida)
        print(f"[Copiado] {archivo}")

    else:
        print(f"[Omitido] {archivo} (formato no compatible)")
