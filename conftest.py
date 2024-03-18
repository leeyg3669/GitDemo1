import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
     chrome_service = Options()
     chrome_service.add_experimental_option("detach", True)
     driver = webdriver.Chrome(options=chrome_service)

    elif browser_name == "firefox":
        service_obj = Service("C:/Users/Administrator/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == "Edge":
        service_obj = Service("C:/Users/Administrator/Downloads/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
