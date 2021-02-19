from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # answer = browser.find_element_by_id("answer")
    browser.find_element_by_id("answer").send_keys(y)
    
    # checkbx = browser.find_element_by_id("robotCheckbox")
    browser.find_element_by_id("robotCheckbox").click()
    
    # radiobtn = browser.find_element_by_id("robotsRule")
    browser.find_element_by_id("robotsRule").click()
    
    # submit = browser.find_element_by_css_selector("button.btn")
    browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
