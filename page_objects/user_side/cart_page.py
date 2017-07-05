from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import wait_for_element
# from utils import one_by_one_delete
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class CartPage(object):

    #locators block
    remove_button_locator = '.btn-danger'



    # initialising driver main web page
    def __init__(self, driver):
        self.driver = driver


    def get_products_list(self):
        elements_list = self.driver.find_elements_by_css_selector(self.remove_button_locator)
        wait_for_element(self.driver, self.remove_button_locator)
        return elements_list

    def get_products_count(self):
        elements_list = self.driver.find_elements_by_css_selector(self.remove_button_locator)
        wait_for_element(self.driver, self.remove_button_locator)
        return len(elements_list)

    # def delete_product_item(self, remove_button):
    #     remove_button.click()

    def empty_cart(self):
        # one_by_one_delete(self)
        element = WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
        # element = WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
        self.WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']"))).click()


    # def one_by_one_delete(self):
#         open_cart()
#         self.implicitly_wait(2)
#         try:
#         WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
#     finally:
#         while items(".//*[@id='box-checkout-cart']//tbody/tr") > 0:
#             try:
#                 WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
#         except:
#     driver.find_element_by_xpath(".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']").click()
#
# def items(xpath):
#     return len(driver.find_elements_by_xpath(xpath))