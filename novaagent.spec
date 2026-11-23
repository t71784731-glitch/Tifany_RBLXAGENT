# -*- mode: python ; coding: utf-8 -*-
# Spec blindado: no exige carpetas, incluye llama_cpp y novaagent si o si
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_all, collect_submodules

PROJECT_DIR = Path(SPECPATH).parent
block_cipher = None

# Motor llama_cpp con sus DLLs nativas
datas_llama, binaries_llama, hiddenimports_llama = collect_all('llama_cpp')

# Solo incluir carpetas que existan realmente
datas = list(datas_llama)
for folder in ['config', 'docs', 'assets']:
    if (PROJECT_DIR / folder).is_dir():
        datas.append((folder, folder))

# Incluir el paquete novaagent como datos (doble via de seguridad)
if (PROJECT_DIR / 'novaagent').is_dir():
    datas.append(('novaagent', 'novaagent'))

# Registrar todos los submodulos de novaagent
try:
    hidden_nova = collect_submodules('novaagent')
except Exception:
    hidden_nova = []

icon_path = PROJECT_DIR / 'assets' / 'icon.ico'
icon_value = str(icon_path) if icon_path.exists() else None

a = Analysis(
    ['main.py'],
    pathex=[str(PROJECT_DIR)],
    binaries=list(binaries_llama),
    datas=datas,
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
    ] + list(hiddenimports_llama) + list(hidden_nova),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'unittest', 'pytest', 'IPython', 'jupyter', 'notebook'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='NovaAgent',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_value,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='NovaAgent',
)
