# -*- mode: python ; coding: utf-8 -*-
"""
NovaAgent - Configuración de PyInstaller.
Se ejecuta automáticamente por GitHub Actions.
"""

import sys
from pathlib import Path

PROJECT_DIR = Path(SPECPATH).parent
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[str(PROJECT_DIR)],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('docs', 'docs'),
        ('assets', 'assets'),
    ],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtNetwork',
        'llama_cpp',
        'novaagent',
        'novaagent.engine',
        'novaagent.engine.llm_engine',
        'novaagent.engine.model_downloader',
        'novaagent.ui',
        'novaagent.ui.desktop_app',
        'novaagent.core',
        'novaagent.utils',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter', 'unittest', 'pytest', 'IPython',
        'jupyter', 'notebook',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NovaAgent',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(PROJECT_DIR / 'assets' / 'icon.ico'),
)
