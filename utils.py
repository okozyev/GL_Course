import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




def wait_for_element(driver, element):
    try:
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, element)))
    except:
        pass


def get_image_path(filename):
    return os.path.abspath("resources/img/{}".format(filename))


def wait_until_element_text_present(driver, element, value):
    try:
        WebDriverWait(driver, 5).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, element), value))
    except:
        pass


def one_by_one_delete(driver):
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
    driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()


#     driver.open_cart()
#     driver.find_element_by_xpath(".//*[@id='cart']").click()
#     driver.implicitly_wait(2)
#     items = return len(driver.find_elements_by_xpath(xpath))
#     try:
#         WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
#     finally:
#         while items(".//*[@id='box-checkout-cart']//tbody/tr") > 0:
#             try:
#                 WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
#             except: driver.find_element_by_xpath(".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']").click()
#
# # def items(xpath):
# #     return len(driver.find_elements_by_xpath(xpath))