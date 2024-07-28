from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib.request import urlretrieve
import time

query = input('검색할 키워드를 입력하세요: ')

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(3)

search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')

search_box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div[2]/a/div').click()
time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

img_content = driver.find_elements(By.CLASS_NAME, 'H8Rx8c')

import os
path_folder = r'./crawler/img'
if  not os.path.isdir(path_folder):
    os.mkdir(path_folder)

i = 0
for img in img_content:
    if len(os.listdir(path_folder)) > 5:
        break
    webdriver.ActionChains(driver).click(img).perform()
    time.sleep(2)
    imgurls = driver.find_elements(By.CLASS_NAME,'sFlh5c.pT0Scc.iPVvYb')
    time.sleep(3)
    for imgurl in imgurls:
        link = imgurl.get_attribute('src')
        time.sleep(5)
        try:
            if link:
                urlretrieve(link, os.path.join(path_folder, f'{i}.jpg'))
                i += 1
                time.sleep(3)
        except:
            print("실패")
            continue

print("종료")
driver.quit()
