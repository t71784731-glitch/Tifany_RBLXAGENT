#!/usr/bin/env python3
"""NovaAgent Desktop - Punto de entrada principal."""
from __future__ import annotations

import os
import sys
import logging
import traceback
import platform
from pathlib import Path
from datetime import datetime


def get_app_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent


def get_data_dir() -> Path:
    if platform.system() == "Windows":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    elif platform.system() == "Darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = Path.home() / ".local" / "share"
    data_dir = base / "NovaAgent"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_models_dir() -> Path:
    models_dir = get_data_dir() / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    return models_dir


def get_logs_dir() -> Path:
    logs_dir = get_data_dir() / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    return logs_dir


def setup_logging() -> logging.Logger:
    logs_dir = get_logs_dir()
    log_file = logs_dir / f"novaagent_{datetime.now().strftime('%Y%m%d')}.log"
    logger = logging.getLogger("novaagent")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(file_handler)
    if not getattr(sys, "frozen", False):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    return logger


def show_error_dialog(title: str, message: str) -> None:
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(title, message)
        root.destroy()
    except Exception:
        print(f"ERROR: {title}\n{message}")


def global_exception_handler(exc_type, exc_value, exc_tb):
    logger = logging.getLogger("novaagent")
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    logger.critical(f"Excepción no capturada:\n{error_msg}")
    show_error_dialog(
        "NovaAgent - Error inesperado",
        f"Se produjo un error inesperado:\n\n{str(exc_value)}\n\n"
        f"Los detalles se han guardado en: {get_logs_dir()}"
    )
    sys.__excepthook__(exc_type, exc_value, exc_tb)


def check_dependencies() -> Dict[str, Any]:
    results = {"dependencies": {}, "all_ok": True}
    required = {"PySide6": "PySide6", "llama_cpp": "llama-cpp-python"}
    for module, package in required.items():
        try:
            __import__(module)
            results["dependencies"][package] = "ok"
        except ImportError:
            results["dependencies"][package] = "missing"
            results["all_ok"] = False
    return results


def main() -> int:
    sys.excepthook = global_exception_handler
    logger = setup_logging()
    logger.info("=" * 60)
    logger.info("NovaAgent Desktop iniciándose")
    logger.info("=" * 60)
    deps = check_dependencies()
    if not deps["all_ok"]:
        missing = [k for k, v in deps["dependencies"].items() if v == "missing"]
        error_msg = "Faltan dependencias:\n\n" + "\n".join(f"  - {m}" for m in missing)
        logger.error(error_msg)
        show_error_dialog("NovaAgent - Dependencias", error_msg)
        return 1
    try:
        from novaagent.ui.desktop_app import NovaDesktopApp
        app = NovaDesktopApp(
            app_dir=str(get_app_dir()),
            data_dir=str(get_data_dir()),
            models_dir=str(get_models_dir()),
        )
        return app.run()
    except Exception as exc:
        logger.critical(f"Error al iniciar: {exc}")
        show_error_dialog("NovaAgent - Error", f"No se pudo iniciar:\n\n{exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
