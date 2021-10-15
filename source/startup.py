import time
import os
import ctypes
import webbrowser

from source import booleans
#from colorama import Fore, Back, Style

def _startup():
    ctypes.windll.kernel32.SetConsoleTitleA('WoTB mod installer (startup)')
    print(" WoTB mod installer by BaseDEV_Official.")
    print(" A system to easily install WoTB mods to the steam folder.")
    print("\n My Social Media;")
    print(" -> Discord: https://discord.gg/3D83XsAbtF")
    print(" -> YouTube: https://www.youtube.com/channel/UCWUXak5LEFbymaQ2QLfxzYQ")
    print(" -> Github: https://github.com/BasHeemskerk")
    time.sleep(10)
    _clearScreen()

def _clearScreen():
    os.system('cls')
    booleans.atStartup = False
    booleans.atAddingDir = True
