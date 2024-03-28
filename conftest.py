import pytest;

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

@pytest.fixture
def driver():
    try:
        chromedriver_autoinstaller.install()
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=service)
        driver.maximize_window()
        driver.get("http://localhost:3000/")        
        return driver
    except Exception as e:
        print("Error founded:", e)