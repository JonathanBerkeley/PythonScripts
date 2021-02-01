import sys
import time
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
    try:
        kill_timer = int(sys.argv[1])
    except:
        print("Missing or invalid args")
        sys.exit(2)
    if len(sys.argv) > 1:
        time.sleep(kill_timer)
    
    for arg in sys.argv[2:]:
        for process in psutil.process_iter():
            try:
                if arg.lower() in process.name().lower():
                    kill_process(process)
            except:
                pass

def kill_process(target_proc):
    target_proc.kill()

main()
