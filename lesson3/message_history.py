from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
login_link = "#login_link"
person_name = "id_login-username"
person_pswd = "#id_login-password"
sign_in_button = "[name='login_submit']"
account_page_link = "[href='/ru/accounts/']"
email_page_link = "[href='/ru/accounts/emails/']"
first_email_link = ".table tbody tr:nth-child(1) a"
page_title_text = ".page-header h1"
topic_email_text = ".table tr:nth-child(2) td"
description_email_text = ".table tr:nth-child(3) td"
try:
    email = "la+1@mail.com"
    user_pswd = "Stepik0987"
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(login_link).click()

    time.sleep(3)
    user_name = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.ID, person_name)))
    #user_name = browser.find_element_by_css_selector("#id_login-username")
    user_name.send_keys(email)

    pswd = browser.find_element_by_css_selector(person_pswd)
    pswd.send_keys(user_pswd)

    browser.find_element_by_css_selector(sign_in_button).click()

    browser.find_element_by_css_selector(account_page_link).click()

    browser.find_element_by_css_selector(email_page_link).click()

    browser.find_element_by_css_selector(first_email_link).click()

    page_title = browser.find_element_by_css_selector(page_title_text).text
    assert "Адрес электронной почты: Спасибо за регистрацию!" in page_title, "Open not email about success registration"

    topic_email = browser.find_element_by_css_selector(topic_email_text).text
    assert "Спасибо за регистрацию!" in topic_email, "incorrect email topic"

    email_description = browser.find_element_by_css_selector(description_email_text).text
    assert "Спасибо за регистрацию!" in email_description, "Incorrect email description"
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()