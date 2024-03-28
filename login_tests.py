from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_fn(wait, username, password):
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login_btn_modal")))
    login_button.click()
    
    username_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    username_input.send_keys(username)

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    password_input.send_keys(password)
    
    login_button_to_click = wait.until(EC.element_to_be_clickable((By.ID, "login_btn")))
    login_button_to_click.click()

def success_login(driver):
    wait = WebDriverWait(driver, 10)
    login_fn(wait, "test.test", "1234567890")

    assert wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/profile']"))) is not None

def wrong_username_or_password(driver):
    wait = WebDriverWait(driver, 10)
    login_fn(wait, "name.name", "password.password")

    error_message = wait.until(EC.visibility_of_element_located((By.ID, "errorMessage")))
    assert error_message.text == "Incorrect username or password!"

def password_required(driver):
    wait = WebDriverWait(driver, 10)
    login_fn(wait, "name.name", "")

    error_message = wait.until(EC.visibility_of_element_located((By.ID, "errorMessage")))
    assert error_message.text == "Password is required!"

def test_login(driver):
    success_login(driver)
    #wrong_username_or_password(driver)
    #password_required(driver)

    print("Test passed successfully")

    