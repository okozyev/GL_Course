from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# from page_objects.user_side.cart_page import CartPage
# from page_objects.user_side.header import Header
# from page_objects.user_side.main_page import MainPage
# from page_objects.user_side.product_page import ProductPage
# from page_objects.user_side.lite_cart import LiteCart


def test_task_7_10():
    driver = webdriver.Chrome()
    driver.get('http://localhost/litecart/en/')
    driver.implicitly_wait(5)
    driver.maximize_window()

    # Pages init

    campaign_products_tab_locator = '[href="#campaign-products"]'
    product_item_locator = '#campaign-products [title="Yellow Duck"]'

    size_selection_locator = '[name="options[Size]"]'
    size_selection_small_item_locator = 'option[value="Small"]'
    size_selection_medium_item_locator = 'option[value="Medium"]'
    size_selection_large_item_locator = 'option[value="Large"]'

    add_to_cart = '[name="add_cart_product"]'
    close_button = '[aria-label="Close"]'

    cart_items_count_locator = '.quantity'
    cart_title_locator = '#cart .title'



    click_on_campaign_products_tab = driver.find_element_by_css_selector(campaign_products_tab_locator).click()
        # element = driver.find_element_by_css_selector(campaign_products_tab_locator)
        # wait_for_element(driver, element)
        # element.click()

    click_on_product_item = driver.find_element_by_css_selector(product_item_locator).click()
        # element = driver.find_element_by_css_selector(product_item_locator)
        # wait_for_element(driver, element)
        # element.click()

    # combining tab and product to open
    # open_product_page = click_on_campaign_products_tab + click_on_product_item

    # product page operations

    click_on_add_to_cart = driver.find_element_by_css_selector(add_to_cart)
    click_on_size_selection = driver.find_element_by_css_selector(size_selection_locator).click()
    # element = driver.find_element_by_css_selector(size_selection_locator)
    #         wait_for_element(driver, element)
    #         element.click()

    click_on_small_size_item = driver.find_element_by_css_selector(size_selection_small_item_locator).click()
            # element = driver.find_element_by_css_selector(size_selection_small_item_locator)
            # wait_for_element(driver, element)
            # element.click()

            # select_small_size_item = click_on_small_size_item
            # click_on_size_selection()
            # click_on_small_size_item()
    click_on_add_to_cart.click()

    click_on_med_size_item = driver.find_element_by_css_selector(size_selection_medium_item_locator).click()
            # element = driver.find_element_by_css_selector(size_selection_medium_item_locator)
            # wait_for_element(driver, element)
            # element.click()
    click_on_add_to_cart.click()

    # select_med_size_item = click_on_med_size_item()
    #         click_on_size_selection()
    #         click_on_med_size_item()
    # click_on_add_to_cart.click()

    click_on_big_size_item = driver.find_element_by_css_selector(size_selection_large_item_locator).click()
            # wait_for_element(driver, element)
            # element.click()

    # select_big_size_item = click_on_big_size_item()
    #         click_on_size_selection()
    #         click_on_big_size_item()
    click_on_add_to_cart.click()
    # click_on_add_to_cart = driver.find_element_by_css_selector(add_to_cart).click()
            # wait_for_element(driver, element)
            # element.click()

    close_product_item_page = driver.find_element_by_css_selector(close_button).click()
            # wait_for_element(driver, element)
            # element.click()

    # def add_all_size_products_to_cart():
    #         select_small_size_item()
    #         click_on_add_to_cart()
    #         select_med_size_item()
    #         click_on_add_to_cart()
    #         select_big_size_item()
    #         click_on_add_to_cart()


            # close_product_item_page()

    # ///////////////////////////////

    get_cart_items_counter = driver.find_element_by_css_selector(cart_items_count_locator).get_attribute('quantity')
            # return get_cart_items_counter.text

    # def wait_untill_cart_items_counter_changed(self):
    # cart_items_value = driver.get_cart_items_counter()
    # wait_until_element_text_present(driver, cart_items_count_locator, cart_items_value + 1)

    open_cart = driver.find_element_by_css_selector(cart_title_locator).click()
        # wait_for_element(self.driver, element)
        # element.click()

    sleep(3)


    # main_page = MainPage(driver)
    # product_page = ProductPage(driver)
    # header_page = Header(driver)
    # cart_page = CartPage(driver)
    #
    #
    # lite_cart.litecart_init()
    # main_page.open_product_page()
    # product_page.add_all_size_products_to_cart()
    # header_page.open_cart()
    #
    # # removing products block
    # cart_page.empty_cart()
    # # products_count = cart_page.get_products_count()
    #
    #
    # # for counter in range(2, 0, -1):
    # #     sleep(1)
    # #     products_list = cart_page.get_products_list()
    # #     cart_page.delete_product_item(products_list[counter])
    # #     # assert (products_count-1 == cart_page.get_products_count())
    # #     sleep(1)
    # #
    # # sleep(5)
    #
    # # try:
    # #     WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
    # # finally:
    # #     while items(".//*[@id='box-checkout-cart']//tbody/tr") > 0:
    # #         try:
    # #             WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
    # #         except:
    # #             driver.find_element_by_xpath(".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']").click()