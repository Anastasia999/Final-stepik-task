from selenium import webdriver
from lesson3 import locator as locator_
from selenium.webdriver.support.ui import WebDriverWait

def find(page, locator):
    return page.find_element_by_css_selector(locator)
def find_all(page, locator):
    return page.find_elements_by_css_selector(locator)

def product_search():
    try:
        #Arrange
        browser = webdriver.Chrome()
        browser.get(locator_.main_page)

        search_field = find(browser, locator_.search_input)
        search_field.clear()

        #Act
        search_field.send_keys(locator_.search_text)
        find(browser, locator_.search_button).click()

        #Asserts
        search_title = find(browser, locator_.page_header).text
        assert locator_.search_text in search_title, "Incorrect page title for found book"

        result_amount = find(browser, locator_.search_elements)
        assert result_amount != 1, "Incorrect amount of search result"

        product_name = find(browser, locator_.book_title).text
        assert locator_.book_name in product_name, "Not found book by name"

        product_image = find(browser, locator_.book_img)
        attribute_value = product_image.get_attribute("alt")
        assert locator_.book_name in attribute_value, "Incorrect product image"

        product_price = find(browser, locator_.book_price).text
        assert locator_.price in product_price, "Incorrect product price"

    finally:
        browser.quit()

def review_cart():
    try:
        #Arrange
        browser = webdriver.Chrome()
        browser.get(locator_.main_page)

        open_catalog = find(browser, locator_.catalog_menu)
        open_catalog.click()

        add_product = find(browser, locator_.add_product_button).click()

        #Act
        open_cart = find(browser, locator_.cart_button).click()

        #Assert
        result_amount = find_all(browser, locator_.products_in_cart)
        assert result_amount != 1, "Incorrect amount of cart"

        product_name = find(browser, locator_.name_product_cart).text
        assert locator_.book_name in product_name, "Incorrect product name"

        product_amount = find(browser, locator_.amount_product_cart)
        amount_value = product_amount.get_attribute("value")
        assert "1" in amount_value, "Inccorrect product amount"

        product_price = find(browser, locator_.price_product_cart).text
        assert locator_.price in product_price, "Incorrect product price"

        product_image = find(browser, locator_.image_product_cart)
        attribute_value = product_image.get_attribute("alt")
        assert locator_.book_name in attribute_value, "Incorrect product image"

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

def message_history():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(20)

        browser.get(locator_.main_page)

        find(browser, locator_.login_link).click()

        user_name = find(browser, locator_.person_name)
        user_name.send_keys(locator_.email)

        pswd = find(browser, locator_.person_pswd)
        pswd.send_keys(locator_.user_pswd)
        find(browser, locator_.sign_in_button).click()

        find(browser, locator_.account_page_link).click()

        find(browser, locator_.email_page_link).click()
        #Act
        find(browser, locator_.first_email_link).click()
        #Assert
        page_title = find(browser, locator_.page_title_text).text
        assert "Адрес электронной почты: Спасибо за регистрацию!" in page_title, "Open not email about success registration"

        topic_email = find(browser, locator_.topic_email_text).text
        assert "Спасибо за регистрацию!" in topic_email, "incorrect email topic"

        email_description = find(browser, locator_.description_email_text).text
        assert "Спасибо за регистрацию!" in email_description, "Incorrect email description"
    finally:
        browser.quit()

def complete_order():
    try:
        locator_.common_attr = "required"
        # Arrange
        browser = webdriver.Chrome()
        browser.get(locator_.main_page)
        open_catalog = find(browser,  locator_.catalog_link)
        open_catalog.click()

        find(browser, locator_.add_product_button).click()

        find(browser, locator_.cart_link).click()

        find(browser, locator_.checkout_button).click()

        user_name = find(browser, locator_.user_name_input)
        user_name.send_keys(locator_.email)

        find(browser, locator_.login_radio_button).click()
        pswd = find(browser, locator_.user_pswd_input)
        pswd.send_keys(locator_.user_pswd)

        find(browser, locator_.login_button).click()

        #Act and assert
        first_name = find(browser, locator_.f_name_input)
        f_name_checked = first_name.get_attribute(locator_.common_attr)
        assert f_name_checked == "true", "First name notlocator_.common_attr"

        last_name = find(browser, locator_.l_name_input)
        l_name_checked = last_name.get_attribute(locator_.common_attr)
        assert l_name_checked == "true", "Last name notlocator_.common_attr"

        first_line = find(browser, locator_.first_line_input)
        f_line_checked = first_line.get_attribute(locator_.common_attr)
        assert f_line_checked == "true", "First line notlocator_.common_attr"

        city = find(browser, locator_.city_input)
        city_checked = city.get_attribute(locator_.common_attr)
        assert city_checked == "true", "City notlocator_.common_attr"

        postcode = find(browser, locator_.postcode_input)
        postcode_checked = postcode.get_attribute(locator_.common_attr)
        assert postcode_checked == "true", "Postcode notlocator_.common_attr"
    finally:
        browser.quit()

def change_email():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(30)

        browser.get(locator_.main_page)

        find(browser, locator_.login_link).click()

        user_name = find(browser, locator_.person_name)
        user_name.send_keys(locator_.email)

        pswd = find(browser, locator_.person_pswd)
        pswd.send_keys(locator_.user_pswd)
        find(browser, locator_.sign_in_button).click()

        find(browser, locator_.account_page_link).click()
        #Act
        find(browser, locator_.profile_edit_link).click()
        email_field = find(browser, locator_.email_imput)
        email_field.clear()
        email_field.send_keys(locator_.new_email)
        #Assert
        find(browser, locator_.save_edited_profile).click()
        success_alert = find(browser, locator_.success_editing_text).text
        assert "Профиль обновлен" in success_alert, "Profile isn't updated"

        changed_email = find(browser, locator_.profile_email_labbel).text
        assert locator_.new_email in changed_email, "New email isn't saved"
    finally:
        browser.quit()

#product_search()
#review_cart()
message_history()
#complete_order()
#change_email()


