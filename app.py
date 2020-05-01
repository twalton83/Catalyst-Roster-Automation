import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import config
from config import catalystKey, catalystUser, uciNetPass
import cv2


os.chdir('/Users/Tatiana/Desktop/CODE/Catalyst-Roster-Automation')


driver = webdriver.Chrome()

driver.get('https://catalyst.merage.uci.edu/')



loginButton= driver.find_element_by_css_selector('#box > div > a')

loginButton.click()

pyautogui.write(config.catalystUser, interval=.03)
pyautogui.press('tab')
pyautogui.write(config.catalystKey, interval=.03)
pyautogui.press('enter')


regSystem = driver.find_element_by_css_selector('#ctl00_ctl46_g_d842051c_2484_466b_9f2b_edb043f8244c_ctl00_lbtnEventRegistration_Enabled')

regSystem.click()

pyautogui.write(config.catalystUser, interval = .03)
pyautogui.press('tab')
pyautogui.write(config.uciNetPass, interval=.03)
pyautogui.press('enter')

wait = WebDriverWait(driver, 20)

reportsButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tabs-horizontal > ul > li:nth-child(2) > a")))

reportsButton.click()

reportLinks = driver.find_elements_by_link_text('View Report')

reportLinks[0].click()
downloadButton = pyautogui.locateCenterOnScreen('/Users/Tatiana/Desktop/CODE/Catalyst-Roster-Automation/Screenshots/saveAs.png', confidence =.7)
pyautogui.click()

