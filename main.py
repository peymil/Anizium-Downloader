import sys
import os
import glob
import subprocess
from pathlib import Path


def _browsers_path():
    if sys.platform == 'win32':
        return Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData' / 'Local')) / 'ms-playwright'
    elif sys.platform == 'darwin':
        return Path.home() / 'Library' / 'Caches' / 'ms-playwright'
    else:
        return Path.home() / '.cache' / 'ms-playwright'


# Must be set before any Playwright import or subprocess call so both the
# install step and the browser launch resolve to the same directory.
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', str(_browsers_path()))

C = "\033[96m"
Y = "\033[93m"
R = "\033[0m"
B = "\033[1m"


def ensure_browser():
    if getattr(sys, 'frozen', False):
        node = os.path.join(sys._MEIPASS, 'playwright', 'driver',
                            'node.exe' if sys.platform == 'win32' else 'node')
        cli  = os.path.join(sys._MEIPASS, 'playwright', 'driver', 'package', 'cli.js')
        cmd  = [node, cli, 'install', 'chromium-headless-shell']
        # Always run install in the frozen exe — Playwright CLI is idempotent and exits
        # immediately if the correct revision is already present.  A glob check is not
        # enough because it can match an old revision while the bundled driver expects
        # a newer one, which causes the "Playwright was just installed" error at launch.
        subprocess.run(cmd, check=True)
    else:
        if glob.glob(str(_browsers_path() / 'chromium_headless_shell-*')):
            return
        print(f"{Y}İlk çalıştırma: tarayıcı indiriliyor, lütfen bekleyin...{R}")
        subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium-headless-shell'], check=True)


def menu():
    print(f"\n{B}{C}=== Anizium Downloader ==={R}")
    print(f"  {Y}1{R}. Video indir")
    print(f"  {Y}2{R}. Altyazı indir")
    print(f"  {Y}0{R}. Çıkış\n")
    choice = input(f"{B}Seçim: {R}").strip()
    if choice == '1':
        return 'video'
    elif choice == '2':
        return 'subtitle'
    elif choice == '0':
        sys.exit(0)
    else:
        print(f"{C}Geçersiz seçim.{R}")
        return menu()


if __name__ == "__main__":
    ensure_browser()

    if len(sys.argv) >= 2:
        cmd = sys.argv[1].lower()
    else:
        cmd = menu()

    if cmd == "video":
        from downloader import main
        main()
    elif cmd == "subtitle":
        from subtitle_downloader import main
        main()
    else:
        print(f"{C}Bilinmeyen komut: {cmd}{R}")
        sys.exit(1)

    if not sys.argv[1:]:
        input(f"\n{Y}Çıkmak için Enter'a basın...{R}")
