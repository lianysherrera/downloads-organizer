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
    ".bmp": "Imagenes",
    ".tiff": "Imagenes",
    ".ico": "Imagenes",
    ".heic": "Imagenes",
    ".raw": "Imagenes",

    ".pdf": "PDFs",
    ".xps": "PDFs",

    ".doc": "Documentos",
    ".docx": "Documentos",
    ".md": "Documentos",
    ".txt": "Documentos",
    ".ppt": "Documentos",
    ".pptx": "Documentos",
    ".odt": "Documentos",
    ".rtf": "Documentos",
    ".epub": "Documentos",
    ".pages": "Documentos",

    ".xls": "Excel",
    ".xlsx": "Excel",
    ".csv": "Excel",
    ".ods": "Excel",

    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",

    ".mp3": "Musica",
    ".wav": "Musica",
    ".flac": "Musica",
    ".aac": "Musica",
    ".ogg": "Musica",
    ".wma": "Musica",
    ".m4a": "Musica",

    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
    ".7z": "Comprimidos",
    ".tar": "Comprimidos",
    ".gz": "Comprimidos",
    ".bz2": "Comprimidos",
    ".xz": "Comprimidos",
    ".iso": "Comprimidos",

    ".exe": "Programas",
    ".msi": "Programas",
    ".dmg": "Programas",
    ".deb": "Programas",
    ".rpm": "Programas",
    ".appimage": "Programas",
    ".apk": "Programas",
    ".msix": "Programas",

    ".po": "i18n",
    ".mo": "i18n",

    ".ova": "MaquinaVirtual",

    ".py": "Codigo",
    ".js": "Codigo",
    ".ts": "Codigo",
    ".java": "Codigo",
    ".cpp": "Codigo",
    ".c": "Codigo",
    ".html": "Codigo",
    ".css": "Codigo",
    ".json": "Codigo",
    ".xml": "Codigo",
    ".yaml": "Codigo",
    ".sql": "Codigo",

    ".ttf": "Fuentes",
    ".otf": "Fuentes",
    ".woff": "Fuentes",
    ".woff2": "Fuentes",

    ".stl": "3D",
    ".obj": "3D",
    ".blend": "3D",
    ".fbx": "3D",

    ".torrent": "Torrents",

    ".db": "BaseDatos",
    ".sqlite": "BaseDatos",
    ".bak": "BaseDatos",
}