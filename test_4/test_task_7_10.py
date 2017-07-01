from time import sleep

from selenium import webdriver

from page_objects.user_side.cart_page import CartPage
from page_objects.user_side.header import Header
from page_objects.user_side.main_page import MainPage
from page_objects.user_side.product_page import ProductPage


def test_task_7_10():
    driver = webdriver.Chrome()
    driver.get('http://localhost/litecart/en/')
    driver.implicitly_wait(5)
    driver.maximize_window()

    # Pages init
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    header_page = Header(driver)
    cart_page = CartPage(driver)


    main_page.open_product_page()
    product_page.add_all_size_products_to_cart()
    header_page.open_cart()

    # removing products block
    products_count = cart_page.get_products_count()

    for counter in range(2, 0, -1):
        sleep(1)
        products_list = cart_page.get_products_list()
        cart_page.delete_product_item(products_list[counter])
        # assert (products_count-1 == cart_page.get_products_count())
        sleep(1)

    sleep(5)
