import sys
import mouse
import time

interval = 7
def main():
    while True:
        clicker_code()

def clicker_code():
    mouse.click()
    time.sleep(interval)

if __name__ == "__main__":
    main()