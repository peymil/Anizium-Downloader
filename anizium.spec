import os
import sys

import playwright as _pw

_playwright_dir = os.path.dirname(_pw.__file__)
_driver_src = os.path.join(_playwright_dir, 'driver')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (_driver_src, 'playwright/driver'),
    ],
    hiddenimports=[
        'greenlet',
        'playwright',
        'playwright.sync_api',
        'playwright._impl._driver',
        'playwright._impl._sync_base',
        'playwright._impl._api_structures',
        'playwright._impl._api_types',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    exclude_binaries=False,
    name='anizium',
    debug=False,
    strip=False,
    upx=True,
    console=True,
)
