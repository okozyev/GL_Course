from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_task_4():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox
    # driver = webdriver.Ie
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").click()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").submit()

    driver.implicitly_wait(5)

    # # //enter menu
    links = driver.find_elements_by_xpath('//*[@id="app-"]')
    for cycle in range(1, len(links) + 1):
        outer_links = '//*[@id="box-apps-menu"]/li[' + str(cycle) + ']'
        driver.find_element_by_xpath(outer_links).click()
        assert (WebDriverWait(driver, 3).until
               (ec.visibility_of_element_located((By.XPATH, '//*[@id="main"]/h1')))), "Element h1 not found"
     # # //entering submenus
        inside = driver.find_elements_by_xpath(outer_links + '/ul/li')
        if inside:
           for cycle_next in range(1, len(inside) + 1):
               inner_links = outer_links + '/ul/li[' + str(cycle_next) + ']'
               driver.find_element_by_xpath(inner_links).click()
               assert (WebDriverWait(driver, 3).until
               (ec.visibility_of_element_located((By.XPATH, '//*[@id="main"]/h1')))), "Element h1 not found"

    driver.quit()