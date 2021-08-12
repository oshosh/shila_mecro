
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time
import pyautogui
import keyboard
import tkinter.messagebox
import random

window = Tk()
window.title('신라호텔 예약')
window.geometry('650x200')

# id, password, link주소 전역 변수
user_id, password, sangpum_link = StringVar(), StringVar(), StringVar()

def check_data():
    if user_id.get() and password.get() and sangpum_link.get():
        tkinter.messagebox.showinfo("성공", "확인 후 메크로를 실행 합니다.")
        start()
    else:
        tkinter.messagebox.showwarning("경고", "전부 입력해야 실행 됩니다.")

def start():
    #URL 세팅 (로그인, 상품)
    url_login = 'https://www.shillahotels.com/fbresv/web/memDiningStepWait.do?lang=ko&hotlId=S&ContIdRest=PAL&_gl=1*1iemql4*_ga*NTI5MDY1NjkxLjE2MjYzNDc2MDI.*_ga_30Y6N61ES4*MTYyNjQwNzQ3NS4yLjEuMTYyNjQwNzQ5Ny4zOA..&_ga=2.84028176.886317983.1626347602-529065691.1626347602'

    driver = Options() 
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'cookies': 1, 'images': 1, 'javascript': 1, 
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2}}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")

    # #크롬 드라이버 경로
                                                                    # D:/temp/chromedriver.exe
    parse_string = text_3080_link.get().replace('\\', '/')
  
    driver = webdriver.Chrome(chrome_options=options, executable_path="{0}".format(parse_string))

    print(parse_string)
    driver.get('https://www.naver.com')

    while True :
        if keyboard.is_pressed('f3') :
            driver.get(url_login)
            
            element2 = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contents > div.new_rsvBox.diningNew > div.rsvWrap.diningHotelBox_N > div.rsvSchHotel > div.rsvSchCont.clearfix > dl > dd > div.diningBtnSearch.fr")))
            element2.click()

            type_element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contents > div > div.rsvOptionWrap > div.diningTableSel.ly_reserve.rsvPeople > div > div > dl > dd > ul > li.last > a")))
            type_element.click()


            # room_element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#roomDiv > div > div > dl:nth-child(1) > dd > ul > li.last > a")))
            room_element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#roomDiv > div > div > dl:nth-child(1) > dd > ul > li.first > a")))
            room_element.click()

            driver.find_element_by_id('roomPersonTmp').send_keys('{0}'.format(user_id.get()))

            diningBtnSearch = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#roomDiv > div > div > div")))
            diningBtnSearch.click()

            nextBtn_element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dateSearchDiv")))
            print(nextBtn_element.get_attribute('style'))

            btn_style = ''
            check = ''
            while True :
                try:
                    nextBtn_element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dateSearchDiv")))
                    
                    btn_style = nextBtn_element.get_attribute('style')
                    print(btn_style)
                    time.sleep(0.5)

                    if btn_style != 'display: none;':
                        # driver.execute_script("document.querySelector('#nextBtn').click()")
                        check = 'T'
                        break
                except Exception:                    
                   print(check)

            if check == 'T' :
                print('잇음')
                
                current_date_text = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#currentCalendar > div > div")))
                current_date = current_date_text.get_attribute('innerText').split('.')[1]
                print('현재 날짜'+ current_date)
                
                i = 0
                idx_date = int(text_3070_link.get()) - int(current_date)
                print(idx_date)

                # driver.execute_script("document.querySelector('#nextBtn').click()")
                # driver.execute_script("document.querySelector('#nextBtn').click()")
                # driver.execute_script("document.querySelector('#nextBtn').click()")
                while i < idx_date :
                    i += 1
                    # 포문 필요 현재 달에 따라 ..
                    driver.execute_script("document.querySelector('#nextBtn').click()") # 9월
                    
                    if idx_date == i :
                        break

                next_date_text = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#currentCalendar > div > div")))
                next_date = next_date_text.get_attribute('innerText').split('.')[1]
                
                if current_date == next_date :
                    while True:
                        try:
                            next_date_text2 = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#currentCalendar > div > div")))
                            next_date2 = next_date_text2.get_attribute('innerText').split('.')[1]
                            
                            time.sleep(0.5)
                            # if next_date2 == current_date:
                            if next_date2 != current_date:
                                check2 ='T'
                                break
                        except Exception: 
                            print('asdgs')
                        
                else :
                    check2 = 'T'
                    date = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#currentCalendar > div > table > tbody > tr.first > td:nth-child(6)")))
                    date.click()

                
                if check2 == 'T':
                    # 날짜 클릭
                    
                    date_list = []
                    table = driver.find_element_by_class_name('thisCal')
                    tbody = table.find_element_by_tag_name("tbody")
                    rows = tbody.find_elements_by_tag_name("tr")
                    for index, value in enumerate(rows):
                        for num in range(0, 7):
                            body = value.find_elements_by_tag_name("td")[num]
                            date_list.append(body.text)

                    print(date_list)

                    row = 1
                    found_date = date_list.index(password.get()) + 1
                    
                    if found_date <= 7:
                        row = 1
                    elif found_date <= 14 :
                        row = 2
                    elif found_date <= 21 :
                        row = 3
                    elif found_date <= 28 :
                        row = 4
                    else :
                        row = 5
                    
                    
                    print("col_before : " + str(found_date))
                    
                    if row == 1:
                        found_date = int(found_date)
                    elif row == 2:
                        found_date = int(found_date - 7)
                    elif row == 3:
                        found_date = int(found_date - 14)
                    elif row == 4:
                        found_date = int(found_date - 21)    
                    elif row == 5:
                        found_date = int(found_date - 28)
                        
                    
                    print('-------------------------------')
                    print("row : " + str(row))
                    print("col_after : " + str(found_date))
                    
                    print('-------------------------------')

                    str_Xpath = '//*[@id="currentCalendar"]/div/table/tbody/tr[{0}]/td[{1}]'.format(str(row), str(found_date))

                    date = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, str_Xpath)))

                    date.click()

                    #break
                    opacity = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.opacity")))
                    opacity_state = opacity.get_attribute('style')

                    print('opacity_state 한번 체크 해봄')
                    print(opacity_state)

                    check3 = ''
                    if opacity_state == 'display: block;':
                        while True :
                            try :
                                opacity = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.opacity")))
                                opacity_state = opacity.get_attribute('style')

                                if opacity_state == 'display: none;':
                                    check3 = 'T'
                                    break
                            except Exception: 
                                print('asdgs')
                            
                    else :
                        check3 == 'T'

                    
                    if check3 == 'T':

                        option = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#visitTimeSel")))
                        option.click()

                        print('시간 선택')

                        select = Select(driver.find_element_by_id('visitTimeSel'))
                        select.select_by_index('2')
                        
                        print('유의 사항 체크')
                                                                                                                                                                                            
                        label_for_checkbox = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="policyCkDiv"]/label')))
                        label_for_checkbox.click()

                        last_btn = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nextBtnDiv"]/div[2]/a[1]')))
                        last_btn.click()
        
            else :
                print('없음')

ttk.Label(window, text = "인원수 13 고정 : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "날짜(1 ~ 31일 ex> 6) : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "월 (현재달 + 3 만 적용) : ").grid(row = 1, column = 3, padx = 10, pady = 10)
ttk.Label(window, text = "예약 주소 : ").grid(row = 0, column = 3, padx = 10, pady = 10)

user_id.set("13")
password.set("21")
sangpum_link.set('https://www.shillahotels.com/fbresv/web/memDiningStepWait.do?lang=ko&hotlId=S&ContIdRest=PAL&_gl=1*1iemql4*_ga*NTI5MDY1NjkxLjE2MjYzNDc2MDI.*_ga_30Y6N61ES4*MTYyNjQwNzQ3NS4yLjEuMTYyNjQwNzQ5Ny4zOA..&_ga=2.84028176.886317983.1626347602-529065691.1626347602')

ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = password).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = sangpum_link).grid(row = 0, column = 4, padx = 10, pady = 10)

text_3070_link, text_3080_link, test = StringVar(), StringVar(), StringVar()

text_3070_link.set("8")
text_3080_link.set("chromedriver.exe 경로 첨부")
test.set("http://m.11st.co.kr/MW/Product/productBasicInfo.tmall?prdNo=2812767439")

textBox = ttk.Entry(window, textvariable = text_3070_link).grid(row = 1, column = 4, columnspan=4, padx = 10, pady = 10)
textBox = ttk.Entry(window, textvariable = text_3080_link, width=60).grid(row = 5, column = 1, columnspan=4, padx = 10, pady = 10)

ttk.Button(window, text = "매크로 실행", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()

