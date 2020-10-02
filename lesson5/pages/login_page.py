from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url1 = self.browser.current_url# реализуйте проверку на корректный url адрес
        #input(current_url1)
        #convert_url = str(current_url1)
        assert "login" in current_url1, "Incorrect URL for login page"

    def should_be_login_form(self):
        assert self.should_be_login_form(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.should_be_register_form(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"