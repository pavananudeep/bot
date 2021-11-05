import pyautogui as pt
from time import sleep
sleep(5)
pos=pt.locateOnScreen("new.png",confidence=0.6)
x=pos[0]
y=pos[1]
pt.moveTo(x,y)
pt.click()
