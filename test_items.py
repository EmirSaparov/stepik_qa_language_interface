import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_button(browser):
    browser.get(link)
    add_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    time.sleep(30)
    assert add_button.is_displayed(), 'Button is not enable'
