# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['D:/python/tool/source/auto_ytb5/auto_ytb5/main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/python/tool/source/auto_ytb5/auto_ytb5/bot_driver.py', '.'), ('D:/python/tool/source/auto_ytb5/auto_ytb5/database_driver.py', '.'), ('D:/python/tool/source/auto_ytb5/auto_ytb5/display_driver.py', '.'), ('D:/python/tool/source/auto_ytb5/auto_ytb5/ytb_bot.py', '.'), ('D:/python/tool/source/auto_ytb5/auto_ytb5/ytb_bot_display.py', '.')],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
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
)
