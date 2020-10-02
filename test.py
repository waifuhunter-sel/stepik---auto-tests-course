import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

link = "http://192.168.82.126:5050/infospot/infospotadmin/index.html#/editor"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.pdf')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)
    browser.find_element_by_id("username").send_keys("3")
    browser.find_element_by_id("password").send_keys("3")

    submitButton = browser.find_element_by_name("task")
    submitButton.click()

    pdfButton = browser.find_element_by_xpath("/html/body/app-root/app-main/div/app-editor/div[1]/tree/tree-internal/ul/li/tree-internal[13]/ul/li/tree-internal/ul/li/div/div[2]")
    pdfButton.click()

    browser.execute_script("window.scrollBy(0, -100);")
    browser.find_element_by_id("fileInput").send_keys(file_path)

    savePDFButton = browser.find_element_by_xpath("/html/body/app-root/app-main/div/app-editor/div[2]/app-pdf-viewer/div/div/div/form/div/div/div[2]/button[1]")
    browser.execute_script("window.scrollBy(0, -100);")
    savePDFButton.click()

    a = browser.find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-item-modal/div[2]/svg/circle")
    print (a)
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
