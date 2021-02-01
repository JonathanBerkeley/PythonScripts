import sys
import subprocess
try:
    import psutil
except ModuleNotFoundError:
    print("Required package psutil was not found, attempting automatic install")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])

try:
    import psutil
except ModuleNotFoundError:
    print("Required package 'psutil' could not be automatically installed. Install psutil and try again.")
    sys.exit(1)

def main():
    kill_these = None
    if (len(sys.argv) < 2):
        kill_these = str(input("Enter programs to kill (seperated by space):\n "))
        kill_these = kill_these.split()
    else:
        kill_these = sys.argv[1:]

    
    for arg in kill_these:
        for process in psutil.process_iter():
            try:
                if arg.lower() in process.name().lower():
                    kill_process(process)
            except:
                pass

def kill_process(target_proc):
    target_proc.kill()

main()
