from selenium import webdriver
import time, math, pytest

lessons = ["https://stepik.org/lesson/236895/step/1", 
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"]

@pytest.fixture
def browser():
    print("\nStarting browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nExiting browser...")
    browser.quit()

@pytest.mark.parametrize('link', lessons)
def test_check_optional_feedback(browser, link):
    browser.implicitly_wait(5)
    browser.get(f"{link}")
    browser.find_element_by_css_selector("textarea.string-quiz__textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector("button.submit-submission").click()
    opt_feedback = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    
    assert "Correct!" == opt_feedback, f"Expected 'Correct!' in optional feedback, but got '{opt_feedback}' instead."