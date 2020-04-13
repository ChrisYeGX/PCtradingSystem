# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:35:11 2020

@author: 11260
"""
### open the software terminal
PASSWORD='asdasd'
import os
cmd1 = 'cd /D D:\wind\V2'
cmd2='.\launcher.exe'
os.system(cmd1+'&'+cmd2)
from pymouse import *
from pykeyboard import PyKeyboard
k = PyKeyboard()
k.type_string(PASSWORD)
######选择服务器 和 用户代码一定要有记录 
k.press_key(k.enter_key)
 #which you then follow with a release of the key
k.release_key(k.enter_key)

m = PyMouse()
m.click(1195, 531)