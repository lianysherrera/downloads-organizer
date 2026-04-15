import os
import shutil
from config import DOWNLOADS_PATH, CATEGORIAS

# Carpetas que crea el script → no tocar
CARPETAS_SISTEMA = set(CATEGORIAS.values()) | {"Others"}

def organize():
    for file in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, file)

        # Ignorar carpetas (incluidas las del script)
        if os.path.isdir(file_path):
            continue

        # Ignorar carpetas del sistema
        if file in CARPETAS_SISTEMA:
            continue

        _, extension = os.path.splitext(file)
        extension = extension.lower()

        folder = CATEGORIAS.get(extension, "Others")

        destination = os.path.join(DOWNLOADS_PATH, folder)
        os.makedirs(destination, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(destination, file))
            print(f"OK {file} → {folder}/")
        except PermissionError:
            print(f"NOT OK {file} está en uso, se omite.")
        except FileNotFoundError:
            print(f"NOT OK {file} no encontrado, se omite.")

organize()