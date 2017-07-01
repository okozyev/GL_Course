from selenium import webdriver

from utils import wait_for_element
from utils import wait_until_element_text_present


class Header(object):


    #locators block
    cart_items_count_locator = '.quantity'
    cart_title_locator = '#cart .title'



    # initialising driver main web page
    def __init__(self, driver):
        self.driver = driver


    def get_cart_items_counter(self):
        element = self.driver.find_element_by_css_selector(self.cart_items_count_locator)
        wait_for_element(self.driver, element)
        return element.text

    def wait_untill_cart_items_counter_changed(self):
        cart_items_value = self.get_cart_items_counter()
        wait_until_element_text_present(self.driver, self.cart_items_count_locator, cart_items_value + 1)

    def open_cart(self):
        element = self.driver.find_element_by_css_selector(self.cart_title_locator)
        wait_for_element(self.driver, element)
        element.click()
