from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("#login_link").click()

    time.sleep(3)
    user_name = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.ID, "id_login-username")))
    #user_name = browser.find_element_by_css_selector("#id_login-username")
    user_name.send_keys("la+1@mail.com")

    pswd = browser.find_element_by_css_selector("#id_login-password")
    pswd.send_keys("Stepik0987")

    browser.find_element_by_css_selector("[name='login_submit']").click()
    time.sleep(3)
    browser.find_element_by_css_selector(locator_.account_page_link).click()

    browser.find_element_by_css_selector(profile_edit_link).click()
    email_field = browser.find_element_by_css_selector(email_imput)
    email_field.clear()
    email_field.send_keys(new_email)


    browser.find_element_by_css_selector(save_edited_profile).click()
    success_alert = browser.find_element_by_css_selector(success_editing_text).text
    assert "Профиль обновлен" in success_alert, "Profile isn't updated"

    new_mail = browser.find_element_by_css_selector(profile_email_labbel).text
    assert new_email in new_mail, "New email isn't saved"
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()