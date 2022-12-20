from selenium import webdriver

from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(executable_path ="chromedriver.exe")
driver.maximize_window()
driver.get("https://facebook.com/")
sleep(3)
driver.find_element(By.ID, "email").send_keys("ravali@gmail.com")
sleep(4)
driver.find_element(By.NAME, "pass").send_keys("123456")
sleep(5)
driver.find_element(By.NAME, "login").click()
sleep
driver.close()
driver.quit()













