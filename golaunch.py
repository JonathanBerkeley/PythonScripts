from subprocess import call
import sys
"""Calls files/exes supplied as arguments given in console, and displays any stdout information to command line."""
if __name__ == "__main__":
    for args in enumerate(sys.argv):
        if args[0] > 0:
            try:
                call(str(args[1]), 1000)
            except(FileNotFoundError):
                print(str(args[1]) + " was not found, make sure to include directory path")
else:
    raise SystemExit
