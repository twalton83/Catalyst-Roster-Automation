import os
import pyautogui
import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def vpnLogin():
    os.system("open" + r" /Applications/Cisco\ AnyConnect\ Secure\ Mobility\ Client.app")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(config.uciNetPass)
    pyautogui.press('enter')
    pyautogui.write(config.uciNetPass)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(config.uciNetPass)
    pyautogui.press('enter')
    pyautogui.press('enter')
    return True
    
