from subprocess import call
import sys

def callfile(path):
    try:
        call(path, 1000)
    except(FileNotFoundError):
        print(path + " was not found, make sure to include directory path")

"""Calls files/exes supplied as arguments given in console, and displays any stdout information to command line."""
if __name__ == "__main__":
    if len(sys.argv) < 2:
        try:
            callfile(str(input('Enter the file\'s filepath to execute:\n ')))
        except:
            print("Bad input")
    else:
        callfile(sys.argv[1])
        
else:
    raise SystemExit
