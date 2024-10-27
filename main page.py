from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.by import By

# Выберите нужный драйвер: ChromeDriver, GeckoDriver (для Firefox) и т.д.
driver = webdriver.Edge()

# Открываем веб-страницу и заходим в профиль
driver.get('https://discord.com/login')
time.sleep(5)
element2=driver.find_element(By.XPATH, '//input[@id="uid_7"]')
element2.click()
element2.send_keys("dyatlova1108@gmail.com")
time.sleep(5)

element3=driver.find_element(By.XPATH, '//input[@id="uid_9"]')
element3.click()
element3.send_keys("Dyatlova1108!")

element1=driver.find_element(By.XPATH, '//button//div[text()="Вход"]')
element1.click()
time.sleep(10)

#Кликаем по сервеву диплома, переходим на канал основной и кликаем на ввод сообщения
element4=driver.find_element(By.XPATH, '//div[text()="СерверДилом"]')
element4.click()
time.sleep(5)

element5=driver.find_element(By.XPATH, '//div[text()="4"]')
element5.click()
time.sleep(5)

element6=driver.find_element(By.XPATH, '//div[@role="textbox"]')
element6.click()

element6.send_keys("Привет @пупкин как твое ничего?")
pyautogui.press('enter')
time.sleep(5)

element7=driver.find_element(By.XPATH, '//div[@class="markup_f8f345 messageContent_f9f2ca"]')

assert element7.get_attribute("role") == None

# element7 = driver.find_element(By.XPATH, '//div[@aria-roledescription="Сообщение"]')
# print(element7.text)
# time.sleep(5)










# Закрываем браузер после завершения теста
driver.quit()