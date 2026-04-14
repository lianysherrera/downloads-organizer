import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

DOWNLOADS_PATH = os.getenv("DOWNLOADS_PATH") or str(Path.home() / "Downloads")

CATEGORIAS = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".webp": "Images",

    ".pdf": "PDFs",
    ".doc": "Documents",
    ".docx": "Documents",
    ".md": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    ".xls": "Excel",
    ".xlsx": "Excel",
    ".csv": "Excel",

    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",

    ".mp3": "Music",
    ".wav": "Music",

    ".zip": "Compressed",
    ".rar": "Compressed",
    ".7z": "Compressed",

    ".exe": "Programs",
    ".msi": "Programs",
    ".dmg": "Programs",
}