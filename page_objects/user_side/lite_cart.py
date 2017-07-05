from selenium import webdriver

class LiteCart(object):

    #urls block
    main_url = 'http://localhost/litecart/en/'

    # initialising driver main web page
    def __init__(self, driver):
        self.driver = driver

    def litecart_init(self):
        self.driver.get(self.main_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
