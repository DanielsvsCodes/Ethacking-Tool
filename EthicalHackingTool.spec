# EthicalHackingTool.spec

block_cipher = None

a = Analysis(
    ['EthackingApp/main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('EthackingApp/categories', 'categories'),
        ('EthackingApp/modules', 'modules'),
        ('EthackingApp/resources', 'resources'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='EthicalHackingTool',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='EthicalHackingTool',
)
