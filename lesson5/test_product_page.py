from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.success_alert()
    page.price_in_cart()

