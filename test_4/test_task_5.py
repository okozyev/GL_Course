from selenium import webdriver



def test_task_5():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()

    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/")

#   tab select
    main_tab = driver.find_element_by_css_selector('a[href="#campaign-products"]').click()
    # seek_prod_title = driver.find_element_by_css_selector('a[title="Yellow Duck"]').click()

#   taking values from tab
#     seek_prod_name = driver.find_element_by_css_selector('a[title="Yellow Duck"]').text
    seek_prod_name = driver.find_element_by_xpath("//div[@class='name']")
    seek_prod_reg_price = driver.find_element_by_css_selector('s[class="regular-price"]').text
    seek_prod_reg_price_decor = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property('text-decoration-line')
    seek_prod_reg_price_color = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property('color')

    seek_prod_title = driver.find_element_by_css_selector('a[title="Yellow Duck"]').click()

#   taking values from opened
    prod_name = driver.find_element_by_xpath("//h1[@class='title']").text
    prod_reg_price = driver.find_element_by_xpath("//del[@class='regular-price']").text

#    comparement
    print('Product Name is equal on Main page and Item Page - ', seek_prod_name == prod_name)
    assert (seek_prod_name == prod_name), "Product Title doesn't match"

    print('Product RegPrice is equal on Main page and Item Page - ', seek_prod_reg_price == prod_reg_price)
    assert (seek_prod_reg_price == prod_reg_price), "Product Price doesn't match"


#

# xpath seek =   //*[@id="box-campaign-products"]/div/div/div/a/div[2]/div[1]  <div class="name">Yellow Duck</div>
# xpath prod =   //*[@id="box-product"]/div[1]/div[2]/h1   <h1 class="title">Yellow Duck</h1>

    # seek_prod_name = driver.find_element_by_xpath("//div[@class='name']")
    # prod_name = driver.find_element_by_xpath("//h1[@class='title']")