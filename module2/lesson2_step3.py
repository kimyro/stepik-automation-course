from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(num1 + num2))
    
    browser.find_element_by_css_selector("button.btn").click()
    
finally:
    time.sleep(10)
    browser.quit()
