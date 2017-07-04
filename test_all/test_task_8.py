from selenium import webdriver


    # define switching
def switch_to_new_window(driver, old_windows):
    new_window = [i for i in driver.window_handles if i not in old_windows]
    return new_window[0]

    # main test
def test_task_8():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox
    # driver = webdriver.Ie
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").submit()
    driver.implicitly_wait(5)

    # enter countries tab
    driver.find_element_by_xpath("//a[contains(.,'Countries')]").click()
    driver.find_element_by_xpath("//a[@class='btn btn-default']").click()

    # define all new_tabs ou parent_tab
    new_tabs = driver.find_elements_by_class_name('fa-external-link')

    # define parent_tab handle
    parent_tab = driver.current_window_handle

    # selecting all new_tabs
    for i in new_tabs:
        old_windows = driver.window_handles
        i.click()

    # comparing handles
        new_window = switch_to_new_window(driver, old_windows)
        assert new_window, print("No new tabs opened")
    # new tab behaviour

        if new_window:
            driver.switch_to.window(new_window)
            driver.close()
            driver.switch_to.window(parent_tab)

    driver.quit()