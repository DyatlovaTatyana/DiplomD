import time
import pytest
from selenium import webdriver
from home_page import HomePage
from login_page import LoginPage
from base_page import BasePage

@pytest.fixture(scope="class")
def init_driver(request):
    #Инициализация драйвера
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    #Добавила блок с входом, чтобы не повторять его постоянно в тестах

    # Инициализация страницы
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    base_page = BasePage(driver)

    # Открытие страницы
    base_page.open_page()
    time.sleep(5)
    # login_page.open_login_page()

    # Логинимся
    login_page.login_user()

    home_page.clic_to_server_diplom()
    time.sleep(5)
    # Переходим в канал "4"
    home_page.clic_to_channel()
    time.sleep(5)

    yield driver

    driver.quit()

@pytest.fixture(scope="class")
def base_url():
    return 'https://discord.com/login'


@pytest.fixture(scope="class")
def channel_url():
    return 'https://discord.com/channels/1281160246110457919/1286673511733268552'
