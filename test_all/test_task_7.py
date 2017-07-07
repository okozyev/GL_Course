from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(5)

    # defs

def ammount_of_cart_items():
    # locators
    cart_items_count_locator = '.quantity'

    cart_items_total = int(driver.find_element_by_css_selector(cart_items_count_locator).text)

def preparation_new_product_to_purchase():
    # locators
    campaign_products_tab_locator = '[href="#campaign-products"]'
    product_item_locator = '#campaign-products [title="Yellow Duck"]'
    # add_to_cart = '[name="add_cart_product"]'
    size_selection_locator = '[name="options[Size]"]'

    click_on_campaign_products_tab = driver.find_element_by_css_selector(campaign_products_tab_locator).click()
    click_on_product_item = driver.find_element_by_css_selector(product_item_locator).click()
    click_on_size_selection = driver.find_element_by_css_selector(size_selection_locator).click()

def finishing_add_new_product():
    # locators
    close_button = '[aria-label="Close"]'
    cart_items_count_locator = '.quantity'
    add_to_cart = '[name="add_cart_product"]'
    cart_items_total = int(driver.find_element_by_css_selector(cart_items_count_locator).text)
    click_on_add_to_cart = driver.find_element_by_css_selector(add_to_cart)

    click_on_add_to_cart.click()
    close_product_item_page = driver.find_element_by_css_selector(close_button).click()
    cart_items_total += 1
    WebDriverWait(driver, 2).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, cart_items_count_locator), str(cart_items_total)))

def add_1st_item_in_cart():
    # locators
    size_selection_small_item_locator = 'option[value="Small"]'

    preparation_new_product_to_purchase()
    click_on_small_size_item = driver.find_element_by_css_selector(size_selection_small_item_locator).click()
    finishing_add_new_product()

def add_2nd_item_in_cart():
    # locators
    size_selection_medium_item_locator = 'option[value="Medium"]'

    preparation_new_product_to_purchase()
    click_on_med_size_item = driver.find_element_by_css_selector(size_selection_medium_item_locator).click()
    finishing_add_new_product()

def add_3rd_item_in_cart():
    # locators
    size_selection_large_item_locator = 'option[value="Large"]'

    preparation_new_product_to_purchase()
    click_on_big_size_item = driver.find_element_by_css_selector(size_selection_large_item_locator).click()
    finishing_add_new_product()

def test_task_7():
    # locators
    cart_items_count_locator = '.quantity'
    cart_title_locator = '#cart .title'
    remove_buttons_locator = 'button[class="btn btn-danger"]'
    back_button_locator = '[href="http://localhost/litecart/en/"]'

    add_1st_item_in_cart()
    add_2nd_item_in_cart()
    add_3rd_item_in_cart()

    cart_items_total = int(driver.find_element_by_css_selector(cart_items_count_locator).text)
    print("cart_items_total_before_delete =", cart_items_total)

    open_cart = driver.find_element_by_css_selector(cart_title_locator).click()

    table = driver.find_element_by_css_selector('#box-checkout-summary')
    delete_buttons = driver.find_elements_by_css_selector(remove_buttons_locator)
    press_back = driver.find_element_by_css_selector(back_button_locator)

    while delete_buttons:
        delete_buttons[0].click()
        WebDriverWait(driver, 2).until(ec.staleness_of(table))
        WebDriverWait(driver, 2).until(ec.staleness_of(delete_buttons[0]))
        delete_buttons = driver.find_elements_by_css_selector(remove_buttons_locator)

    press_back.click()

    cart_items_total_after_delete = int(driver.find_element_by_css_selector(cart_items_count_locator).text)

    print("Cart_items_after_delete =", cart_items_total_after_delete)
    assert (cart_items_total > cart_items_total_after_delete), print("Hrenovyi u vac cod, tovaris4")

    print("Good job, Padavan. Confident more should now You be")

    driver.quit()