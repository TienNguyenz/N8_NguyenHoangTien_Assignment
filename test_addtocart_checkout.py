from tkinter.tix import Select
from driver import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import UnexpectedAlertPresentException

#TC1
def test_add_product_to_cart(driver):
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/ul/li[2]/a").click() 
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div[1]/div/div[2]/p/a").click()  
    time.sleep(2)

    driver.find_element(By.NAME, "form_add_to_cart").click()  

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/ul/li[3]/a").click()
    time.sleep(2)


    assert "Amazfit GTS 3 Smart Watch for Android iPhone" in driver.page_source  
    
#TC2
def test_remove_product_from_cart(driver):

    test_add_product_to_cart(driver)
    

    table = driver.find_element(By.CLASS_NAME, "table")


    rows = table.find_elements(By.TAG_NAME, "tr")
    
    product_name = "Amazfit GTS 3 Smart Watch for Android iPhone"  # Define the product name
    

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")


    if len(columns) > 1:

        product_name_in_cart = columns[2].text


        if product_name == product_name_in_cart:
                remove_button = driver.find_element(By.CLASS_NAME, "trash") 
                remove_button.click()
                time.sleep(2)


        assert product_name not in driver.page_source


#TC3
def test_update_item_quantity_in_cart(driver):
    test_add_product_to_cart(driver)


    table = driver.find_element(By.CLASS_NAME, "table")


    rows = table.find_elements(By.TAG_NAME, "tr")
    
    product_name = "Amazfit GTS 3 Smart Watch for Android iPhone"  
    

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        
    if len(columns) > 1:

        product_name_in_cart = columns[2].text  

        if product_name == product_name_in_cart:

            quantity_input = driver.find_element(By.CLASS_NAME, "input-text") 
            quantity_input.clear()
            quantity_input.send_keys("2")  
                

            driver.find_element(By.NAME, "form1").click()
            time.sleep(2)


        updated_quantity = driver.find_element(By.CLASS_NAME, "input-text").get_attribute("value")
        updated_price = driver.find_element(By.CLASS_NAME, "text-right").text 

        assert updated_quantity == "2"  
        assert "Total Price: $..." in updated_price  
    
#TC4
def test_bankDeposit_payment(driver):
    driver.get('http://localhost/Phpcode/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("testuser@example.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys("Password123")
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    driver.find_element(By.XPATH, "//button[text()='Update Billing and Shipping Info']").click()
    time.sleep(2)

    if not is_billing_address_filled(driver):
        update_billing_address(driver)
        
    if not is_shipping_address_filled(driver):
        update_shipping_address(driver)

    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Men").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Amazfit GTS 3 Smart Watch for Android iPhone").click()

    product_title = driver.find_element(By.CLASS_NAME, "p-title").text

    qty_input = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty[name='p_qty']")
    qty_input.clear()
    qty_input.send_keys("4")
    qty = qty_input.get_attribute("value")
    
    driver.find_element(By.NAME, "form_add_to_cart").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    time.sleep(2)

    table = driver.find_element(By.CLASS_NAME, "table")

    # Go through all the rows in the cart table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Go through each column in each row
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

    if len(columns) > 1:
        # Get product's name in cart
        product_name_in_cart = columns[2].text
        price_in_cart = columns[5]
        price = int(price_in_cart.text.strip('$'))
        qty_in_cart = columns.find_element(By.NAME, "quantity[]").get_attribute("value")
        total_price_in_cart = columns[7]
        total_price = int(total_price_in_cart.text.strip('$'))
        
        calculated_total_price = price * int(qty_in_cart)

        assert product_title == product_name_in_cart
        assert qty == qty_in_cart
        assert total_price == calculated_total_price

    # Click "Proceed to Checkout"
    driver.find_element(By.XPATH, "//a[@href='checkout.php']").click()
    time.sleep(2)
    driver.find_element(By.ID,"select2-advFieldsStatus-container").click()  

    bank_deposit_option = driver.find_element(By.XPATH, "//li[contains(text(), 'Bank Deposit')]")
    bank_deposit_option.click()
    time.sleep(2)

    driver.find_element(By.NAME, "transaction_info").send_keys("Please deliver it quickly and carefully!")
    time.sleep(2)

    # Click "Pay now"
    driver.find_element(By.NAME, "form3").click()
    time.sleep(2)

    success_message = driver.find_element(By.CSS_SELECTOR, "h3").text

    assert "Congratulation! Payment is successful." in success_message
    

# Test the checkout process, using "Paypal" payment method
def test_Paypal_payment(driver):
    driver.get('http://localhost/Phpcode/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("testuser@example.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys("Password123")
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    driver.find_element(By.XPATH, "//button[text()='Update Billing and Shipping Info']").click()
    time.sleep(2)

    if not is_billing_address_filled(driver):
        update_billing_address(driver)
        
    if not is_shipping_address_filled(driver):
        update_shipping_address(driver)

    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Men").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Amazfit GTS 3 Smart Watch for Android iPhone").click()

    product_title = driver.find_element(By.CLASS_NAME, "p-title").text
    time.sleep(2)

    qty_input = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty[name='p_qty']")
    qty_input.clear()
    qty_input.send_keys("4")
    qty = qty_input.get_attribute("value")
    
    driver.find_element(By.NAME, "form_add_to_cart").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    time.sleep(2)

    table = driver.find_element(By.CLASS_NAME, "table")

    # Go through all the rows in the cart table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Go through each column in each row
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

    if len(columns) > 1:
        # Get product's name in cart
        product_name_in_cart = columns[2].text
        price_in_cart = columns[5]
        price = int(price_in_cart.text.strip('$'))
        qty_in_cart = columns.find_element(By.NAME, "quantity[]").get_attribute("value")
        total_price_in_cart = columns[7]
        total_price = int(total_price_in_cart.text.strip('$'))
        
        calculated_total_price = price * int(qty_in_cart)

        assert product_title == product_name_in_cart
        assert qty == qty_in_cart
        assert total_price == calculated_total_price

    # Click "Proceed to Checkout"
    driver.find_element(By.XPATH, "//a[@href='checkout.php']").click()
    time.sleep(2)

    
    driver.find_element(By.ID, "select2-advFieldsStatus-container").click() 

    paypal_option = driver.find_element(By.XPATH, "//li[contains(text(), 'PayPal')]")
    paypal_option.click()
    time.sleep(2)

    # Click "Pay now"
    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

    assert "https://www.paypal.com/webapps/shoppingcart/error?flowlogging_id=f7930417dd231&code=GENERIC_ERROR&mfid=1730703263286_f7930417dd231" in driver.current_url

# This is a function to fill all fields of Billing Address to Checkout
def update_billing_address(driver):
    driver.find_element(By.NAME, "cust_b_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_cname").send_keys("SGU")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_phone").send_keys("0383161867")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_b_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_address").send_keys("An Duong Vuong")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)
    
    driver.find_element(By.NAME, "cust_b_state").send_keys("Mien Nam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_zip").send_keys(112233)
    time.sleep(1.5)


# This is a function to fill all fields of Shipping Address to Checkout
def update_shipping_address(driver):
    driver.find_element(By.NAME, "cust_s_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_cname").send_keys("SGU")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_phone").send_keys("0383161867")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_s_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)
    
    driver.find_element(By.NAME, "cust_s_state").send_keys("Mien Nam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_zip").send_keys(112233)
    time.sleep(1.5)


# This is a function to check if all fields of Billing Address are filled and updated
def is_billing_address_filled(driver):
    required_fields = ["cust_b_name", "cust_b_cname", "cust_b_phone", "cust_b_address", "cust_b_city", "cust_b_state", "cust_b_zip"]
    for field_name in required_fields:
        field_value = driver.find_element(By.NAME, field_name).get_attribute("value")
        if not field_value:
            return False
    return True


# This is a function to check if all fields of Shipping Address are filled and updated
def is_shipping_address_filled(driver):
    required_fields = ["cust_s_name", "cust_s_cname", "cust_s_phone", "cust_s_address", "cust_s_city", "cust_s_state", "cust_s_zip"]
    for field_name in required_fields:
        field_value = driver.find_element(By.NAME, field_name).get_attribute("value")
        if not field_value:
            return False
    return True
