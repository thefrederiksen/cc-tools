# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec file for cc_gmail."""

from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Get the spec file directory
spec_path = Path(SPECPATH)

# Collect all rich submodules to handle dynamic unicode imports
rich_imports = collect_submodules('rich')

a = Analysis(
    [str(spec_path / 'main.py')],
    pathex=[SPECPATH, str(spec_path / 'src')],
    binaries=[],
    datas=[],
    hiddenimports=[
        'typer',
        'google.auth',
        'google.auth.transport.requests',
        'google.oauth2.credentials',
        'google_auth_oauthlib.flow',
        'googleapiclient.discovery',
        'httplib2',
        'cli',
        'auth',
        'gmail_api',
        'utils',
    ] + rich_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='cc_gmail',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
