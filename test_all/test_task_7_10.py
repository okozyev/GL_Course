from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import wait_for_element
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.user_side.cart_page import CartPage
from page_objects.user_side.header import Header
from page_objects.user_side.main_page import MainPage
from page_objects.user_side.product_page import ProductPage
from page_objects.user_side.lite_cart import LiteCart


def test_task_7_10():
    driver = webdriver.Chrome()
    # driver.get('http://localhost/litecart/en/')
    # driver.implicitly_wait(5)
    # driver.maximize_window()

    # Pages init
    lite_cart = LiteCart(driver)
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    header_page = Header(driver)
    cart_page = CartPage(driver)


    lite_cart.litecart_init()
    main_page.open_product_page()
    product_page.add_all_size_products_to_cart()
    header_page.open_cart()

    # removing products block
    cart_page.empty_cart()
    # products_count = cart_page.get_products_count()


    # for counter in range(2, 0, -1):
    #     sleep(1)
    #     products_list = cart_page.get_products_list()
    #     cart_page.delete_product_item(products_list[counter])
    #     # assert (products_count-1 == cart_page.get_products_count())
    #     sleep(1)
    #
    # sleep(5)

    # try:
    #     WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
    # finally:
    #     while items(".//*[@id='box-checkout-cart']//tbody/tr") > 0:
    #         try:
    #             WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
    #         except:
    #             driver.find_element_by_xpath(".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']").click()