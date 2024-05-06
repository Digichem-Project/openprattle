# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path
sys.path.insert(0,str(Path("./").resolve()))

from base import binaries, datas

script = "../../bin/oprattle"
prog_name = "oprattle.exe"
package_name = "CentOS-7.9"

a = Analysis([script],
     pathex=["../../"],
     binaries=binaries,
     datas=datas,
     hiddenimports=[],
     hookspath=[],
     runtime_hooks=[],
     excludes=[],
     win_no_prefer_redirects=False,
     win_private_assemblies=False,
     cipher=None,
     noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data,
     cipher=None
)

exe = EXE(pyz,
     a.scripts,
     [],
     exclude_binaries=True,
     name=prog_name,
     debug=False,
     bootloader_ignore_signals=False,
     strip=False,
     upx=True,
     console=True
)

import openprattle
coll = COLLECT(exe,
     a.binaries,
     a.zipfiles,
     a.datas,
     strip=False,
     upx=True,
     upx_exclude=[],
     name="{}.{}.{}".format("openprattle", openprattle.__version__, package_name)
)
