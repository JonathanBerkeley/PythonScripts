# Python scripts
My small utility python scripts

# killprograms.py
#### Usage: 
killprograms.py \[Time in seconds] \[Program names seperated by space]

#### Info:
Kills multiple processes with timer. First arg should be 0 for instant kill. Requires psutil.

# kps0.py
#### Usage: 
kps0.py

#### Info: 
Kills processes with no timer, takes input instead of commandline arguments. Created to be bound to a keyboard key to rapidly kill multiple programs.
Doesn't need full process name, substrings will work though becareful not to kill important processes.

# golaunch.py
#### Usage: 
golaunch.py \[Executables path]

#### Info: 
Launches executable and displays stdout to console. This was made for launching golang .exes and displaying their output.

# Re_Sort_Names
#### Usage: 
Requires txt file name sortme.txt filled with firstname lastname formatted names. Will output to output.txt lastname firstname format.
Names should be seperated by newlines.

#### Info: 
Intended for reversing name ordering.

# clicker.py
#### Info:
Very simple timed autoclicker, set interval to desired time between clicks in seconds
