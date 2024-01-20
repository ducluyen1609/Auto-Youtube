import os 
import random
from time import sleep

import subprocess
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class auto_bot():
    def __init__(self):
        self.xpath_database = {
            "SignIn":"//*[@id='buttons']/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]",
            "Email_Textbox":"//*[@id='identifierId']",
            "Password_Textbox":"//*[@id='password']/div[1]/div/div[1]/input",
            
            "Sub_Box": "//*[@id='subscribe-button']/ytd-subscribe-button-renderer/yt-button-shape/button",
            "Cmt_Box": "//*[@id='placeholder-area']",
            "Like_button": "//*[@id='segmented-like-button']/ytd-toggle-button-renderer/yt-button-shape/button",
            "Enter_Cmt": "//*[@id='submit-button']"
        }

        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = uc.Chrome(use_subprocess=True, options=options, service_creationflags=subprocess.CREATE_NO_WINDOW)
        self.actions = ActionChains(self.driver)

    def try_find(self, xpath, time = 10, roll = True):
        while time:
            try: button = self.driver.find_element(by= By.XPATH, value = xpath); sleep(1); return button
            except: 
                if roll: self.actions.send_keys(Keys.PAGE_DOWN).perform()
                sleep(3); time -=1
                
        return False

    def try_click(self, xpath, time = 10, roll = True):
        button = self.try_find(xpath, time = time, roll = True)
        if button: self.actions.click(button).perform(); sleep(3); return button

    def try_send(self, xpath, key):
        button = self.try_find(xpath)
        if button: self.actions.click(button).send_keys(key).send_keys(Keys.ENTER).perform(); sleep(3)

    def try_get_attri(self, xpath, attri, find = None):
        button = self.try_find(xpath)
        if not button: return False
        button = button.get_attribute(attri)

        if not find: return True
        if button.find(find) != -1: return True
        else: return False

        return button

# bot = auto_bot()

# # bot.driver.close()
# bot.driver.get("https://www.facebook.com/")

# bot.driver.delete_all_cookies()
# input()