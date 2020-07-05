#Requires txt file name sortme.txt filled with firstname lastname formatted names. Will output to output.txt lastname firstname format
#Names should be seperated by newlines

#Setup
import sys
sys.stdout = open('output.txt', "w")
inc = 0

#Resort lines
with open("sortme.txt", "r+") as file:
    for line in file:
        inc += 1
        line = line.split(" ")
        line[len(line)-1] = line[len(line)-1].replace('\n', '')
        line.append(line.pop(line.index(line[0].rstrip())))
        line[len(line)-1] += '\n'
        if (len(line) == 1):
            print(line[0], end = '')
        elif (len(line) == 2):
            print(line[0] + " " +  line[1], end = '')
        elif (len(line) == 3):
            print(line[0] + " " +  line[1] + " " + line[2], end = '')
        elif (len(line) == 4):
            print(line[0] + " " +  line[1] + " " + line[2] + " " + line[3], end = '')
