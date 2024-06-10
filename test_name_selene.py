import pytest
from selene import browser, have, be
from selenium import webdriver
from time import sleep

def test_name():
    browser.config.timeout = 7.0
    # driver_options = webdriver.ChromeOptions()
    # browser.config.driver_options = driver_options

    browser.open('https://koshelek.ru/authorization/signup')
    # sleep(10)
    # browser.all('.v-btn__content').should(have.size(5))
    # sleep(10)
    browser.element('.remoteComponent').execute_script('return arguments[0].shadowRoot',)

    browser.quit()