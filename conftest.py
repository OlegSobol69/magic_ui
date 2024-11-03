from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from pages.account_create_page import AccountCreate
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale
import pytest
import os

base_path = os.path.dirname(os.path.dirname(__file__))
argument_path = os.path.join(base_path, 'SeleniumProfile')


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument(f"user-data-dir={argument_path}")
    chrome_driver = webdriver.Chrome(options)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(5)


@pytest.fixture()
def account_create_page(driver):
    return AccountCreate(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return Sale(driver)
