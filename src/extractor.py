#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor v1.0 — Herramienta de documentación automática para proyectos
Autor: Daniel  |  Ecosistema: dedaniel.com
------------------------------------------------------------
Lee todos los archivos de una carpeta (recursivamente),
detecta el tipo de proyecto y genera un único archivo .txt y .md
con el contenido completo y un resumen estructurado.
------------------------------------------------------------
"""

import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip

# ========= CONFIGURACIÓN GENERAL ========= #
EXCLUDE_FOLDERS = [
    "__pycache__", "node_modules", "dist", "venv", ".git",
    ".idea", ".vscode", "build", ".next", ".cache", "env"
]
VALID_EXTENSIONS = [
    ".py", ".js", ".html", ".css", ".sql", ".json", ".yml",
    ".yaml", ".php", ".xml", ".md", ".txt", ".conf", ".env"
]
OUTPUT_FILENAME = "extractor_output"
# ========================================= #


def detect_project_type(folder_path: str) -> str:
    """Detecta el tipo de proyecto en base a los archivos encontrados."""
    indicators = {
        "Node.js": ["package.json", "server.js"],
        "Python / Flask": ["app.py"],
        "Python / Django": ["manage.py"],
        "PHP / Laravel": ["artisan", "composer.json"],
        "React / Frontend": ["vite.config.js", "react"],
        "Docker": ["Dockerfile", "docker-compose.yml"],
        "HTML / Static": ["index.html"]
    }

    for project, markers in indicators.items():
        if any(os.path.exists(os.path.join(folder_path, m)) for m in markers):
            return project
    return "Proyecto genérico"


def read_file_content(file_path: str) -> str:
    """Lee un archivo y devuelve su contenido."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"⚠️ Error al leer {file_path}: {e}\n"


def generate_extraction(folder_path: str) -> str:
    """Recorre la carpeta, lee archivos válidos y construye el texto final."""
    project_type = detect_project_type(folder_path)
    output_lines = []

    output_lines.append("# 🧩 EXTRACTOR v1.0")
    output_lines.append(f"**Ruta analizada:** {folder_path}")
    output_lines.append(f"**Tipo de proyecto detectado:** {project_type}")
    output_lines.append(f"**Fecha:** {time.strftime('%Y-%m-%d %H:%M:%S')}")
    output_lines.append("\n---\n")

    total_files = 0
    output_lines.append("## 🗂️ Estructura del proyecto\n")

    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_FOLDERS]
        depth = root.replace(folder_path, "").count(os.sep)
        indent = "  " * depth
        folder_name = os.path.basename(root)
        output_lines.append(f"{indent}- 📁 {folder_name}/")

        for file in files:
            if any(file.endswith(ext) for ext in VALID_EXTENSIONS):
                total_files += 1
                file_path = os.path.join(root, file)
                output_lines.append(f"{indent}  - 📄 {file}")

    output_lines.append("\n---\n## 📦 Contenido de archivos\n")

    processed = 0
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_FOLDERS]
        for file in files:
            if any(file.endswith(ext) for ext in VALID_EXTENSIONS):
                processed += 1
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, folder_path)
                output_lines.append(f"\n### 📄 {rel_path}\n```")
                output_lines.append(read_file_content(file_path))
                output_lines.append("```\n")

    output_lines.append("---\n")
    output_lines.append("## 🧾 Resumen final")
    output_lines.append(f"- Archivos procesados: **{processed}**")
    output_lines.append(f"- Tipo de proyecto: **{project_type}**")
    output_lines.append(f"- Fecha de generación: **{time.strftime('%Y-%m-%d %H:%M:%S')}**")
    output_lines.append("\n---\n💡 *Generado automáticamente por Extractor v1.0 — dedaniel.com*")

    return "\n".join(output_lines)


def save_output(folder_path: str, content: str):
    """Guarda el contenido generado en .txt y .md"""
    txt_path = os.path.join(folder_path, f"{OUTPUT_FILENAME}.txt")
    md_path = os.path.join(folder_path, f"{OUTPUT_FILENAME}.md")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
    return txt_path, md_path


def start_extraction():
    """Inicia el flujo principal con selector de carpeta."""
    folder_path = filedialog.askdirectory(title="Selecciona la carpeta del proyecto")
    if not folder_path:
        messagebox.showinfo("Extractor", "Operación cancelada.")
        return

    start_time = time.time()
    messagebox.showinfo("Extractor", "Extrayendo contenido...\nEsto puede tardar unos segundos.")

    content = generate_extraction(folder_path)
    txt_path, md_path = save_output(folder_path, content)
    pyperclip.copy(content)

    duration = round(time.time() - start_time, 2)
    messagebox.showinfo(
        "Extracción completada ✅",
        f"Archivos generados:\n\n📄 {os.path.basename(txt_path)}\n📄 {os.path.basename(md_path)}\n\n"
        f"Copiado al portapapeles automáticamente.\nTiempo total: {duration}s"
    )


# ===== Interfaz gráfica ===== #
def build_ui():
    root = tk.Tk()
    root.title("Extractor 1.0 — dedaniel.com")
    root.geometry("480x320")
    root.configure(bg="#1e1e1e")

    tk.Label(
        root,
        text="🧠 Extractor v1.0",
        font=("Segoe UI", 16, "bold"),
        bg="#1e1e1e",
        fg="#00ffcc",
        pady=10
    ).pack()

    tk.Label(
        root,
        text="Genera documentación automática en Markdown.\n"
             "Convierte cualquier proyecto en un solo archivo legible.",
        bg="#1e1e1e",
        fg="#cccccc",
        font=("Segoe UI", 10),
        justify="center"
    ).pack(pady=10)

    tk.Button(
        root,
        text="📂 Seleccionar carpeta y generar",
        font=("Segoe UI", 12, "bold"),
        bg="#00bcd4",
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        command=start_extraction
    ).pack(pady=20)

    tk.Label(
        root,
        text="© 2025 Daniel — dedaniel.com",
        bg="#1e1e1e",
        fg="#888888",
        font=("Segoe UI", 9)
    ).pack(side="bottom", pady=10)

    root.mainloop()


if __name__ == "__main__":
    build_ui()
