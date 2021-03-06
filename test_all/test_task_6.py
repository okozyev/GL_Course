from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import os

def test_task_6():
    #   Select Browser (del '#')

    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()

    driver.get("http://localhost/litecart/admin/")

    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").submit()

    driver.implicitly_wait(5)

    #selecting tab
    driver.find_element_by_xpath("//a[contains(., 'Catalog')]").click()
    driver.find_element_by_xpath("//a[contains(., ' New Product')]").click()

    # filling fields
    driver.find_element_by_xpath("//label[contains(., ' Enabled')]").click()
    driver.find_element_by_xpath("//label[contains(., ' Unisex')]").click()

    driver.find_element_by_xpath("//input[@name='date_valid_from']").send_keys("20000101")
    driver.find_element_by_xpath("//input[@name='date_valid_to']").send_keys("20200101")

    driver.find_element_by_xpath("//input[@name='code']").send_keys("005")
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys("cat_carrier")
    driver.find_element_by_xpath("//input[@name='sku']").send_keys("500")
    driver.find_element_by_xpath("//input[@name='gtin']").send_keys("600")
    driver.find_element_by_xpath("//input[@name='taric']").send_keys("700")

    driver.find_element_by_xpath("//input[@name='quantity']").clear()
    driver.find_element_by_xpath("//input[@name='quantity']").send_keys("1000")
    driver.find_element_by_xpath("//input[@name='weight']").clear()
    driver.find_element_by_xpath("//input[@name='weight']").send_keys("2")
    driver.find_element_by_xpath("//input[@name='dim_x']").clear()
    driver.find_element_by_xpath("//input[@name='dim_x']").send_keys("100")
    driver.find_element_by_xpath("//input[@name='dim_y']").clear()
    driver.find_element_by_xpath("//input[@name='dim_y']").send_keys("50")
    driver.find_element_by_xpath("//input[@name='dim_z']").clear()
    driver.find_element_by_xpath("//input[@name='dim_z']").send_keys("30")

    # inserting image
    # driver.find_element_by_xpath("//input[@name='new_images[]']").send_keys("C:\\_all_lib\\ver3\\test_4\\01_cat_carrier.jpg")
    driver.find_element_by_xpath("//input[@name='new_images[]']").send_keys(os.getcwd() + "/01_cat_carrier.jpg")
    driver.find_element_by_xpath("//button[@value='Save']").click()

    # checking presence
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, ("//./a[contains(.,'cat_carrier')]"))))

    driver.quit()

# http://software-testing.ru/forum/index.php?/topic/17746-podskazhite-po-xpath/
# http://software-testing.ru/forum/index.php?/topic/26091-zagruzit-izobrazhenie/
# http://software-testing.ru/forum/index.php?/topic/32621-python-selenium-proverit-est-li-element-na-stranitce/