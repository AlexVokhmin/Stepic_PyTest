from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    val1 = browser.find_element(By.ID, 'num1').text
    val2 = browser.find_element(By.ID, 'num2').text
    res = int(val1) + int(val2)
    sel = Select(browser.find_element(By.ID, 'dropdown'))
    sel.select_by_value(str(res))


    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
