from openpyxl import workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import openpyxl
import excel
import time

driver = webdriver.Chrome('.\chromedriver.exe')
driver.maximize_window()

# Mở web
driver.get("http://127.0.0.1:8000/")

#Log in
driver.find_element_by_xpath('/html/body/div[1]/div[3]/p/a[1]').click()
#Điền tên đăng nhập, mật khẩu       
driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("thanhmai")
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("m")
driver.find_element_by_xpath('/html/body/div[3]/div/form/button').click() 
#Ấn vào tên để ra trang đổi thông tin
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/a').click()
#Hàm xóa infor có sẵn
def clear_text(element):
    length = len(element.get_attribute('value'))
    element.send_keys(length * Keys.BACKSPACE)
path='.\changeInfor.xlsx'
rows=excel.getRowCount(path,'Sheet1')
for r in range(2, rows+1):
    firstName_excel=excel.readData(path,'Sheet1', r, 1)
    lastName_excel=excel.readData(path,'Sheet1', r, 2)
#xóa infor, thêm infor mới
    firstName=driver.find_element_by_xpath('//*[@id="id_first_name"]')
    clear_text(firstName)
    if firstName_excel != None:
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys(firstName_excel)

    lastName=driver.find_element_by_xpath('//*[@id="id_last_name"]')
    clear_text(lastName)
    if lastName_excel != None:
        driver.find_element_by_xpath('//*[@id="id_last_name"]').send_keys(lastName_excel)
#Ấn click
    driver.find_element_by_xpath('/html/body/div[3]/div/div/form/input[2]').click()
    time.sleep(5)
    if driver.find_element_by_xpath('/html/body/div[3]/div/div/div'):
        excel.writeData(path,"Sheet1", r, 3, "test passed")
    else:
        excel.writeData(path,"Sheet1", r, 3, "test failed")



