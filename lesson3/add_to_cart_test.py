from selenium import webdriver
import time


try:
    catalog_menu = "ul .dropdown-menu :nth-child(1)"
    add_product_button = "[action='/ru/basket/add/207/']"
    cart_button = "[href='/ru/basket/'"
    products_in_cart = ".basket-items"
    name_product_cart = ".basket-items .col-sm-4 a"
    amount_product_cart = ".basket-items [type='number']"
    price_product_cart = ".price_color"
    image_product_cart = ".basket-items img"

    main_page = "http://selenium1py.pythonanywhere.com/ru/"
    book_name = "Coders at Work"
    price = "19,99"
    browser = webdriver.Chrome()
    browser.get(main_page)

    open_catalog = browser.find_element_by_css_selector(catalog_menu)
    open_catalog.click()

    add_product = browser.find_element_by_css_selector(add_product_button).click()

    open_cart = browser.find_element_by_css_selector(cart_button).click()

    result_amount = browser.find_elements_by_css_selector(products_in_cart)
    assert result_amount != 1, "Incorrect amount of cart"

    product_name = browser.find_element_by_css_selector(name_product_cart).text
    assert book_name in product_name, "Incorrect product name"

    product_amount = browser.find_element_by_css_selector(amount_product_cart)
    amount_value = product_amount.get_attribute("value")
    assert "1" in amount_value, "Inccorrect product amount"

    product_price = browser.find_element_by_css_selector(price_product_cart).text
    assert price in product_price, "Incorrect product price"

    product_image = browser.find_element_by_css_selector(image_product_cart)
    attribute_value = product_image.get_attribute("alt")
    assert book_name in attribute_value, "Incorrect product image"

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()