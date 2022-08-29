from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from datadriven_testing import XLutils

driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()


file = "C:\\Users\\dell\\excel auto.xlsx"

rows = XLutils.getRowCount(file,"Sheet1")
#reading from excel
for r in range(2,rows+1):
    pric = XLutils.readData(file,"Sheet1",r,1)
    ratofi = XLutils.readData(file, "Sheet1", r, 2)
    per1 = XLutils.readData(file,"Sheet1",r,3)
    per2 = XLutils.readData(file, "Sheet1", r, 4)
    fre = XLutils.readData(file, "Sheet1", r, 5)
    exp_matv = XLutils.readData(file, "Sheet1", r, 6)

#passing data to application)
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(ratofi)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    perioddrp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)
    friqudrp = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    friqudrp.select_by_visible_text(fre)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_mvalue = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
#valitation
    if float(exp_matv) == float(act_mvalue):
        print("test passed")
        XLutils.writeData(file,"Sheet1",r,8,"Passed")
        XLutils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XLutils.writeData(file,"Sheet1",r,8,"Failed")
        XLutils.fillRedColor(file,"Sheet1",r,8)
    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(2)
driver.close()