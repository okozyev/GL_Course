from selenium import webdriver


def test_task_5():

#   Select Browser (del '#')

    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    # driver = webdriver.Ie()

    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/")

#   tab select
    main_tab = driver.find_element_by_css_selector('a[href="#campaign-products"]').click()
    # seek_prod_title = driver.find_element_by_css_selector('a[title="Yellow Duck"]').click()

#   taking values from tab
    seek_prod_name = driver.find_element_by_xpath("//div[@class='name']").text

    seek_prod_reg_price = driver.find_element_by_css_selector('s[class="regular-price"]').text
    seek_prod_reg_price_decor = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property('text-decoration-line')
    seek_prod_reg_price_color = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property('color')

    seek_prod_low_price = driver.find_element_by_css_selector('strong[class="campaign-price"]').text
    seek_prod_low_price_decor = driver.find_element_by_css_selector('strong[class="campaign-price"]').value_of_css_property('font-weight')
    seek_prod_low_price_color = driver.find_element_by_css_selector('strong[class="campaign-price"]').value_of_css_property('color')

#   click to open
    seek_prod_title = driver.find_element_by_css_selector('a[title="Yellow Duck"]').click()

#   taking values from opened
    prod_name = driver.find_element_by_xpath("//h1[@class='title']").text

    prod_reg_price = driver.find_element_by_xpath("//del[@class='regular-price']").text
    prod_reg_price_decor = driver.find_element_by_xpath("//del[@class='regular-price']").value_of_css_property('text-decoration-line')
    prod_reg_price_color = driver.find_element_by_xpath("//del[@class='regular-price']").value_of_css_property('color')

    prod_low_price = driver.find_element_by_xpath("//strong[@class='campaign-price']").text
    prod_low_price_decor = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')
    prod_low_price_color = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('color')

#    comparement
    print('Product Name is equal on Main page and Item Page - ', seek_prod_name == prod_name)
    assert (seek_prod_name == prod_name), "Product Title doesn't match"

    print('Product RegPrice is equal on Main page and Item Page - ', seek_prod_reg_price == prod_reg_price)
    assert (seek_prod_reg_price == prod_reg_price), "Product Price doesn't match"

    print('Product RegPrice decor (Line) is equal on Main page and Item Page - ', seek_prod_reg_price_decor == prod_reg_price_decor)
    assert (seek_prod_reg_price_decor == prod_reg_price_decor), "Product RegPrice decor (Line) doesn't match"

    print('Product RegPrice color is equal on Main page and Item Page - ', seek_prod_reg_price_color == prod_reg_price_color)
    assert (seek_prod_reg_price_color == prod_reg_price_color), "Product RegPrice color doesn't match"

    print('Product Campaign Price is equal on Main page and Item Page - ', seek_prod_low_price == prod_low_price)
    assert (seek_prod_low_price == prod_low_price), "Product Campaign Price doesn't match"

    print('Product Campaign Price font weight is equal on Main page and Item Page - ', seek_prod_low_price_decor == prod_low_price_decor)
    assert (seek_prod_low_price_decor == prod_low_price_decor), "Product Campaign Price font weight doesn't match"

    print('Product Campaign Price font color is equal on Main page and Item Page - ', seek_prod_low_price_color == prod_low_price_color)
    assert (seek_prod_low_price_color == prod_low_price_color), "Product Campaign Price color doesn't match"

#   end of process
    driver.quit()


# xpath seek =   //*[@id="box-campaign-products"]/div/div/div/a/div[2]/div[1]  <div class="name">Yellow Duck</div>
# xpath prod =   //*[@id="box-product"]/div[1]/div[2]/h1   <h1 class="title">Yellow Duck</h1>

# seek_prod_name = driver.find_element_by_xpath("//div[@class='name']")
# prod_name = driver.find_element_by_xpath("//h1[@class='title']")