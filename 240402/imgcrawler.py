#step1.selenium 패키지와 time 모듈 import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib.request import urlretrieve
import time

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

# 크롬드라이버 실행
driver = webdriver.Chrome()
#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.google.com/')
# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)

# 검색어 창을 찾아 search 변수에 저장 (By.CLASS_NAME 방식)
search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')

# 검색어 창을 찾아 search 변수에 저장 (By.XPATH 방식)
search_box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
search_box.send_keys(query) # 검색어
search_box.send_keys(Keys.RETURN)
time.sleep(5)

#step5.이미지 탭 클릭
driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div[2]/a/div').click()
time.sleep(5)

# 스크롤 내리기 (모든 썸네일 이미지 로딩을 위함)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

#이미지 다운로드
img_content = driver.find_elements(By.CLASS_NAME, 'H8Rx8c')

# 이미지 저장할 폴더 생성
import os

# path_folder의 경로는 각자 저장할 폴더의 경로를 적어줄 것
path_folder = r'D:/vision/연구실/crawler/img'
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
        link = imgurl.get_attribute('src')  # 이미지 URL을 가져옴
        time.sleep(5)
        try:
            if link:  # URL이 존재할 경우에만 다운로드 시도
                urlretrieve(link, os.path.join(path_folder, f'{i}.jpg'))  # 이미지 다운로드
                i += 1
                time.sleep(3)
        except:
            print("실패")
            continue

print("종료")
driver.quit()
