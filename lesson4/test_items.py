import pytest
import time
from lesson3 import locator as locator_

def find(page, locator):
    return page.find_element_by_css_selector(locator)
def find_all(page, locator):
    return page.find_elements_by_css_selector(locator)

def test_cart_button(browser):
   browser.get(locator_.main_page)

    time.sleep(5)

    open_catalog = find(browser, locator_.catalog_menu)
    open_catalog.click()

    search_field = find(browser, locator_.search_input)
    search_field.clear()

    search_field.send_keys(locator_.search_text)
    find(browser, locator_.search_button).click()

    product_name = find(browser, locator_.book_title).text
    assert locator_.book_name in product_name, "Not found book by name"

    product_image = find(browser, locator_.book_img)
    attribute_value = product_image.get_attribute("alt")
    assert locator_.book_name in attribute_value, "Incorrect product image"

    product_image.click()

    product_button = find(browser, locator_.item_buy_button)

    assert product_button != 0, "Missing button for buy"





