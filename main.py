import os
import shutil
import logging
from config import DOWNLOADS_PATH, CATEGORIAS

# Carpetas que crea el script
CARPETAS_SISTEMA = set(CATEGORIAS.values()) | {"Otros"}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "logs", "organizer.log")
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)


logging.basicConfig(
    filename=LOG_PATH,
    level= logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def unique_name(destination, filename):
    final_path = os.path.join(destination, filename)
    if not os.path.exists(final_path):
        return final_path
    name, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(os.path.join(destination, f"{name}({counter}){ext}")):
        counter += 1
    return os.path.join(destination, f"{name}({counter}){ext}")

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

        folder = CATEGORIAS.get(extension, "Otros")

        destination = os.path.join(DOWNLOADS_PATH, folder)
        os.makedirs(destination, exist_ok=True)

        try:
            final_path = unique_name(destination, file)
            shutil.move(file_path, final_path)
            message = f"{file} → {folder}/"
            print(f"OK {message}")
            logging.info(message)
        except PermissionError:
            print(f"NOT OK {file} está en uso, se omite.")
            logging.warning(f"{file} en uso, omitido.")
        except FileNotFoundError:
            print(f"NOT OK {file} no encontrado, se omite.")
            logging.warning(f"{file} no encontrado, omitido.")

organize()