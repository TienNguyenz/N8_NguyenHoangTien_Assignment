# Call all modules and functions in the "driver.py" file
from driver import *

#Form Submission Functional
#TC1
def test_user_registration(driver):
    driver.find_element(By.LINK_TEXT, "Register").click()  
    time.sleep(2)
    driver.find_element(By.NAME, "cust_name").send_keys("testuser")
    driver.find_element(By.NAME,"cust_cname").send_keys("ABC Company")
    driver.find_element(By.NAME, "cust_email").send_keys("testuser1@example.com")
    driver.find_element(By.NAME, "cust_phone").send_keys("0397387337")
    driver.find_element(By.NAME, "cust_address").send_keys("123 Main St")
    
    country_select = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/form/div/div[2]/div[6]/span/span[1]/span/span[1]")
    country_select.click()  
    time.sleep(1)
    
    
    search_box = driver.find_element(By.CLASS_NAME, "select2-search__field")

    
    search_box.send_keys("Vietnam")
    search_box.send_keys(Keys.RETURN)
    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    driver.find_element(By.NAME, "cust_state").send_keys("Mien Nam")
    driver.find_element(By.NAME, "cust_zip").send_keys("112233")
    driver.find_element(By.NAME, "cust_password").send_keys("Password123")
    driver.find_element(By.NAME, "cust_re_password").send_keys("Password123")
    driver.find_element(By.NAME, "form1").click()  
    time.sleep(5)
    
    assert "Your registration is completed. Please check your email address to follow the process to confirm your registration." in driver.page_source ,"Email Address Already Exists." 

#TC2
def test_register_empty(driver):
    driver.find_element(By.LINK_TEXT, "Register").click()  
    time.sleep(2)
    driver.find_element(By.NAME, "cust_name").send_keys("")
    driver.find_element(By.NAME,"cust_cname").send_keys("")
    driver.find_element(By.NAME, "cust_email").send_keys("")
    driver.find_element(By.NAME, "cust_phone").send_keys("")
    driver.find_element(By.NAME, "cust_address").send_keys("")
    driver.find_element(By.NAME, "cust_city").send_keys("")
    driver.find_element(By.NAME, "cust_state").send_keys("")
    driver.find_element(By.NAME, "cust_zip").send_keys("")
    driver.find_element(By.NAME, "cust_password").send_keys("")
    driver.find_element(By.NAME, "cust_re_password").send_keys("")
    driver.find_element(By.NAME, "form1").click()  
    time.sleep(5)

    assert "Customer Name can not be empty." in driver.page_source
    assert "Email Address can not be empty" in driver.page_source
    assert "Phone Number can not be empty." in driver.page_source
    assert "Address can not be empty." in driver.page_source
    assert "You must have to select a country."in driver.page_source
    assert "City can not be empty."in driver.page_source
    assert "State can not be empty."in driver.page_source
    assert "City can not be empty."in driver.page_source
    assert "Zip Code can not be empty." in driver.page_source
    assert "Password can not be empty." in driver.page_source

#TC3
def test_registration_error_messages(driver):
    driver.find_element(By.LINK_TEXT, "Register").click()  
    time.sleep(2)

    driver.find_element(By.NAME, "cust_name").send_keys("testuser")
    driver.find_element(By.NAME,"cust_cname").send_keys("ABC Company")
    driver.find_element(By.NAME, "cust_phone").send_keys("0397387337")
    driver.find_element(By.NAME, "cust_address").send_keys("123 Main St")
    
    country_select = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/form/div/div[2]/div[6]/span/span[1]/span/span[1]")
    country_select.click()  
    time.sleep(1)
    
        
    search_box = driver.find_element(By.CLASS_NAME, "select2-search__field")

    
    search_box.send_keys("Vietnam")
    search_box.send_keys(Keys.RETURN)

    time.sleep(1)  

    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    driver.find_element(By.NAME, "cust_state").send_keys("Mien Nam")
    driver.find_element(By.NAME, "cust_zip").send_keys("112233")
    driver.find_element(By.NAME, "cust_password").send_keys("Password123")
    driver.find_element(By.NAME, "cust_re_password").send_keys("Password123")

    email_input = driver.find_element(By.NAME, "cust_email")
    driver.execute_script("arguments[0].removeAttribute('type')", email_input)
    driver.find_element(By.NAME, "cust_email").send_keys("invalid_email") 
    driver.find_element(By.NAME, "form1").click()  
    time.sleep(2)

    assert "Email address must be valid." in driver.page_source  

#TC4

def test_registration_max_username(driver):
    driver.find_element(By.LINK_TEXT, "Register").click()  
    time.sleep(2)
    driver.find_element(By.NAME, "cust_name").send_keys("u" * 30)
    driver.find_element(By.NAME,"cust_cname").send_keys("ABC Company")
    driver.find_element(By.NAME, "cust_email").send_keys("testuser2@example.com")
    driver.find_element(By.NAME, "cust_phone").send_keys("0397387337")
    driver.find_element(By.NAME, "cust_address").send_keys("123 Main St")
    
    country_select = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/form/div/div[2]/div[6]/span/span[1]/span/span[1]")
    country_select.click()  
    time.sleep(1)
    
    
    search_box = driver.find_element(By.CLASS_NAME, "select2-search__field")

    
    search_box.send_keys("Vietnam")
    search_box.send_keys(Keys.RETURN)
    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    driver.find_element(By.NAME, "cust_state").send_keys("Mien Nam")
    driver.find_element(By.NAME, "cust_zip").send_keys("112233")
    driver.find_element(By.NAME, "cust_password").send_keys("Password123")
    driver.find_element(By.NAME, "cust_re_password").send_keys("Password123")
    driver.find_element(By.NAME, "form1").click()  
    time.sleep(5)

    assert "Your registration is completed. Please check your email address to follow the process to confirm your registration." in driver.page_source  

#TC5
def test_registration_speciall(driver):
    driver.find_element(By.LINK_TEXT, "Register").click()  
    time.sleep(2)
    driver.find_element(By.NAME, "cust_name").send_keys("testuser")
    driver.find_element(By.NAME,"cust_cname").send_keys("ABC Company")
    driver.find_element(By.NAME, "cust_email").send_keys("testuser3@example.com")
    driver.find_element(By.NAME, "cust_phone").send_keys("039738@@@@@@!!!!!37")
    driver.find_element(By.NAME, "cust_address").send_keys("123 Main St")
    
    country_select = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/form/div/div[2]/div[6]/span/span[1]/span/span[1]")
    country_select.click()  
    time.sleep(1)
    
    
    search_box = driver.find_element(By.CLASS_NAME, "select2-search__field")

    
    search_box.send_keys("Vietnam")
    search_box.send_keys(Keys.RETURN)
    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    driver.find_element(By.NAME, "cust_state").send_keys("Mien Nam")
    driver.find_element(By.NAME, "cust_zip").send_keys("112233")
    driver.find_element(By.NAME, "cust_password").send_keys("Password123")
    driver.find_element(By.NAME, "cust_re_password").send_keys("Password123")
    driver.find_element(By.NAME, "form1").click()  
    time.sleep(5)
    assert "Invalid phone number." in driver.page_source  
