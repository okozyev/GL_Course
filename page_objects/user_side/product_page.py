from selenium import webdriver

from utils import wait_for_element


class ProductPage(object):


    #locators block
    size_selection_locator = '[name="options[Size]"]'
    size_selection_small_item_locator = 'option[value="Small"]'
    size_selection_medium_item_locator = 'option[value="Medium"]'
    size_selection_large_item_locator = 'option[value="Large"]'

    add_to_cart = '[name="add_cart_product"]'
    close_button = '[aria-label="Close"]'


    # initialising driver main web page
    def __init__(self, driver):
        self.driver = driver

    def click_on_size_selection(self):
        element = self.driver.find_element_by_css_selector(self.size_selection_locator)
        wait_for_element(self.driver, element)
        element.click()

    def click_on_small_size_item(self):
        element = self.driver.find_element_by_css_selector(self.size_selection_small_item_locator)
        wait_for_element(self.driver, element)
        element.click()

    def select_small_size_item(self):
        self.click_on_size_selection()
        self.click_on_small_size_item()


    def click_on_med_size_item(self):
        element = self.driver.find_element_by_css_selector(self.size_selection_medium_item_locator)
        wait_for_element(self.driver, element)
        element.click()

    def select_med_size_item(self):
        self.click_on_size_selection()
        self.click_on_med_size_item()

    def click_on_big_size_item(self):
        element = self.driver.find_element_by_css_selector(self.size_selection_large_item_locator)
        wait_for_element(self.driver, element)
        element.click()

    def select_big_size_item(self):
        self.click_on_size_selection()
        self.click_on_big_size_item()

    def click_on_add_to_cart(self):
        element = self.driver.find_element_by_css_selector(self.add_to_cart)
        wait_for_element(self.driver, element)
        element.click()

    def close_product_item_page(self):
        element = self.driver.find_element_by_css_selector(self.close_button)
        wait_for_element(self.driver, element)
        element.click()

    def add_all_size_products_to_cart(self):
        self.select_small_size_item()
        self.click_on_add_to_cart()
        self.select_med_size_item()
        self.click_on_add_to_cart()
        self.select_big_size_item()
        self.click_on_add_to_cart()

        self.close_product_item_page()
