import random
import os
import time

from source import fileAdd
from source import renderer
from source import booleans
from source import startup

def start():
    startup._startup()

def loop():
    time.sleep(0.05)
    if booleans.atAddingDir:
        fileAdd._addDir()

    loop()

start()
loop()


