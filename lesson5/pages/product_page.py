from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def success_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        success_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text
        assert product_name in success_alert, "Product is not added to cart"

    def price_in_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert product_price in cart_price, "Price isn't match"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    #def should_be_add_to_cart(self):
        #assert ""

