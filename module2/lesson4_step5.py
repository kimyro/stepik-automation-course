# пример реализации неявного ожидания элементов страницы (Implicit wait)
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
    
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(5) # time.sleep пока используем для того, чтобы визуально оценить результат теста
    browser.quit()
