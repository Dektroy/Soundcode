import os
import winsound

def checkfile(filename):
    input = open(filename)
    line_tot = 0
    linec = 0
    for line in input:
        line_tot += 1
    freq = 0
    dur = 1
    input = open(filename)
    for line in input:
        for char in line:
            freq += 1
            if char == ' ':
                dur += 1
        linec += 1
        freq *= 10
        freq += 40
        dur *= 50
	print("Line " + str(linec) + "/" + str(line_tot) + " (f:" + str(freq) + "Hz, t=" + str(dur) + "ms)")
        winsound.Beep(freq, dur))
        freq = 0
        dur = 1


dir = os.getcwd()
filename = raw_input("File ? (Relative path) ")
checkfile(dir + "\\" + filename)

raw_input()
