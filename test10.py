import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.select import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    browser.switch_to.alert.accept()

    x = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(x)
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    text = browser.switch_to.alert.text
    text = text.split(': ')[-1]
    pyperclip.copy(text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
