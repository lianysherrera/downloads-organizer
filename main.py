import os
import shutil
from config import DOWNLOADS_PATH, CATEGORIAS

def organize():
    for file in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, file)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file)
        extension = extension.lower()

        folder = CATEGORIAS.get(extension, "Others")

        destination = os.path.join(DOWNLOADS_PATH, folder)
        os.makedirs(destination, exist_ok=True)

        shutil.move(file_path, os.path.join(destination, file))
        print(f"YES {file} → {folder}/")

organize()