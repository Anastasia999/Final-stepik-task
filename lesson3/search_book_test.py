from selenium import webdriver
import time
from lesson3 import locator as locator_


def find(page, locator):
    return page.find_element_by_css_selector(locator)


def find_all(page, locator):
    return page.find_elements_by_css_selector(locator)
try:

    main_page = "http://selenium1py.pythonanywhere.com/ru/"
    search_text = "Coders at work"
    book_name = "Coders at Work"
    price = "19,99"
    browser = webdriver.Chrome()
    browser.get(main_page)

    search_field = find(browser, locator_.search_input)
    search_field.clear()
    search_field.send_keys(search_text)
    browser.find_element_by_css_selector(locator_.search_button).click()

    search_title = browser.find_element_by_css_selector(locator_.page_header).text
    assert search_text in search_title, "Incorrect page title for found book"

    result_amount = browser.find_elements_by_css_selector(locator_.search_elements)
    assert result_amount != 1, "Incorrect amount of search result"

    product_name = browser.find_element_by_css_selector(locator_.book_title).text
    assert book_name in product_name, "Not found book by name"

    product_image = browser.find_element_by_css_selector(locator_.book_img)
    attribute_value = product_image.get_attribute("alt")
    assert book_name in attribute_value, "Incorrect product image"

    product_price = browser.find_element_by_css_selector(locator_.book_price).text
    assert price in product_price, "Incorrect product price"
    time.sleep(3)

finally:
    browser.quit()