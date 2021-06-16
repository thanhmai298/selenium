from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import excel
import time

driver = webdriver.Chrome('.\chromedriver.exe')
driver.get("http://127.0.0.1:8000/admin")
driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("thanhmai")
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("m")
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

path='.\changeInfor.xlsx'
rows=excel.getRowCount(path,'Sheet2')
for r in range(2, rows+1):
    driver.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr/th/a').click()
    driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()

    brandname_excel=excel.readData(path,'Sheet2', r, 1)
    img_excel=excel.readData(path,'Sheet2', r, 2)
    category_excel=excel.readData(path,'Sheet2', r, 3)
    descrip_excel=excel.readData(path,'Sheet2', r, 4)

    if brandname_excel != None:
        driver.find_element_by_xpath('//*[@id="id_branding_name"]').send_keys(brandname_excel)
    if img_excel != None:
        image_path=os.path.abspath(img_excel)
        driver.find_element_by_xpath('//*[@id="id_brandImage"]').send_keys(image_path)
    if category_excel != None:
        driver.find_element_by_id(category_excel).is_selected()
    if descrip_excel != None:
        driver.find_element_by_xpath('//*[@id="id_brandDescript"]').send_keys(descrip_excel)
    driver.find_element_by_xpath('//*[@id="brand_form"]/div/div/input[1]').click()
    time.sleep(5)
    if driver.title=="Select brand to change | Django site admin":
        excel.writeData(path,"Sheet2",r,5,"Thành công")
    else:
        excel.writeData(path,"Sheet2",r,5,"Thất bại")
    driver.find_element_by_xpath('//*[@id="site-name"]/a').click()
        

assert "No results found" not in driver.page_source


