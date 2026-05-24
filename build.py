import subprocess
import sys


def run(cmd):
    print("$", " ".join(str(c) for c in cmd))
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    run(["playwright", "install", "chromium-headless-shell"])
    run([sys.executable, "-m", "PyInstaller", "anizium.spec", "--noconfirm"])
    print("\nBuild tamamlandı → dist/anizium/anizium.exe")
