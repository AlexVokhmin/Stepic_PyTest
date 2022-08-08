from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc (x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, 'div.form-group .nowrap:nth-child(2)')
    x = calc(x.text)
    browser.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(x)
    browser.find_element(By.CSS_SELECTOR, 'input.form-check-input').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
