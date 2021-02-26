from selenium import webdriver
import unittest

class TestAbs(unittest.TestCase):
    def test_check_registration_form1(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element_by_css_selector("input.first[required]").send_keys("Anakin")
        browser.find_element_by_css_selector("input.second[required]").send_keys("Skywalker")
        browser.find_element_by_css_selector("input.third[required]").send_keys("darth.vader66@gmail.com")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Cannot complete the registration, please check all required fields")
        browser.quit()

    def test_check_registration_form2(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get("http://suninjuly.github.io/registration2.html")
        browser.find_element_by_css_selector("input.first[required]").send_keys("Anakin")
        browser.find_element_by_css_selector("input.second[required]").send_keys("Skywalker")
        browser.find_element_by_css_selector("input.third[required]").send_keys("darth.vader66@gmail.com")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Cannot complete the registration, please check all required fields")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
