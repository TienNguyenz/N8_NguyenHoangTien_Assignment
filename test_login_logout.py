# Call all modules and functions in the "driver.py" file
from driver import *

#Login/logout Functional:
#TC1

def test_user_login(driver):
    driver.find_element(By.LINK_TEXT, "Login").click() 
    time.sleep(2)
    driver.find_element(By.NAME, "cust_email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "cust_password").send_keys("Password123")
    driver.find_element(By.NAME, "form1").click()  
    time.sleep(2)
    assert "Welcome to the Dashboard" in driver.page_source  

#TC2
def test_user_invalid_login_pass(driver):
    driver.find_element(By.LINK_TEXT, "Login").click()  
    time.sleep(2)
    driver.find_element(By.NAME, "cust_email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "cust_password").send_keys("Password#123")
    driver.find_element(By.NAME, "form1").click() 
    time.sleep(2)
    assert "Passwords do not match." in driver.page_source  

#TC3
def test_user_invalid_login_email(driver):
    driver.find_element(By.LINK_TEXT, "Login").click()  
    time.sleep(2)
    driver.find_element(By.NAME, "cust_email").send_keys("testuse1r@example.com")
    driver.find_element(By.NAME, "cust_password").send_keys("Password#123")
    driver.find_element(By.NAME, "form1").click() 
    time.sleep(2)
    assert "Email Address does not match." in driver.page_source  

#TC4
def test_user_empty_login(driver):
    driver.find_element(By.LINK_TEXT, "Login").click()  
    time.sleep(2)
    driver.find_element(By.NAME, "cust_email").send_keys("")
    driver.find_element(By.NAME, "cust_password").send_keys("")
    driver.find_element(By.NAME, "form1").click() 
    time.sleep(2)
    assert "Email and/or Password can not be empty." in driver.page_source  

#TC5
def test_user_logout(driver):
    test_user_login(driver)  
    driver.find_element(By.LINK_TEXT, "Logout").click()  
    time.sleep(2)

    assert "Customer Login" in driver.page_source 