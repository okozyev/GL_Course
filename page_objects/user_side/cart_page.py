from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import wait_for_element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class CartPage(object):

    #locators block
    remove_button_locator = '.btn-danger'
    # remove_buttons_locator = 'button[class="btn btn-danger"]'
    # back_button_locator = '[href="http://localhost/litecart/en/"]'
    # loader_wrapper_locator = ".//div[@class='loader-wrapper']"

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


    def products_in_cart(self, xpath):
        return len(self.driver.find_elements_by_xpath(xpath))

    def empty_cart_mechanism(self):
        remove_buttons_locator = 'button[class="btn btn-danger"]'
        x_locator = ".//*[@id='box-checkout-cart']//tbody/tr"
        loader_wrapper_locator = ".//div[@class='loader-wrapper']"
        back_button_locator = '[href="http://localhost/litecart/en/"]'
        try:
            WebDriverWait(self.driver, 1).until(ec.presence_of_element_located((By.XPATH, loader_wrapper_locator)))
        finally:
            while self.products_in_cart(x_locator) > 0:
                try:
                    WebDriverWait(self.driver, 1).until(ec.presence_of_element_located((By.XPATH, loader_wrapper_locator)))
                except:
                    self.driver.find_element_by_css_selector(remove_buttons_locator).click()

        self.driver.find_element_by_css_selector(back_button_locator).click()

    def empty_cart(self):
        self.empty_cart_mechanism()