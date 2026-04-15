import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

DOWNLOADS_PATH = os.getenv("DOWNLOADS_PATH") or str(Path.home() / "Downloads")

CATEGORIAS = {
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".gif": "Imagenes",
    ".svg": "Imagenes",
    ".webp": "Imagenes",
    ".avif": "Imagenes",

    ".pdf": "PDFs",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".md": "Documentos",
    ".txt": "Documentos",
    ".ppt": "Documentos",
    ".pptx": "Documentos",

    ".xls": "Excel",
    ".xlsx": "Excel",
    ".csv": "Excel",

    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",

    ".mp3": "Musica",
    ".wav": "Musica",

    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
    ".7z": "Comprimidos",

    ".exe": "Programas",
    ".msi": "Programas",
    ".dmg": "Programas",

    ".po": "i18n",
    ".mo": "i18n",

    ".ova": "MaquinaVirtual",
}