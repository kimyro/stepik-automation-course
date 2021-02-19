from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    browser.find_element_by_css_selector("button.btn").click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    y = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()
 
finally:
    time.sleep(15)
    browser.quit()
