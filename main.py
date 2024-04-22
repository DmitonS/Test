from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
names = []
def getNames():
    names = []
    list_items = getListItems('mm_company_list_item')
    for item in list_items:
        while 1:
            try:
                name = getContent(item, 'mm_company_list_link')
                print(name.text)
                # name = item.find_element(By.CLASS_NAME, 'mm_company_list_link')
                print("content - " + name.text)
                names.append(name.text)
                print("--------------------------------------------------")
                break
            except Exception as e:
                # None
                print("какая то ошибка")
                print(e)
                driver.refresh()
                time.sleep(20)
                time.sleep(1123213)

    return names
# Процесс ожидания прогрузки карточек
def getListItems(clas):
    list_items = None
    while True:
        list_items = driver.find_elements(By.CLASS_NAME, clas)
        # ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
        # list_items = WebDriverWait(driver, 5,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, clas)))
        # print(list_items.text)
        if len(list_items) == 0:
            time.sleep(1)
            print("карточек нету")
        else:
            print("нашел какие то карточки")
            # print(clas)
            # print(len(list_items))
            time.sleep(10)
            return list_items
def getContent(block, clas):
    list_items = None
    while True:
        list_items = block.find_element(By.CLASS_NAME, clas)
        if len(list_items) == 0:
            time.sleep(1)
            print("длинна текста 0")
        else:
            print("текст что то содержит")
            print(clas)
            time.sleep(10)
            return list_items
def parseCurrentPage():
    # РАБОТА С КАРТОЧКАМИ
    # list_items = getListItems('mm_company_list_item')
    # Выдача данных из карточки
    return getNames()

# Ожидание нижней панели
def getlastnum():
    lastnum = None
    while True:
        try:
            allpages = getListItems('bottom-element')
            # break
            return allpages[-1].text
        except Exception as e:
            print(e)
            print("жду нижнюю панель")
            time.sleep(1)

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
    

# lastnum = None
# while True:
#     try:
#         allpages = getListItems('bottom-element')
#         lastnum = allpages[-1].text
#         break
#     except Exception as e:
#         print(e)
#         print("жду нижнюю панель")
#         time.sleep(1)
#     # list_items = driver.find_elements(By.CLASS_NAME, clas)
#     # if len(list_items) == 0:
#     #     time.sleep(1)
#     #     print("sleep")
#     # else:
#     #     print("no sleep")
#     #     # print(len(list_items))
#     #     time.sleep(10)
#         # return list_items
# # print(driver.current_url)



# ОСНОВНОЙ БЛОК
# auth(driver)
# url = driver.current_url
links = []
# list_items = getListItems('mm_company_list_item')
# print(len(list_items))
# time.sleep(10123213)
# for i in list_items:
#     print(i.text)

# q = driver.find_element(By.XPATH, '//*[@id="widgetInner"]/div/div[1]/div[11]/div[6]')
# q.click()

# list_items = getListItems('mm_company_list_item')
# print(len(list_items))
# time.sleep(10)
# for i in list_items:
    # print(i.text)

while True:
        try:
            list_items = driver.find_element(By.XPATH, '//*[@id="widgetInner"]/div/div[1]')
            print(list_items.text)
            q = driver.find_element(By.XPATH, '//*[@id="widgetInner"]/div/div[1]/div[11]/div[6]')
            q.click()
            driver.refresh()
            print("__________________________________________________________________")
            # break
        except Exception as e:
            print(e)
            print("OUT xpath")
            time.sleep(1)
        # if len(list_items) == 0:
        #     time.sleep(1)
        #     print("карточек нету")
        # else:
        #     print("нашел какие то карточки")
        #     # print(clas)
        #     # print(len(list_items))
        #     time.sleep(10)
        #     return list_items

# for num in range(int(lastnum)):
#     list_items = getListItems('mm_company_list_item')
#     for i in list_items:
#         print(i.text)
#     thisurl = url + "%"+"3Fpage=" + str(num)
#     # driver.get(thisurl)
#     # driver.refresh()
#     time.sleep(5)
#     # links.append(thisurl)
#     # out = parseCurrentPage()
#     # driver.refresh()
#     # links.append(out)
#     # print(links)
print(links)
time.sleep(123123)


# print(links)
# def checkLastNumString(string):
#     if string[-1] 
# for numdiv in allpages:
#     try:
#         num = int(numdiv)
#         if num == nextnum:
#             # тут кликаем его

#     except Exception as e:
#         print(e)

# https://www.neftegaz-expo.ru/ru/visitors/mm/?cabinet&activityId=1466&visitorId=3491128#MatchMaking%2FCompany%2FList
# https://www.neftegaz-expo.ru/ru/visitors/mm/?cabinet&activityId=1466&visitorId=3491128#%2FMatchMaking%2FCompany%2FList%3Fpage=3

# Время работы цикла
time.sleep(23000000)