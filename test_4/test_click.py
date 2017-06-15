from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_click():
    driver = webdriver.Chrome()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").click()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").submit()
    # WebDriverWait(driver, 5).until(EC.title_is("My Store"))
    sleep(5)
    search = driver.find_element_by_css_selector("span.name").click()

    # for elem in search:
    #     if elem.is_displayed():
    #         elem.click
