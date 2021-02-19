from selenium import webdriver
import time, os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    browser.find_element_by_css_selector('[name="firstname"]').send_keys("Anakin")
    browser.find_element_by_css_selector('[name="lastname"]').send_keys("Skywalker")
    browser.find_element_by_css_selector('[name="email"]').send_keys("darth.vader66@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    browser.find_element_by_id("file").send_keys(os.path.join(current_dir, 'test-file.txt'))
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(15)
    browser.quit()
