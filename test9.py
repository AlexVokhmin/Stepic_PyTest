from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'test.txt'
    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys('fafd')
    browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys('fafd')
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys('fafd')
    browser.find_element(By.ID, 'file').send_keys(os.path.join(current_dir, file_name))

    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
