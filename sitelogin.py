from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("")
#assert "cdse" in driver.title

try:
    submit_element = driver.find_element_by_id("id_submitbutton")
    submit_element.click()
    #submit_element.clear()
    username_element = driver.find_element_by_id("username")
    password_element = driver.find_element_by_id("password")
    username_element.send_keys("")
    password_element.send_keys("")
    login_element = driver.find_element_by_id("loginbtn")
    login_element.click()
    username_element.clear()
    password_element.clear()
except NoSuchElementException as error:
    print('element not found')

#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)    

assert "No results found." not in driver.page_source
driver.close()
