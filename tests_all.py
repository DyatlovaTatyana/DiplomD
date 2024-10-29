import time
import pytest
from home_page import HomePage
from login_page import LoginPage
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Пишем какое сообщение хотим отправить
text = "Привет, пора приступать к диплому, торопись! А еще меня отправили из пучарм"
text_mention = "Привет @BEE-diploma#7805 как твое ничего?"
text_mention_non_exist_user = "Привет @пупкин как твое ничего?"

@pytest.mark.usefixtures("init_driver", "base_url")
class TestMessage:
   def test_login_me(self, base_url):
        # Инициализация страницы
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.open_page()
        time.sleep(3)
        login_page.login_user()
        time.sleep(5)
        login_page.click_login()
        time.sleep(10)
        print("Текущий урл: ", self.driver.current_url)
        # Проверяем, что открылась страница с моими каналами
        assert self.driver.current_url == 'https://discord.com/channels/@me'
    
    def test_send_message(self, base_url):
        # Инициализация страницы
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        base_page = BasePage(self.driver)

        # # Открытие страницы
        # base_page.open_page('https://discord.com/channels/@me')
        # time.sleep(5)

        # # Логинимся
        # login_page.login_user()
        # time.sleep(5)
        # print("Текущий урл: ", self.driver.current_url)
        # Проверяем, что открылась страница с моими каналами
        # assert self.driver.current_url == 'https://discord.com/channels/@me'
        # Переходим в канал "4"
        home_page.clic_to_server_diplom()
        time.sleep(3)
        home_page.clic_to_channel()
        time.sleep(3)

        # Отправка сообщения
        home_page.send_message_in_channel(text)

        # Проверка, что сообщение отправилось в диалог
        # assert home_page.is_message_send().is_displayed() == True
        message_send = home_page.is_message_send()
        assert message_send.count(text) == 1, "Сообщение не отправлено"
        # print(self.driver.current_url)

    def test_edit_message(self,base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        #Нажимаем редактировать сообщение
        home_page.edit_message()
        time.sleep(3)

        #Проверка, что новый текст с пометкой (изменено)
        new_message = home_page.is_message_send()
        assert new_message.count('изменено') == 1


    def test_add_reacrion(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Поставить реакцию
        home_page.send_reactoin()
        time.sleep(3)
        # Проверка, что реакция появилась под сообщением
        assert home_page.is_reactoin_displayed().is_displayed() == True, "Реакция на сообщение отсутствует"


    def test_delete_reacrion(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Удалить реакцию
        home_page.delete_reaction()

        # Проверка, что реакция исчезла
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(home_page.reaction_locator()))


    def test_delete_message(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Удалить сообщение
        home_page.delete_message()

        # Проверка, что сообщение удалилось
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(home_page.form_message_locator()))


    def test_send_message_with_mention(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Отправка сообщения
        home_page.send_message_in_channel(text_mention)
        time.sleep(3)

        # Проверка, что упомянутый пользователь существует
        role = home_page.is_mention_user_exists()
        assert role == "button"

        # Удалить сообщение
        home_page.delete_message()
        time.sleep(3)

    def test_send_message_with_non_exist_user(self, base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Отправка сообщения
        home_page.send_message_in_channel(text_mention_non_exist_user)

        # Проверка, что упомянутый пользователь не существует
        assert home_page.is_mention_user_non_exists() == None

        # Удалить сообщение
        home_page.delete_message()
        time.sleep(3)

    def test_send_empty_message(self,base_url):
        # Инициализация страницы
        home_page = HomePage(self.driver)

        # Отправка сообщения
        home_page.send_message_in_channel("    ")

        # Проверка, что никакого сообщения не появилось
        assert WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(home_page.form_message_locator()))
