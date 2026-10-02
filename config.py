import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

DOWNLOADS_PATH = os.getenv("DOWNLOADS_PATH") or str(Path.home() / "Downloads")

# Descargas que todavía no han terminado (Chrome, Edge, Firefox, Safari...)
EXTENSIONES_IGNORADAS = {".crdownload", ".part", ".partial", ".download", ".tmp"}
# Archivos del sistema que no se deben mover
ARCHIVOS_IGNORADOS = {"desktop.ini", "thumbs.db"}
# Prefijos de archivos ocultos y de bloqueo de Office (~$archivo.docx)
PREFIJOS_IGNORADOS = (".", "~$")

# Carpeta de destino -> extensiones que van a ella
GRUPOS = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".avif", ".bmp", ".tiff", ".ico", ".heic", ".raw"],
    "PDFs": [".pdf", ".xps"],
    "Documentos": [".doc", ".docx", ".md", ".txt", ".ppt", ".pptx", ".odt", ".rtf", ".epub", ".pages"],
    "Excel": [".xls", ".xlsx", ".csv", ".ods"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Musica": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"],
    "Programas": [".exe", ".msi", ".dmg", ".deb", ".rpm", ".appimage", ".apk", ".msix"],
    "i18n": [".po", ".mo"],
    "MaquinaVirtual": [".ova"],
    "Codigo": [".py", ".js", ".ts", ".java", ".cpp", ".c", ".html", ".css", ".json", ".xml", ".yaml", ".sql"],
    "Fuentes": [".ttf", ".otf", ".woff", ".woff2"],
    "3D": [".stl", ".obj", ".blend", ".fbx"],
    "Torrents": [".torrent"],
    "BaseDatos": [".db", ".sqlite", ".bak"],
}

# Extensión -> carpeta de destino (lo que usa main.py)
CATEGORIAS = {ext: carpeta for carpeta, extensiones in GRUPOS.items() for ext in extensiones}