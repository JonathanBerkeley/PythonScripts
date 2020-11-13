#Developed for fun by Jonathan Berkeley - 2020
#https://opensource.org/licenses/MIT
#Shared under MIT license. I am not liable for any claims or damages. Read MIT license for more details.
#Please give credit if you use/repurpose this source :)

import sys
import time
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
    
    for arg in sys.argv[2:]:
        for process in psutil.process_iter():
            try:
                if arg.lower() in process.name().lower():
                    kill_process(kill_timer, process)
            except:
                pass

def kill_process(wait, target_proc):
    time.sleep(wait)
    target_proc.kill()

if __name__ == "__main__":
    main()