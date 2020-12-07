import sys
import mouse
import time

def main():
    if len(sys.argv) > 1:
        interval = int(sys.argv[1])
    else:
        interval = 7
    while True:
        try:
            clicker_code(interval)
        except KeyboardInterrupt:
            print("-- Exitting --")
            sys.exit(0)

def clicker_code(interval):
    mouse.click()
    time.sleep(interval)

if __name__ == "__main__":
    main()