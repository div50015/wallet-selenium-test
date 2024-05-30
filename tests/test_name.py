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
    # shadow_host = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "remoteComponent")))
    # shadow_root = shadow_host.shadow_root
    # shadow_form = shadow_root.find_element((By.CSS_SELECTOR, 'form'))

    shadow_form: webdriver = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, "remoteComponent")).shadow_root.find_element(By.CSS_SELECTOR, 'form')
    # shadow_div: webdriver = wait.until(lambda driver: shadow_form.find_element(By.XPATH, ".//div[@data-wi='user-name']"))
    # shadow_div = shadow_form.find_element(By.XPATH, ".//div[@data-wi='user-name']")
    until1(shadow_form)
    driver.close()

def until1(driver):
    wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[@data-wi='user-name']")))