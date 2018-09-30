#Darian Marvel, 9/29/2018, learning Python
#This program counts the number of lines of code in all source files
#that are put into the automatically created 'PRG' folder

#Create the folder yourself, or launch the program to create the folder
#Put source files into folder (program won't search subfolders)
#Run

import os
from os import walk

import sys, time

def log(a):
    with open("Log.txt","a") as f:
        #print("[LOGGER] Logging \"" + a + "\"")
        print(a)
        f.write(a + "\n")

def count(a):
    #print("Counting " + a)
    count = 0;
    with open(a, "r") as file:
        for line in file:
            #log(line)
            count = count + 1
    #print(count)
    return count

log("Program launching...")

path = r"PRG"

log("Ensuring folder exists...")

if not os.path.exists(path):
    log("Creating folder...")
    os.makedirs(path)
    log("Folder created")
    log("Place source files in folder, re-launch program")
    sys.exit()

log("Finding files in folder...")

files = []
dirs = []
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    dirs.extend(dirnames)

#for name in dirs:
    #log("DIR: " + name)

fileCount = 0

for name in files:
    #log(name)
    fileCount = fileCount + 1
    

log( str( fileCount ) + " files")

log("Done Loading")

log("Counting...")

total = 0
for file in files:
    total = total + count(path + '/' + file)
    #time.sleep(0.05)

log("Done counting")
log( str(total) + " lines")
