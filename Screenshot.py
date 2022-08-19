import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("CHROMEDRIVER_PATH", options=chrome_options)
'''options = Options()
options.headless = True
driver = webdriver.Chrome('driver/chromedriver',chrome_options=options)'''
file = open('urllist.txt', 'r')
file_content = file.readline()
file_content_list = file_content.split(',')
size_of_content = len(file_content_list)
for number in range (size_of_content):
    url = file_content_list[number]
    driver.get(url)
    driver.implicitly_wait(10)
    title = driver.title
    current_datetime = (datetime.now().strftime("%Y%m%d_%I%M%S%p"))
    image_file_name = title + '_' + current_datetime + ".png"
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) 
    driver.find_element_by_tag_name('body').screenshot(("Images" + '/'+image_file_name + '.png'))

print("Please check Images Folder")