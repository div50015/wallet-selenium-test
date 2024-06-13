import pytest
import allure
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=5, ignored_exceptions=(WebDriverException,))


def test_name():
    driver.get('https://koshelek.ru/authorization/signup')
    shadow_host = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "remoteComponent")))
    shadow_root = shadow_host.shadow_root
    element_form: webdriver = shadow_root.find_element(By.CSS_SELECTOR, 'form')
    element_div: webdriver = wait.until(lambda driver: element_form.find_element(By.XPATH, ".//div[@data-wi='user-name']"))
    element_input: webdriver = wait.until(lambda driver: element_div.find_element(By.CSS_SELECTOR, "input"))
    element_input.send_keys(f'UseR')
    element_form.click()
    element_span: driver = wait.until(lambda driver: element_div.find_element(By.XPATH, ".//span[@class='k-text']"))
    assert element_span.text == 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы'

    driver.close()

def until1(driver):
    wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[@data-wi='user-name']")))