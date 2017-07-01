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