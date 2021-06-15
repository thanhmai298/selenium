from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('.\chromedriver.exe')
driver.get("http://127.0.0.1:8000/admin")
driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("thanhmai")
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("m")
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

assert "No results found" not in driver.page_source
