from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(5)
driver.maximize_window()

def products_in_cart(xpath):
    return len(driver.find_elements_by_xpath(xpath))


def test_task_7():

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

    remove_buttons_locator = 'button[class="btn btn-danger"]'
    back_button_locator = '[href="http://localhost/litecart/en/"]'


    click_on_campaign_products_tab = driver.find_element_by_css_selector(campaign_products_tab_locator).click()

    click_on_product_item = driver.find_element_by_css_selector(product_item_locator).click()

    # product page operations

    click_on_add_to_cart = driver.find_element_by_css_selector(add_to_cart)

    click_on_size_selection = driver.find_element_by_css_selector(size_selection_locator).click()
    click_on_small_size_item = driver.find_element_by_css_selector(size_selection_small_item_locator).click()
    click_on_add_to_cart.click()

    click_on_med_size_item = driver.find_element_by_css_selector(size_selection_medium_item_locator).click()
    click_on_add_to_cart.click()

    click_on_big_size_item = driver.find_element_by_css_selector(size_selection_large_item_locator).click()
    click_on_add_to_cart.click()

    close_product_item_page = driver.find_element_by_css_selector(close_button).click()

    # close_product_item_page()

    # get_cart_items_counter = driver.find_element_by_css_selector(cart_items_count_locator).get_attribute('quantity')


    # return get_cart_items_counter.text

    # def wait_untill_cart_items_counter_changed(self):
    # cart_items_value = driver.get_cart_items_counter()
    # wait_until_element_text_present(driver, cart_items_count_locator, cart_items_value + 1)

    open_cart = driver.find_element_by_css_selector(cart_title_locator).click()

    try:
        WebDriverWait(driver, 1).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
    finally:
        while products_in_cart(".//*[@id='box-checkout-cart']//tbody/tr") > 0:
            try:
                WebDriverWait(driver, 1).until(ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
            except:
                driver.find_element_by_css_selector(remove_buttons_locator).click()

    press_back = driver.find_element_by_css_selector(back_button_locator).click()

    # get_cart_items_counter = driver.find_element_by_css_selector(cart_items_count_locator).get_attribute('text')
    print("Good job, padavan. Confident should You be")

    driver.quit()


