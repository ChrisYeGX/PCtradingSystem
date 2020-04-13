# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:47:03 2020

@author: 11260
"""

from pymouse import *
from pykeyboard import PyKeyboard
m = PyMouse()
#m.move(1744, 15)
m.click(1756, 17)
#import os,time
import pyautogui as pag
try:
    while True:
            print ("Press Ctrl-C to end")
            x,y = pag.position() #返回鼠标的坐标
            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
            print (posStr)#打印坐标
            time.sleep(0.2)
            os.system('cls')#清楚屏幕
except  KeyboardInterrupt:
    print ('end....')