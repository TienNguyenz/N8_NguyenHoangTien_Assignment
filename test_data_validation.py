from driver import *

#TC1
def test_validate_data_with_special_characters(driver):
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/contact.php")
    time.sleep(2)

    name_field = driver.find_element(By.NAME, "visitor_name")
    phone_field = driver.find_element(By.NAME, "visitor_phone")
    email_field = driver.find_element(By.NAME, "visitor_email") 
    message_field = driver.find_element(By.NAME, "visitor_message")

    name_field.clear()
    name_field.send_keys("!@#$%^&*()")
    time.sleep(3)
    phone_field.clear()
    phone_field.send_keys("123-456-7890")
    time.sleep(3)
    email_field.clear()
    email_field.send_keys("test@email.com")  
    time.sleep(3)
    message_field.clear()
    message_field.send_keys("Test message with special characters !@#$%^&*()")
    time.sleep(3)
    send_message_button = driver.find_element(By.NAME, "form_contact")
    send_message_button.click()
    time.sleep(5)
    
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message")
    assert "Special characters are not allowed" in error_message.text

#TC2
def test_user_registration_min_password(driver):
    driver.find_element(By.LINK_TEXT, "Register").click() 
    time.sleep(2)
    driver.find_element(By.NAME, "cust_name").send_keys("testuser")
    driver.find_element(By.NAME,"cust_cname").send_keys("ABC Company")
    driver.find_element(By.NAME, "cust_email").send_keys("testuser4@example.com")
    driver.find_element(By.NAME, "cust_phone").send_keys("0397387337")
    driver.find_element(By.NAME, "cust_address").send_keys("123 Main St")
    
    country_select = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/form/div/div[2]/div[6]/span/span[1]/span/span[1]")
    country_select.click()  
    time.sleep(1)
    
    country_option = country_select.find_element(By.XPATH, "//option[text()='Vietnam']")
    country_option.click()  
    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    driver.find_element(By.NAME, "cust_state").send_keys("Mien Nam")
    driver.find_element(By.NAME, "cust_zip").send_keys("112233")
    driver.find_element(By.NAME, "cust_password").send_keys("123")
    driver.find_element(By.NAME, "cust_re_password").send_keys("123")
    driver.find_element(By.NAME, "form1").click() 
    time.sleep(5)
    
    assert "Password is too short" in driver.page_source
    