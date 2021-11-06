import pyautogui as pt
from time import sleep
import pyperclip
import random
import os
os.startfile("whatsapp:")

sleep(10)
pos=pt.locateOnScreen("new.PNG",confidence=0.6)
x1=pos[0]
y1=pos[1]
pt.moveTo(x1,y1)
pt.click()
sleep(4)
position1=pt.locateOnScreen("smiley_paperclip.png",confidence=0.6)
x=position1[0]
y=position1[1]
pt.moveTo(x,y)

def getmessage():
	global x,y
        
	position=pt.locateOnScreen("smiley_paperclip.PNG",confidence=0.6)
	x=position[0]
	y=position[1]
	pt.moveTo(x,y)
	pt.moveTo(x+110,y-70)
	pt.tripleClick()
	pt.rightClick()
	pt.moveRel(12,10)
	pt.click()
	message=pyperclip.paste()
	print("Message received ",message)
	return(message)

def postmessage(message):
        global x,y
        position=pt.locateOnScreen("smiley_paperclip.PNG",confidence=0.6)
        x=position[0]
        y=position[1]
        if(message=="Hi" or message=="hi"):
                pt.moveTo(x+200,y+20)
                pt.click()
                pt.typewrite("hi",interval=0.01)
                pt.typewrite("\n")
        

postmessage(getmessage())
