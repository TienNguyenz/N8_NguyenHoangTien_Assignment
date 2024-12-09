# Call all modules and functions in the "driver.py" file
from driver import *
from test_login_logout import *
#TC001
def test_search_product(driver):
    test_user_login(driver)  
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.send_keys("Amazfit GTS 3 Smart Watch for Android iPhone")
    search_box.send_keys(Keys.RETURN)  
    time.sleep(2)
    assert "Amazfit GTS 3 Smart Watch for Android iPhone" in driver.page_source  

#TC2
def test_search_product_invalid_keywords(driver):
    test_user_login(driver)  
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.send_keys("@")
    search_box.send_keys(Keys.RETURN)  
    time.sleep(2)
    assert "No result found" in driver.page_source  

#TC3
def test_search_emptyt(driver):
    test_user_login(driver)  
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.send_keys("")
    search_box.send_keys(Keys.RETURN)  
    time.sleep(2)
    assert "index.php" in  driver.current_url 

#TC4
def test_search_uppercase_lower_product(driver):
    test_user_login(driver)  # Log in first
    
    # Test with uppercase
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.clear()  # Clear any pre-filled text in the search box
    search_box.send_keys("MEN'S ULTRA COTTON T-SHIRT, MULTIPACK")
    search_box.send_keys(Keys.RETURN)  # Press Enter to search
    time.sleep(2)  # Wait for results to load
    assert "Men's Ultra Cotton T-Shirt,Multipack"  # Assert the correct result is found
    
    # Test with lowercase
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.clear()  # Clear the search box again
    search_box.send_keys("men's ultra cotton t-shirt, multipack")
    search_box.send_keys(Keys.RETURN)  # Press Enter to search
    time.sleep(2)  # Wait for results to load
    assert "Men's Ultra Cotton T-Shirt,Multipack"  # Assert the correct result is found

#TC5
def test_search_history(driver):
    # Step 1: Navigate to the homepage
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/index.php")
    time.sleep(2)  # Wait for the page to load

    # Step 2: Perform several searches
    search_box = driver.find_element(By.NAME, "search_text")
    
    # Perform the first search
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.clear()
    search_box.send_keys("MEN'S ULTRA COTTON T-SHIRT, MULTIPACK")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for results to load

    # Perform the second search
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.clear()
    search_box.send_keys("WOMEN'S COTTON T-SHIRT, MULTIPACK")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for results to load

    # Perform the third search
    search_box = driver.find_element(By.NAME, "search_text")
    search_box.clear()
    search_box.send_keys("KIDS' T-SHIRT, MULTIPACK")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for results to load

    # Step 3: Select the search bar to check for search history
    search_box = driver.find_element(By.NAME, "search_text")  # Refetch the search box element
    search_box.click()  # Click on the search bar

    # Step 4: Verify previous searches are displayed (access history)
    search_history = driver.find_elements(By.CSS_SELECTOR, ".select2-results__option")  # Locate the search history dropdown

    # Assert that the previous search terms are in the search history
    previous_search_terms = ["MEN'S ULTRA COTTON T-SHIRT, MULTIPACK", "WOMEN'S COTTON T-SHIRT, MULTIPACK", "KIDS' T-SHIRT, MULTIPACK"]
    
    for term in previous_search_terms:
        assert any(term in history.text for history in search_history), f"Search term '{term}' not found in history"

