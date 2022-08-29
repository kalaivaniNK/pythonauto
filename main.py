from confidential import Confidential_Data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Suman:
    url="https://www.instagram.com/"
    driver= webdriver.Firefox()

    def Instagram_login(self):
        username=Confidential_Data().insta_username
        password=Confidential_Data().insta_password
        self.driver.get(self.url)
        time.sleep(5)
        username_xpath='//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_xpath='//*[@id="loginForm"]/div/div[2]/div/label/input'
        submit_button_xpath='//*[@id="loginForm"]/div/div[3]'
        username1 = self.driver.find_element(by=By.XPATH,value=username_xpath)
        password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
        submit_button = self.driver.find_element(by=By.XPATH, value=submit_button_xpath)

        username1.send_keys(username)
        time.sleep(5)
        password1.send_keys(password)
        submit_button.click()
        time.sleep(5)
        not_now=self.driver.find_element(by=By.CLASS_NAME,value='cmbtv')
        not_now.click()
        time.sleep(5)


    def Notnow_button(self):
        not_now2_xpath='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]'
        not_now_button= self.driver.find_element(by=By.XPATH, value=not_now2_xpath)
        not_now_button.click()
        time.sleep(5)
    def profile(self):
        profile_xpath='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img'
        profile_1=self.driver.find_element(by=By.XPATH,value=profile_xpath)
        profile_1.click()
        time.sleep(3)
    def profile1(self):
        profile1_xpath='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div'
        profile=self.driver.find_element(by=By.XPATH,value=profile1_xpath)
        profile.click()
        time.sleep(5)
    def followers(self):
        foloowers_xpath='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div'
        followers=self.driver.find_element(by=By.XPATH,value=foloowers_xpath)
        followers.click()
        print(followers.text)
        time.sleep(5)

Suman().Instagram_login()
Suman().Notnow_button()
Suman().profile()
Suman().profile1()
Suman().followers()
