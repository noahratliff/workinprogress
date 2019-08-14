import sys, os
import pyautogui

def picFind(image):
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'pyautoproj' + "\\"  + image)
    return(filename)

def locClick(target):
    startlocation = pyautogui.locateOnScreen(target)
    startx, starty = pyautogui.center(startlocation)
    pyautogui.click(startx, starty)

def clickFind(pic):
    locClick(picFind(pic))

clickFind('start.png')
    
