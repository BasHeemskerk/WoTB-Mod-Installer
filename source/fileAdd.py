import time
import os

from source import booleans

def parseDir(dir):
    _clearScreen()

    print("Added folder, checking if location exists...")
    _modPathDir = dir
    print(" -> " + _modPathDir)
    

def _addDir():
    _clearScreen()

    print("Add mod folder below;")
    _modDir = input("")

    parseDir(_modDir)

def _clearScreen():
    os.system('cls')