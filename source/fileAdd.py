import time
import os

from source import booleans
from source import fileCopy
from source import clearScreen

wotbDir = "C:/Program Files (x86)/Steam/steamapps/common/World of Tanks Blitz/"
cDir = "C:/"
folderSize = 0
maxSize = 0
byteType = ["PiB", "TiB", "GiB", "MiB", "KiB", "B"]

#check mod directory
def parseDir(dir):
    clearScreen.clearScr()

    print("Added folder, checking if location exists...")
    _modPathDir = dir
    print(" -> " + _modPathDir)
    if (os.path.exists(_modPathDir)):
        booleans.folderExists = True
    elif (os.path.exists(_modPathDir) == False):
        booleans.folderExists = False
    
    time.sleep(3)

    if (booleans.folderExists):
        confirmDataSize(_modPathDir)
    elif (booleans.folderExists == False):
        folderDoesNotExist(_modPathDir)

def confirmDataSize(dir):
    clearScreen.clearScr()

    print("Location exists!")
    print("Checking folder size...")
    _modPathDir = dir
    print(" -> " + _modPathDir)

    maxSize += os.path.getsize(cDir)
    folderSize += os.path.getsize(_modPathDir)

    time.sleep(3)

    if (folderSize < maxSize):
        finalize(_modPathDir)
    else:
        folderSize = 0
        maxSize = 0
        notEnoughSpace(_modPathDir)


def notEnoughSpace(dir):
    clearScreen.clearScr()

    print("ERROR\n")
    print("There is not enough space in the '" + cDir + "' drive!")

    _addDir()


def finalize(dir):
    _modPathDir = dir
    folderExists(_modPathDir)

#add mod directory
def _addDir():
    clearScreen.clearScr()

    print("Add mod folder below;")
    _modDir = input("")

    parseDir(_modDir)

#if folder doesnt exist
def folderDoesNotExist(dir):
    clearScreen.clearScr()

    print("ERROR \n")
    print("The folder, '" + dir + "' does not exist...")
    print("Please make sure to assign a valid directory!")

    time.sleep(3)

    _addDir()

#if folder does exist
def folderExists(dir):
    clearScreen.clearScr()

    print("SUCCES \n")
    print ("Do you want to copy the files from the folder, '" + dir + "' to '" + wotbDir + "'?")
    print("Y, N \n")

    _option = input(">> ")

    if (_option == ">> Y"):
        fileCopy.copyFiles(dir)
        booleans.atAddingDir = False
        booleans.atRunning = True
    elif (_option == ">> N"):
        _addDir()
