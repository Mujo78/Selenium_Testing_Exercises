from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_tests import success_login

def profile_info(driver):
    wait = WebDriverWait(driver, 10)
    success_login(driver)

    nav_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/profile']")))
    nav_profile.click()

    root_div = wait.until(EC.visibility_of_element_located((By.XPATH, "//div/div/div[3]")))
    founded_element = root_div.find_element(By.XPATH, "//div/div/h2")

    assert founded_element.text == "test.test"

def cart_check_empty(driver):
    wait = WebDriverWait(driver, 30)
    success_login(driver)

    cart_button = wait.until(EC.element_to_be_clickable((By.ID, "cart_btn")))
    cart_button.click()

    offcanvas_cart_element = wait.until(EC.visibility_of_element_located((By.ID, "alert_message")))

    assert offcanvas_cart_element.text == "Empty"


def comment_success_fn(wait, comment_to_send):
    nav_contact = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact']")))
    nav_contact.click()

    name = wait.until(EC.element_to_be_clickable((By.NAME, "name")))
    name.send_keys("Mujo78")

    email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    email.send_keys("example@gmail.com")

    comment = wait.until(EC.element_to_be_clickable((By.NAME, "comment")))
    comment.send_keys(comment_to_send)

    btn_submit = wait.until(EC.element_to_be_clickable((By.ID, "comment_btn")))
    btn_submit.click()

def comment_post(driver):
    wait = WebDriverWait(driver, 10)
    comment_success_fn(wait, "My new comment will be here from now on...")

    toast_body = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
    toast_body_second_element = toast_body.find_elements(By.XPATH, "//div[2]")[1]

    assert toast_body_second_element.text == "Comment successfully added!"

def comment_required(driver):
    wait = WebDriverWait(driver, 10)
    comment_success_fn(wait, "")

    error_message = wait.until(EC.visibility_of_element_located((By.ID, "errorMessage")))
    assert error_message.text == "Comment is required!"

def logout(driver):
    wait = WebDriverWait(driver, 10)
    success_login(driver)

    nav_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/profile']")))
    nav_profile.click()

    logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_btn")))
    logout_button.click()

    assert wait.until(EC.element_to_be_clickable((By.ID, "login_btn_modal"))) is not None

def test_run(driver):
    cart_check_empty(driver)
    #comment_post(driver)
    #comment_required(driver)
    #logout(driver)
    
    print("Successfully done!")