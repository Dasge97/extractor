import os
import tkinter as tk
from tkinter import filedialog, messagebox
import datetime
import pyperclip

# === CONFIGURACIÓN GLOBAL ===
CARPETAS_EXCLUIDAS = {
    "node_modules", "dist", "build", "__pycache__", ".git",
    ".idea", ".vscode", "venv", "env", ".next", ".cache"
}

EXTENSIONES_EXCLUIDAS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
    ".webp", ".pdf", ".zip", ".rar", ".7z",
    ".ttf", ".otf", ".woff", ".woff2",
    ".mp4", ".mp3", ".avi", ".mov", ".exe", ".dll"
}

# === FUNCIÓN: detectar tipo de proyecto ===
def detectar_tipo_proyecto(ruta):
    if os.path.exists(os.path.join(ruta, "docker-compose.yml")):
        return "Docker / Traefik"
    if os.path.exists(os.path.join(ruta, "package.json")):
        return "Node.js"
    if os.path.exists(os.path.join(ruta, "index.php")):
        return "PHP"
    if os.path.exists(os.path.join(ruta, "manage.py")):
        return "Python (Django)"
    return "Desconocido"

# === FUNCIÓN: generar árbol de carpetas ===
def generar_estructura(ruta):
    estructura = ["\n\n---\n## 🗂️ Estructura del proyecto\n"]
    for root, dirs, files in os.walk(ruta):
        dirs[:] = [d for d in dirs if d not in CARPETAS_EXCLUIDAS]
        nivel = root.replace(ruta, "").count(os.sep)
        indent = " " * 2 * nivel
        estructura.append(f"{indent}- 📁 {os.path.basename(root)}/")
        for nombre in files:
            extension = os.path.splitext(nombre)[1].lower()
            if extension not in EXTENSIONES_EXCLUIDAS:
                estructura.append(f"{indent}  - 📄 {nombre}")
    return "\n".join(estructura)

# === FUNCIÓN PRINCIPAL ===
def extraer_contenido(ruta_directorio, salida="contenido_proyecto.txt"):
    total_archivos = 0
    total_saltados = 0
    tipo = detectar_tipo_proyecto(ruta_directorio)
    estructura = generar_estructura(ruta_directorio)
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(salida, "w", encoding="utf-8") as f:
        # CABECERA
        f.write(f"# 📦 CONTENIDO DE PROYECTO — dedaniel.com\n")
        f.write(f"**Ruta:** {ruta_directorio}\n")
        f.write(f"**Fecha:** {fecha}\n")
        f.write(f"**Tipo de proyecto detectado:** {tipo}\n")
        f.write(f"{estructura}\n\n---\n")

        # RECORRER ARCHIVOS
        for root, dirs, files in os.walk(ruta_directorio):
            dirs[:] = [d for d in dirs if d not in CARPETAS_EXCLUIDAS]
            for archivo in files:
                extension = os.path.splitext(archivo)[1].lower()
                if extension in EXTENSIONES_EXCLUIDAS:
                    total_saltados += 1
                    continue

                ruta_completa = os.path.join(root, archivo)
                try:
                    with open(ruta_completa, "r", encoding="utf-8") as archivo_actual:
                        contenido = archivo_actual.read()
                    total_archivos += 1
                except Exception as e:
                    contenido = f"[No se pudo leer el archivo: {e}]"
                    total_saltados += 1

                # BLOQUE FORMATEADO EN MARKDOWN
                f.write(f"\n\n## 📄 {ruta_completa}\n\n")
                bloque = extension[1:] if extension else ""
                f.write(f"```{bloque}\n{contenido}\n```\n")

        # RESUMEN FINAL
        f.write(f"\n\n---\n## 📊 Resumen del proyecto\n")
        f.write(f"- Archivos procesados: {total_archivos}\n")
        f.write(f"- Archivos omitidos: {total_saltados}\n")
        f.write(f"- Tipo de proyecto: {tipo}\n")

    # COPIAR AL PORTAPAPELES
    try:
        with open(salida, "r", encoding="utf-8") as archivo:
            pyperclip.copy(archivo.read())
    except Exception:
        pass

    return total_archivos, total_saltados, salida, tipo

# === INTERFAZ GRÁFICA ===
def seleccionar_carpeta():
    carpeta = filedialog.askdirectory(title="Selecciona la carpeta del proyecto")
    if not carpeta:
        return

    lbl_estado.config(text="Procesando, espera un momento...")
    root.update()

    try:
        procesados, omitidos, archivo, tipo = extraer_contenido(carpeta)
        messagebox.showinfo(
            "✅ Listo",
            f"Proyecto detectado: {tipo}\n\n"
            f"Archivo generado: {archivo}\n\n"
            f"Archivos procesados: {procesados}\n"
            f"Archivos omitidos: {omitidos}\n\n"
            f"📋 El contenido completo se ha copiado al portapapeles."
        )
        lbl_estado.config(text=f"Completado: {archivo}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
        lbl_estado.config(text="Error durante la extracción.")

# === UI ===
root = tk.Tk()
root.title("Extractor IA dedaniel.com v2.0")
root.geometry("450x230")
root.resizable(False, False)

titulo = tk.Label(root, text="🧠 Extractor IA dedaniel.com", font=("Segoe UI", 14, "bold"))
titulo.pack(pady=10)

descripcion = tk.Label(
    root,
    text="Genera un archivo Markdown con todo el código relevante\n"
         "de tu proyecto, listo para compartir con ChatGPT u otra IA.",
    justify="center"
)
descripcion.pack(pady=5)

btn_seleccionar = tk.Button(root, text="📂 Seleccionar carpeta", command=seleccionar_carpeta, font=("Segoe UI", 11))
btn_seleccionar.pack(pady=10)

lbl_estado = tk.Label(root, text="", fg="gray")
lbl_estado.pack(pady=5)

footer = tk.Label(root, text="v2.0 — dedaniel.com", font=("Segoe UI", 8), fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()
