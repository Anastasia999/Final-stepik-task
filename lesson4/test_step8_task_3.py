import time
import math
import pytest
from selenium import webdriver
from lesson3 import locator as locator_

def find(page, locator):
    return page.find_element_by_css_selector(locator)

@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_test_answer(url):
    try:
        browser = webdriver.Chrome()
        # говорим WebDriver искать каждый элемент в течение 5 секунд
        browser.implicitly_wait(10)
        browser.get(url)
        answer = str(math.log(int(time.time())))
        #input(anwer)

        #time.sleep(10)
        answer_field = find(browser, locator_.answer_input)
        answer_field.clear()
        answer_field.send_keys(answer)

        find(browser, locator_.send_button).click()
        #time.sleep(5)
        text_from_alien = find(browser, locator_.placeholder).text
        input(text_from_alien)

        assert  "Correct!" in find(browser, locator_.placeholder).text, "Incorrect answer!"
    finally:
        browser.quit()
