from subprocess import call
import sys

if __name__ == "__main__":
    """Executes .exe, and displays any stdout information to command line."""
    for args in enumerate(sys.argv):
        if args[0] > 0:
            try:
                call(str(args[1]), 1000)
            except(FileNotFoundError):
                print(str(args[1]) + " was not found, make sure to include directory path")
else:
    raise SystemExit