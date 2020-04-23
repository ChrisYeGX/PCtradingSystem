# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:45:07 2020

发送交易信息

@author: 11260
"""
#######
#
# tool to get the point of mouse
###########
#import os,time
#import pyautogui as pag
#try:
#    while True:
#            x,y = pag.position() #返回鼠标的坐标
#            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
#            print (posStr)#打印坐标
#            time.sleep(2)
#            os.system('cls')#清楚屏幕
#except  KeyboardInterrupt:
#    print ('end')
#    
#from pymouse import * 
#m=PyMouse()
#m.move(1361, 195)
#m.click(1361, 195)
#from event import *
#from settings import *
from time import sleep, time
from random import choice
from random import random
import pyautogui as pag
import win32api
import win32clipboard as wincld
import win32con
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import os
#开启程序后几秒开始发送信息
WAIT_TIME = 5
#连续发送多少秒后停止发送
AUTO_SAY_HELLO_TIME = 10
#是否使用表情包, 0为否，1为是(需要把图片放入images文件夹下)
USE_IMAGE = 0
#每次发送信息后间隔多久发送第二次
DELAY_TIME = 1
#要自动发送的话
TRADE_INFO = [
    'BUY,OPEN,3099',
    'SELL,OPEN,301121'
]
msg="BUY OPEN 3011 \nSELL CLOSE 3031"
#软件能否支持回车键发送消息，0为否，1为是
USE_ENTER = 1
def set_text():
    if not USE_IMAGE:
        wincld.OpenClipboard()
        wincld.EmptyClipboard()
        #wincld.SetClipboardData(win32con.CF_UNICODETEXT, choice(TRADE_INFO))
        wincld.SetClipboardData(win32con.CF_UNICODETEXT, msg)
        wincld.CloseClipboard()
    else:
        all_file(os.path.dirname(os.path.realpath(__file__))+'\\images')
        img_path = choice(filepaths)
        img = Image.open(img_path)
        output = BytesIO()
        img.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        wincld.OpenClipboard()
        wincld.EmptyClipboard()
        wincld.SetClipboardData(win32con.CF_DIB, data)
        wincld.CloseClipboard()

def get_mouse_position():
    x, y = pag.position()
    return x, y

def mouse_click(x, y):
    mouse = PyMouse()
    mouse.click(x, y)

def tap_enter():
    kb = PyKeyboard()
    kb.tap_key(kb.enter_key)

def send_text(msg):
    kb = PyKeyboard()
    kb.type_string(msg)

def ctrl_v():
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(86,0,0,0)  #v键位码是86
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
cmd1 = 'cd C:\Program Files (x86)\Tencent\WeChat'
cmd2='start WeChat.exe'
sleep(3)
#########微信对话框的位置
x1, y1 = 990,786
mouse_click(x, y)
set_text()
ctrl_v()
tap_enter()
###### 关闭窗口
mouse_click(1361, 195)

