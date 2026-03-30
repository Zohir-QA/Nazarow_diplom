from pydoc import browse

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import requests


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    b = request.param
    if b == 'edge':
        browser = webdriver.Edge()
    else:
        browser = webdriver.Chrome()

    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser # закрывает, после него не чего не писать
    browser.quit()