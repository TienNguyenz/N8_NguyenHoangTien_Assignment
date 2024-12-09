# Call all modules and functions in the "driver.py" file
from driver import *

def test_mobile_layout(driver):
    driver.set_window_size(375, 667)
    time.sleep(3)  
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/index.php")
    time.sleep(3)  

    try:
        mobile_header = driver.find_element(By.CLASS_NAME, "top")  
        assert mobile_header.is_displayed(), "Mobile header is not displayed."


        mobile_menu = driver.find_element(By.CLASS_NAME, "menu-mobile")  
        assert mobile_menu.is_displayed(), "Mobile menu is not displayed."

        
        page_width = driver.execute_script("return window.innerWidth;")
        assert page_width <= 768, "Page is not optimized for mobile devices."

        print("Mobile layout test passed successfully.")

    except AssertionError as e:
        pytest.fail(f"Mobile layout test failed: {e}")

#TC02
def test_layout_rotation_consistency(driver):

    driver.set_window_size(375, 667)
    time.sleep(3)  
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/index.php")
    time.sleep(2) 


    try:

        mobile_header = driver.find_element(By.CLASS_NAME, "top") 
        assert mobile_header.is_displayed()

        mobile_menu = driver.find_element(By.CLASS_NAME, "menu-mobile")
        assert mobile_menu.is_displayed()

 
        page_width = driver.execute_script("return window.innerWidth;")
        assert page_width <= 768


    except AssertionError as e:
        pytest.fail(f"Mobile layout test failed: {e}")


    driver.set_window_size(667, 375)  
    time.sleep(2)


    try:

        mobile_header = driver.find_element(By.CLASS_NAME, "top") 
        assert mobile_header.is_displayed()
        mobile_menu = driver.find_element(By.CLASS_NAME, "menu-mobile") 
        assert mobile_menu.is_displayed()

        page_width = driver.execute_script("return window.innerWidth;")
        assert page_width > 768

    except AssertionError as e:
        pytest.fail(f"Mobile layout test failed: {e}")