# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

mydatas = [('./aspose-cells-23.1.jar', '.'),
				('./bcprov-jdk15on-160.jar', '.'),
				('./bcpkix-jdk15on-1.60.jar', '.'),
				('./JavaClassBridge.jar', '.') ]

a = Analysis(
    ['example.py'],
    pathex=[],
    binaries=[],
    datas=mydatas,
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='example',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='example',
)
