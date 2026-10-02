import shutil
import logging
from collections import Counter
from pathlib import Path
from config import (
    DOWNLOADS_PATH, CATEGORIES,
    IGNORED_EXTENSIONS, IGNORED_FILES, IGNORED_PREFIXES,
)

BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR / "logs"
LOG_PATH = LOGS_DIR / "organizer.log"
LOGS_DIR.mkdir(exist_ok=True)


logging.basicConfig(
    filename=LOG_PATH,
    encoding="utf-8",
    level= logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def unique_name(destination, filename):
    final_path = destination / filename
    if not final_path.exists():
        return final_path
    name, ext = final_path.stem, final_path.suffix
    counter = 1
    while (destination / f"{name}({counter}){ext}").exists():
        counter += 1
    return destination / f"{name}({counter}){ext}"

def print_summary(moved, skipped):
    total = sum(moved.values())
    if total == 0 and skipped == 0:
        summary = "No había archivos que organizar."
    else:
        plural = "s" if total != 1 else ""
        summary = f"{total} archivo{plural} movido{plural}"
        if moved:
            detail = ", ".join(f"{count} {folder}" for folder, count in moved.most_common())
            summary += f" ({detail})"
        summary += f", {skipped} omitido{'s' if skipped != 1 else ''}"
    print()
    print(summary)
    logging.info(f"Resumen: {summary}")

def organize():
    moved = Counter()
    skipped = 0
    for file in DOWNLOADS_PATH.iterdir():
        name = file.name

        # Ignorar carpetas (incluidas las del script)
        if file.is_dir():
            continue

        extension = file.suffix.lower()

        # Ignorar descargas a medias, archivos del sistema y de bloqueo
        if (extension in IGNORED_EXTENSIONS
                or name.lower() in IGNORED_FILES
                or name.startswith(IGNORED_PREFIXES)):
            continue

        folder = CATEGORIES.get(extension, "Otros")

        destination = DOWNLOADS_PATH / folder
        destination.mkdir(exist_ok=True)

        try:
            final_path = unique_name(destination, name)
            shutil.move(file, final_path)
            message = f"{name} → {folder}/"
            print(f"OK {message}")
            logging.info(message)
            moved[folder] += 1
        except PermissionError:
            print(f"NOT OK {name} está en uso, se omite.")
            logging.warning(f"{name} en uso, omitido.")
            skipped += 1
        except FileNotFoundError:
            print(f"NOT OK {name} no encontrado, se omite.")
            logging.warning(f"{name} no encontrado, omitido.")
            skipped += 1

    print_summary(moved, skipped)

organize()
