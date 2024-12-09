# Call all modules and functions in the "driver.py" file
from driver import *

#Navigation Function
#TC1
def test_navigation_home(driver):
    driver.get('http://localhost/Phpcode/eCommerceSite-PHP/index.php')
    time.sleep(5)
    driver.find_element(By.LINK_TEXT,"Home").click()

#TC2
def test_navigation_home_About_Us(driver):
    driver.get('http://localhost/Phpcode/eCommerceSite-PHP/about.php')
    time.sleep(5)
    driver.find_element(By.LINK_TEXT,"Home").click()

#TC3
def test_navigate_back_to_previous_page(driver):
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/index.php")
    time.sleep(2)

    contact_us_link = driver.find_element(By.LINK_TEXT, "Contact Us")
    contact_us_link.click()
    time.sleep(2)

    assert "contact.php" in driver.current_url

    driver.back()
    time.sleep(2)

    assert "index.php" in driver.current_url

#TC4
def test_reload_current_page(driver):
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/index.php")
    time.sleep(2)

    driver.refresh()  # Reload the page
    time.sleep(2)

    assert "index.php" in driver.current_url

#TC5
def test_navigation_via_site_logo(driver):
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/faq.php")
    time.sleep(2)

    site_logo = driver.find_element(By.CLASS_NAME, "col-md-4")  # Adjust selector to target the logo
    site_logo.click()
    time.sleep(2)

    assert "index.php" in driver.current_url

#TC6
def test_navigate_to_search_results_page(driver):
    driver.get("http://localhost/Phpcode/eCommerceSite-PHP/index.php")
    time.sleep(2)

    search_bar = driver.find_element(By.NAME, "search_text")  
    search_bar.send_keys("laptop")  
    time.sleep(1)

    search_button = driver.find_element(By.CLASS_NAME, "btn-danger")  
    search_button.click()
    time.sleep(2)

    assert "search-result.php" in driver.current_url  
