from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# Создание объекта опций
options = Options()
# Инициализация веб-драйвера с использованием объекта опций
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
driver.get('https://www.neftegaz-expo.ru/ru/visitors/mm/?auto=mm&step=step1')
time.sleep(5)

# ПРОЦЕСС РЕГИСТРАЦИИ
# Присваиваем переменную для поля логина
xpath_login = '//*[@id="EmailText"]'
# Записываем поиск этого элемента
input_element = driver.find_element(By.XPATH, xpath_login)
# print("111")
# Производим запись
input_element.send_keys("e.maksimova@e-shkaf.su")

# Присваиваем переменную для кнопки
xpath_login_button = '//*[@id="expodatakrat"]/div/div/div[2]/div/div[2]/button'
# Ищем кнопку
input_element = driver.find_element(By.XPATH, xpath_login_button)
# Жмем на кнопку
input_element.click()
# Время ожидания
time.sleep(5)

# Присваиваем переменную для поля пароля
xpath_password = '//*[@id="Password"]'
# Записываем поиск этого элемента
input_element = driver.find_element(By.XPATH, xpath_password)
# Производим запись
input_element.send_keys("231287")

# Присваиваем переменную для кнопки
xpath_password_button = '//*[@id="expodatakrat"]/div/div/div[2]/div[1]/div[3]/button'
# Ищем кнопку
input_element = driver.find_element(By.XPATH, xpath_password_button)
# Жмем на кнопку
input_element.click()
# Время ожидания
time.sleep(5)
# Обновление страницы для перехода на другой язык
driver.refresh()

# Присваиваем переменную для панели страниц
xpath_number_panel = '//*[@id="widgetInner"]/div/div[1]/div[11]'
#Записываем поиск этого элемента
number_panel = driver.find_element(By.XPATH, xpath_number_panel)

time.sleep(23000000)