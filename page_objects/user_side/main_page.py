from selenium import webdriver

from utils import wait_for_element


class MainPage(object):

    #locators block
    campaign_products_tab_locator = '[href="#campaign-products"]'
    product_item_locator = '#campaign-products [title="Yellow Duck"]'

    # initialising driver main web page
    def __init__(self, driver):
        self.driver = driver

    def click_on_campaign_products_tab(self):
        element = self.driver.find_element_by_css_selector(self.campaign_products_tab_locator)
        wait_for_element(self.driver, element)
        element.click()

    def click_on_product_item(self):
        element = self.driver.find_element_by_css_selector(self.product_item_locator)
        wait_for_element(self.driver, element)
        element.click()

    # combining tab and product to open
    def open_product_page(self):
        self.click_on_campaign_products_tab()
        self.click_on_product_item()


