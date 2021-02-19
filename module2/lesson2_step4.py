from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # browser.execute_script("alert('Robots at work');")
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True
    
finally:
    time.sleep(15)
    browser.quit()
