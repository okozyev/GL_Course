import datetime

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class ScreenerAndLoggerListener(AbstractEventListener):
    # print element locator
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value)

    # print screenshot after exeption
    def on_exception(self, exception, driver):
        print(exception)
        now = datetime.datetime.now()
        time_string = str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
        driver.get_screenshot_as_file('pic_' + time_string + '.png')


def test_task_9():
    # Listener activation
    driver = EventFiringWebDriver(webdriver.Chrome(), ScreenerAndLoggerListener())
    # driver = EventFiringWebDriver(webdriver.Firefox(), ScreenerAndLoggerListener())
    # driver = EventFiringWebDriver(webdriver.Ie(), ScreenerAndLoggerListener())

    # login
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").submit()

    driver.implicitly_wait(5)

    # enter menu
    links = driver.find_elements_by_xpath('//*[@id="app-"]')
    for cycle in range(1, len(links) + 1):
        outer_links = '//*[@id="box-apps-menu"]/li[' + str(cycle) + ']'
        driver.find_element_by_xpath(outer_links).click()

        # entering submenus
        inside = driver.find_elements_by_xpath(outer_links + '/ul/li')
        if inside:
            for cycle_next in range(1, len(inside) + 1):
                inner_links = outer_links + '/ul/li[' + str(cycle_next) + ']'
                driver.find_element_by_xpath(inner_links).click()
    driver.quit()


# https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/