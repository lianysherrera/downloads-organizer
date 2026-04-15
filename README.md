# Organizador de Descargas

Herramienta en Python que vigila tu carpeta de descargas en tiempo real y mueve cada archivo a su carpeta correspondiente según la extensión: imágenes, documentos, vídeos, música y más.

## ¿Qué hace?

- Detecta archivos en tu carpeta de Descargas
- Los mueve automáticamente a subcarpetas según su extensión:


| Extensiones | Carpeta |
|---|---|
| `.jpg` `.jpeg` `.png` `.gif` `.svg` `.webp` `.avif` | `Imagenes` |
| `.pdf` | `PDFs` |
| `.doc` `.docx` `.txt` `.md` `.ppt` `.pptx` | `Documentos` |
| `.xls` `.xlsx` `.csv` | `Excel` |
| `.mp4` `.mov` `.avi` | `Videos` |
| `.mp3` `.wav` | `Musica` |
| `.zip` `.rar` `.7z` | `Comprimidos` |
| `.exe` `.msi` `.dmg` | `Programas` |
| `.po` `.mo` | `i18n` |
| `.ova` | `MaquinaVirtual` |
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
