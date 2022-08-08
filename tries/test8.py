from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.select import Select

def calc (x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    x = calc(browser.find_element(By.ID, 'input_value').text)
    but = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    but.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
