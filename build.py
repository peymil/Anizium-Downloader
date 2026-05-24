import subprocess
import sys


def run(cmd):
    print("$", " ".join(str(c) for c in cmd))
    subprocess.run(cmd, check=True)


def main():
    run(["playwright", "install", "chromium-headless-shell"])
    run([sys.executable, "-m", "PyInstaller", "anizium.spec", "--noconfirm"])
    print("\nBuild tamamlandi -> dist/anizium/anizium.exe")


if __name__ == "__main__":
    main()
