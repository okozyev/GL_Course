from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_IE():
    #   driver = webdriver.Ie("C:\\_all_lib\\Drivers\\IEDriverServer.exe")
    driver = webdriver.Ie()
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("lololo")
    driver.find_element_by_name("btnG").click()
    driver.maximize_window()
    sleep(2)
    #   WebDriverWait(driver, 15)
    driver.quit()
