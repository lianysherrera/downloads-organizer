# Organizador de Descargas

Herramienta en Python que vigila tu carpeta de descargas en tiempo real y mueve cada archivo a su carpeta correspondiente según la extensión: imágenes, documentos, vídeos, música y más.

## ¿Qué hace?

- Detecta archivos en tu carpeta de Descargas
- Los mueve automáticamente a subcarpetas según su extensión:


| Extensiones | Carpeta |
|---|---|
| `.jpg` `.jpeg` `.png` `.gif` `.svg` `.webp` `.avif` `.bmp` `.tiff` `.ico` `.heic` `.raw` | `Imagenes` |
| `.pdf` `.xps` | `PDFs` |
| `.doc` `.docx` `.txt` `.md` `.ppt` `.pptx` `.odt` `.rtf` `.epub` `.pages` | `Documentos` |
| `.xls` `.xlsx` `.csv` `.ods` | `Excel` |
| `.mp4` `.mov` `.avi` `.mkv` `.wmv` `.flv` `.webm` | `Videos` |
| `.mp3` `.wav` `.flac` `.aac` `.ogg` `.wma` `.m4a` | `Musica` |
| `.zip` `.rar` `.7z` `.tar` `.gz` `.bz2` `.xz` `.iso` | `Comprimidos` |
| `.exe` `.msi` `.dmg` `.deb` `.rpm` `.appimage` `.apk` `.msix` | `Programas` |
| `.po` `.mo` | `i18n` |
| `.ova` | `MaquinaVirtual` |
| `.py` `.js` `.ts` `.java` `.cpp` `.c` `.html` `.css` `.json` `.xml` `.yaml` `.sql` | `Codigo` |
| `.ttf` `.otf` `.woff` `.woff2` | `Fuentes` |
| `.stl` `.obj` `.blend` `.fbx` | `3D` |
| `.torrent` | `Torrents` |
| `.db` `.sqlite` `.bak` | `BaseDatos` |
| cualquier otra | `Otros` |


## Instalación

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la carpeta del proyecto con tu ruta de Descargas:

```
DOWNLOADS_PATH=C:/Users/TuUsuario/Downloads
```

Si no lo configuras, usará automáticamente la carpeta de Descargas de tu usuario.

## Uso

**Opción 1 — Doble clic** en `organizar.bat` (Windows)

**Opción 2 — Terminal:**

```bash
python main.py
```
