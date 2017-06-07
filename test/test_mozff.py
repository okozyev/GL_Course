from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_mozff():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("lololo")
    driver.find_element_by_name("btnG").click()
    driver.maximize_window()
    # WebDriverWait(driver, 5)
    sleep(2)
    driver.quit()
#     just rem