# 🧰 Extractor

![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![Python](https://img.shields.io/badge/python-3.12+-yellow)

> 🧾 *Extrae el contenido de cualquier proyecto y genera un único archivo .txt con todos sus archivos dentro.*

---

## ⚡ Descripción

**Extractor** es una herramienta simple y útil para desarrolladores, estudiantes y creadores de proyectos.  
Permite recorrer carpetas completas y **volcar todo su contenido en un solo archivo `.txt`**, facilitando la lectura, documentación o análisis de código.  

Ideal para preparar proyectos antes de compartirlos, hacer backups de contenido o generar informes para IA y revisores de código.

---

## 🚀 Características

- 📂 Selección de carpetas o rutas específicas  
- 📜 Genera un único archivo `extract.txt` con todo el contenido  
- 🔍 Filtra extensiones si se desea (ej: `.py`, `.html`, `.js`, `.sql`, etc.)  
- 💬 Indica automáticamente nombre de archivo y ruta  
- 🧠 Perfecto para análisis con IA o documentación rápida  
- 💾 Versión `.exe` disponible (no requiere instalación)

---

## 🧠 Ejemplo de salida

=== Archivo: src/server.js ===
const express = require('express');
const app = express();

=== Archivo: db/init.sql ===
CREATE TABLE users (...);


---

## 💾 Descargar versión compilada (.exe)

[![Descargar .EXE](https://img.shields.io/badge/⬇️%20Descargar%20Extractor.exe-0078D7?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/TU_USUARIO/extractor/releases/latest/download/Extractor.exe)

> No requiere instalación.  
> Solo ejecútalo, elige la carpeta y genera tu archivo `extract.txt` con un clic.

---

## 🧰 Ejecutar desde el código fuente

# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/extractor.git
cd extractor/src

# 2. (Opcional) Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python extractor.py

🧱 Estructura del proyecto
css
Copiar código
extractor/
├─ src/
│   ├─ extractor.py
│   └─ requirements.txt
├─ dist/
│   └─ Extractor.exe
├─ README.md
├─ LICENSE
└─ .gitignore

---

🪄 Uso típico
Ejecuta Extractor.

Elige una carpeta raíz.

Espera unos segundos mientras analiza los archivos.

Obtendrás un archivo extract.txt con el contenido completo y ordenado.

Ideal para entregar prácticas, analizar código con IA o generar documentación técnica sin perder contexto.

🧾 Release oficial v1.0
🎉 Versión inicial estable

📁 Soporte para lectura recursiva de carpetas

⚙️ Salida organizada por nombre de archivo

🚀 Versión .exe incluida para Windows

🪪 Licencia
Distribuido bajo licencia MIT — libre para uso personal o profesional.

💬 Autor
Desarrollado por Daniel 🧑‍💻
Proyecto abierto del ecosistema dedaniel.com

⭐ Si esta herramienta te resulta útil, deja una estrella en el repositorio :)

yaml
Copiar código

---

## 🧠 Descripción corta para el repositorio de GitHub

> Extrae todo el contenido de un proyecto y genera un `.txt` con cada archivo.  
> Perfecto para documentar, analizar o compartir código completo.

---

## 💬 Descripción larga ("About" del repo)

> **Extractor** es una herramienta ligera para desarrolladores y estudiantes que necesitan revisar o compartir el contenido completo de un proyecto.  
> Recorre carpetas y genera un único archivo `.txt` con todos los archivos dentro, identificando sus rutas y nombres.  
>  
> Ideal para documentar proyectos, hacer backups o preparar código para análisis automático (por ejemplo, con IA o revisores externos).

---

¿Quieres que te prepare también la **nota de release oficial v1.0** (texto para pegar en GitHub cuando subas el `.exe`)?  
Así la subes con el mismo formato profesional que SmartInjector.
