import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import config
from config import catalystKey, catalystUser, uciNetPass
import time
from datetime import date
from open import vpnLogin


today = date.today()
os.chdir('/Users/Tatiana/Desktop/CODE/Catalyst-Roster-Automation')
chrome_options = webdriver.ChromeOptions()
#prefs = {'download.default_directory' : f'/Users/Tatiana/Desktop/CODE/Catalyst-Roster-Automation/{today}'}
#chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(driver, 20)



def catalystLogin():
    driver.get('https://catalyst.merage.uci.edu/')
    loginButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#box > div > a')))
    loginButton.click()

    pyautogui.write(config.catalystUser)
    pyautogui.press('tab')
    pyautogui.write(config.catalystKey)
    pyautogui.press('enter')
    regSystem = driver.find_element_by_css_selector('#ctl00_ctl46_g_d842051c_2484_466b_9f2b_edb043f8244c_ctl00_lbtnEventRegistration_Enabled')
    regSystem.click()
    pyautogui.write(config.catalystUser)
    pyautogui.press('tab')
    pyautogui.write(config.uciNetPass)
    pyautogui.press('enter')
    reportsButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tabs-horizontal > ul > li:nth-child(2) > a")))
    reportsButton.click()
    reportLinksList = driver.find_elements_by_link_text('View Report')
    reportLinks = []
    for link in reportLinksList:
        reportLinks.append(link.get_attribute('href'))
    for link in reportLinks:
        driver.execute_script(link)
        print('I have successfully opened a program page.')
        downloadButton= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_ContentPlaceHolderMain_btnExcelTop")))
        downloadButton.click()
        driver.back()
    driver.close()

if (vpnLogin() == True):
    catalystLogin()