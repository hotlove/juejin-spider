from selenium import webdriver

driver = webdriver.Chrome("d://chromedriver.exe")
driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")

assert "No results found." not in driver.page_source
driver.close()