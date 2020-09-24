from selenium import webdriver
import time
try:
    catalog_link = "ul .dropdown-menu :nth-child(1)"
    add_product_button = "[action='/ru/basket/add/207/']"
    cart_link = "[href='/ru/basket/'"
    checkout_button = ".form-group [href='/ru/checkout/']"
    user_name_input = "#id_username"
    login_radio_button = "[for='id_options_2']"
    user_pswd_input = "#id_password"
    login_button = ".form-stacked button"
    f_name_input = "#id_first_name"
    l_name_input = "#id_last_name"
    first_line_input = "#id_line1"
    city_input = "#id_line4"
    postcode_input = "#id_postcode"
    common_attr = "required"
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser = webdriver.Chrome()
    browser.get(link)
    open_catalog = browser.find_element_by_css_selector(catalog_link)
    open_catalog.click()

    browser.find_element_by_css_selector(add_product_button).click()

    browser.find_element_by_css_selector(cart_link).click()

    browser.find_element_by_css_selector(checkout_button).click()

    user_name = browser.find_element_by_css_selector(user_name_input)
    user_name.send_keys(email)

    browser.find_element_by_css_selector(login_radio_button).click()
    pswd = browser.find_element_by_css_selector(user_pswd_input)
    pswd.send_keys(user_pswd)

    browser.find_element_by_css_selector(login_button).click()

    first_name = browser.find_element_by_css_selector(f_name_input)
    f_name_checked = first_name.get_attribute(common_attr)
    assert f_name_checked == "true", "First name notcommon_attr"

    last_name = browser.find_element_by_css_selector(l_name_input)
    l_name_checked = last_name.get_attribute(common_attr)
    assert f_name_checked == "true", "Last name notcommon_attr"

    first_line = browser.find_element_by_css_selector(first_line_input)
    f_line_checked = first_line.get_attribute(common_attr)
    assert f_line_checked == "true", "First line notcommon_attr"

    city = browser.find_element_by_css_selector(city_input)
    city_checked = city.get_attribute(common_attr)
    assert city_checked == "true", "City notcommon_attr"

    postcode = browser.find_element_by_css_selector(postcode_input)
    postcode_checked = postcode.get_attribute(common_attr)
    assert postcode_checked == "true", "Postcode notcommon_attr"

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()