from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    browser.find_element_by_css_selector("button.trollface").click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    y = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()
 
finally:
    time.sleep(10)
    browser.quit()
