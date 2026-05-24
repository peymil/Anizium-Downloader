import sys
import os

if getattr(sys, 'frozen', False):
    os.environ['PLAYWRIGHT_BROWSERS_PATH'] = os.path.join(sys._MEIPASS, 'ms-playwright')

C = "\033[96m"
Y = "\033[93m"
R = "\033[0m"
B = "\033[1m"

def usage():
    print(f"{B}{C}Anizium Downloader{R}")
    print(f"  {Y}anizium video{R}     – video indir")
    print(f"  {Y}anizium subtitle{R}  – altyazı indir")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    cmd = sys.argv[1].lower()

    if cmd == "video":
        from downloader import main
        main()
    elif cmd == "subtitle":
        from subtitle_downloader import main
        main()
    else:
        usage()
