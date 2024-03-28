from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def registration_fn(wait, first_name_to_input):
    registration_button = wait.until(EC.element_to_be_clickable((By.ID, "signup_btn_modal")))
    registration_button.click()

    first_name = wait.until(EC.element_to_be_clickable((By.NAME, "first_name")))
    first_name.send_keys(first_name_to_input)

    last_name = wait.until(EC.element_to_be_clickable((By.NAME, "last_name")))
    last_name.send_keys("seventy-eight")

    phone_number = wait.until(EC.element_to_be_clickable((By.NAME, "phone_number")))
    phone_number.send_keys("111222333444")

    gender = wait.until(EC.element_to_be_clickable((By.NAME, "gender")))
    gender.send_keys("Male")

    city = wait.until(EC.element_to_be_clickable((By.NAME, "city")))
    city.send_keys("Sarajevo")

    address = wait.until(EC.element_to_be_clickable((By.NAME, "address")))
    address.send_keys("Address")

    username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    username.send_keys("Mujo78")
    
    email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    email.send_keys("example@gmail.com")

    password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    password.send_keys("newpassword")

    confirmpassword = wait.until(EC.element_to_be_clickable((By.NAME, "confirmPassword")))
    confirmpassword.send_keys("newpassword")

    submit = wait.until(EC.element_to_be_clickable((By.ID, "signup_btn")))
    submit.click()

def registration_success(driver):
    wait = WebDriverWait(driver, 10)
    registration_fn(wait, "Mujo")

    toast_body = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
    toast_body_second_element = toast_body.find_elements(By.XPATH, "//div[2]")[1]

    assert toast_body_second_element.text == "Account successfully created!"

def first_name_required(driver):
    wait = WebDriverWait(driver, 10)
    registration_fn(wait, "")

    error_message = wait.until(EC.visibility_of_element_located((By.ID, "errorMessage")))
    
    assert error_message.text == "First name is required"

def test_registration(driver):
    registration_success(driver)
    #first_name_required(driver)

    print("Successfull registration!")