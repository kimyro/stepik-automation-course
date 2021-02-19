from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    # вводим значение функции в поле
    browser.find_element_by_id("answer").send_keys(y)
    
    # выбираем checkbox "I`m the robot"
    browser.find_element_by_id("robotCheckbox").click()
    
    # переключаем radiobutton на "Robots rule"
    browser.find_element_by_id("robotsRule").click()
    
    # отправляем результат
    browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
