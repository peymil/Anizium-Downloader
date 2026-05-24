import glob
import os
import sys
from pathlib import Path

import playwright as _pw

_playwright_dir = os.path.dirname(_pw.__file__)
_driver_src = os.path.join(_playwright_dir, 'driver')

_browsers_env = os.environ.get('PLAYWRIGHT_BROWSERS_PATH', '')
if _browsers_env:
    _ms_playwright = _browsers_env
elif sys.platform == 'win32':
    _ms_playwright = str(Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData' / 'Local')) / 'ms-playwright')
elif sys.platform == 'darwin':
    _ms_playwright = str(Path.home() / 'Library' / 'Caches' / 'ms-playwright')
else:
    _ms_playwright = str(Path.home() / '.cache' / 'ms-playwright')

_chs_dirs = glob.glob(os.path.join(_ms_playwright, 'chromium_headless_shell-*'))
if not _chs_dirs:
    raise RuntimeError(
        f"chromium-headless-shell not found in {_ms_playwright}.\n"
        "Run:  playwright install chromium-headless-shell"
    )
_chs_dir = _chs_dirs[0]
_chs_dest = os.path.join('ms-playwright', os.path.basename(_chs_dir))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (_driver_src, 'playwright/driver'),
        (_chs_dir,    _chs_dest),
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
