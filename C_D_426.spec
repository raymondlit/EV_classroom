# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('yolov8n.pt', '.'), ('E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages/ultralytics/cfg/*.yaml', 'ultralytics/cfg'), ('E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages/cv2/*.*', 'cv2'), ('deepface_weights/*', 'deepface_weights')]
binaries = []
hiddenimports = ['deepface.basemodels', 'deepface.modules', 'tf_keras', 'keras.src.backend', 'ultralytics.models.yolo', 'deepface.extendedmodels', 'deepface.models.facial_recognition', 'torchvision.models', 'tensorflow.keras.layers']
tmp_ret = collect_all('cv2')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['C_D_426.py'],
    pathex=['E:/2025study/2025Python/code/crowed_density/np_fix_env/Lib/site-packages'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='C_D_426',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['visio45.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='C_D_426',
)
