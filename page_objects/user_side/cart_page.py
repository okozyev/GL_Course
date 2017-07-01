from selenium import webdriver

from utils import wait_for_element


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

    def delete_product_item(self, remove_button):
        remove_button.click()
