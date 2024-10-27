from base_page import BasePage
import time
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для кнопки "Вход"
    def login_user_button_locator(self):
        return By.XPATH, f'//button[@class="marginBottom8_f7730b button_b83a05 button_dd4f85 lookFilled_dd4f85 colorBrand_dd4f85 sizeLarge_dd4f85 fullWidth_dd4f85 grow_dd4f85"]'

    # Локатор для ввода логина
    def login_input_locator(self):
        return By.XPATH, f'//input[@name="email"]'

    # Локатор для ввода пароля
    def password_input_locator(self):
        return By.XPATH, f'//input[@name="password"]'


    # Метод для залогиниться
    def login_user(self):
        self.send_keys(self.login_input_locator(), "dyatlova1108@gmail.com")
        self.send_keys(self.password_input_locator(), "Dyatlova1108!")
        self.click(self.login_user_button_locator())


    # Метод для открытия страницы
    def open_login_page(self):
        self.open_page()
