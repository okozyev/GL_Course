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





def test_task_10():
    driver = webdriver.Chrome()

    # Pages init
    lite_cart = LiteCart(driver)
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    header_page = Header(driver)
    cart_page = CartPage(driver)

    # test
    lite_cart.litecart_init()
    main_page.open_product_page()
    product_page.add_all_size_products_to_cart()
    header_page.open_cart()

    # removing products block
    cart_page.empty_cart()
    # products_count = cart_page.get_products_count()

    print("Good job, padavan. Confident should You be")

    lite_cart.quit()