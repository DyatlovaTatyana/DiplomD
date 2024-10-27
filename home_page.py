import time
import pyautogui
from base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.channel_url = 'https://discord.com/channels/1281160246110457919/1286673511733268552'

    # Локатор для сервера диплома
    def server_diplom_locator(self):
        return By.XPATH, f'//div[@class="childWrapper_f90abb childWrapperNoHoverBg_f90abb acronym_f90abb"]'

    # Локатор для канала 4
    def channel_locator(self):
        return By.XPATH, f'//div[text()="4"]'

    # Локатор для ввода сообщения
    def message_input_locator(self):
        return By.XPATH, f'//div[@role="textbox"]'

    #Локатор для сообщения (общий на все, т.е. если сообщения будет 2, то будет 2 совпадения)
    def message_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="markup_f8f345 messageContent_f9f2ca"]'

    #Локатор для формы сообщения
    def form_message_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]'

    # Локатор для редактирования
    def actions_button_edit_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="buttonContainer_f9f2ca"]//div[@aria-label="Действия с сообщениями"]//div[@aria-label="Изменить"]'

    #Локатор для реакции на сообщение
    def actions_button_reactoin_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="buttonContainer_f9f2ca"]//div[@aria-label="Действия с сообщениями"]//div[@aria-label="Нажмите, чтобы отреагировать эмодзи thumbsup"]'

    # Локатор для троеточия "Ещё"
    def actions_button_more_locator(self):
        return By.XPATH, f'//div[@aria-roledescription="Сообщение"]//div[@class="buttonContainer_f9f2ca"]//div[@aria-label="Действия с сообщениями"]//div[@aria-label="Ещё"]'

    #Локатор для кнопки "удалить сообщение"
    def delete_message_button_locator(self):
        return By.XPATH, f'//div[@id="message-actions-delete"]'

    # Локатор для кнопки подтвердить "удалить сообщение"
    def delete_message_confirm_button_locator(self):
        return By.XPATH, f'//button[@type="submit"]'

    # Локатор для реакции под сообщение
    def reaction_locator(self):
        return By.XPATH, f'//div[@class="reactionInner_ec6b19"]'

    #Локатор для упомянутого пользователя
    def mention_user_locator(self):
        return By.XPATH, f'//div[@class="markup_f8f345 messageContent_f9f2ca"]//span[@role="button"]'

    #Локатор для несущ упоминания
    def mention_non_exist_user_locator(self):
        return By.XPATH, f'//div[@class="markup_f8f345 messageContent_f9f2ca"]'

    #Метод для вытаскивания атрибута у упомянутого пользователя (для дальнейшей проверки)
    def is_mention_user_exists(self):
        return self.find_element(self.mention_user_locator()).get_attribute("role")

     # Метод для вытаскивания атрибута у несущ упомянутого пользователя (для дальнейшей проверки)
    def is_mention_user_non_exists(self):
        return self.find_element(self.mention_non_exist_user_locator()).get_attribute("role")

    #Метод для проверки видимости реакции
    def is_reactoin_displayed(self):
        return self.find_element(self.reaction_locator())

    #Метод для удаления реакции
    def delete_reaction(self):
        self.click(self.reaction_locator())

    # Метод для редактирования сообщения
    def edit_message(self):
        self.hover(self.form_message_locator())
        self.click(self.actions_button_edit_locator())
        pyautogui.press('backspace', presses=6)
        pyautogui.typewrite("PyCharm")
        pyautogui.press('enter')

    #Метод для удаления сообщения
    def delete_message(self):
        self.hover(self.form_message_locator())
        self.click(self.actions_button_more_locator())
        self.click(self.delete_message_button_locator())
        self.click(self.delete_message_confirm_button_locator())

    #Метод для реакции через меню действий
    def send_reactoin(self):
        self.hover(self.form_message_locator())
        self.click(self.actions_button_reactoin_locator())

    #Метод для вытаскивания текста из сообщени
    def is_message_send(self):
        return self.find_element(self.message_locator()).text
        # return self.find_element(self.message_locator())

    # Метод для клика по Серверу диплома
    def clic_to_server_diplom(self):
        self.hover(self.server_diplom_locator())
        self.click(self.server_diplom_locator())

    # Метод для клика по 4ому каналу
    def clic_to_channel(self):
        self.click(self.channel_locator())

    # Метод для ввода и отправки сообщения
    def send_message_in_channel(self,text):
        self.send_message(self.message_input_locator(),{text})

    # Метод для открытия страницы с каналом
    # def open_channel(self):
    #     self.driver.get(self.channel_url)
