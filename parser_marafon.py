from asyncio import wait
import datetime
import operator
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
from array import *
from datetime import date
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


def print_frame():
    text = f'All rights reserved. © {date.today().year} LeFort Techs Inc.'
    print(
        f'|=============================================== {text} ===============================================|')


print_frame()

matrix = []
uniq_id_counter = 0
for p in range(1):

    r = requests.get(
        'https://www.marathonbet.ru/su/betting/Football+-+11?page=' + str(p))

    print(str(r.status_code) + str(p) + "\n")

    soup = BeautifulSoup(r.text, "html.parser")

    count_bg = len(soup.findAll('div', class_='bg coupon-row'))

    for k in range(count_bg):
        dict = []

        bg = soup.findAll('div', class_='bg coupon-row')[k]
        team_name = bg.findAll('a', class_='member-link')[0]

        team_name_str = team_name.text
        out_team_name = team_name_str.replace('\n', '')

        team_name1 = bg.findAll('a', class_='member-link')[1]

        team_name1_str = team_name1.text
        out_team_name1 = team_name1_str.replace('\n', '')

        coffi0 = bg.findAll('td', {'data-market-type': 'RESULT'})[0]

        coffi0_str = coffi0.text
        out_coffi0 = coffi0_str.replace('\n', '')

        coffi1 = bg.findAll('td', {'data-market-type': 'RESULT'})[1]

        coffi1_str = coffi1.text
        out_coffi1 = coffi1_str.replace('\n', '')

        coffi2 = bg.findAll('td', {'data-market-type': 'RESULT'})[2]

        coffi2_str = coffi2.text
        out_coffi2 = coffi2_str.replace('\n', '')

        coffi3 = bg.findAll('td', {'data-market-type': 'DOUBLE_CHANCE'})[0]

        coffi3_str = coffi3.text
        out_coffi3 = coffi3_str.replace('\n', '')

        coffi4 = bg.findAll('td', {'data-market-type': 'DOUBLE_CHANCE'})[1]

        coffi4_str = coffi4.text
        out_coffi4 = coffi4_str.replace('\n', '')

        coffi5 = bg.findAll('td', {'data-market-type': 'DOUBLE_CHANCE'})[2]

        coffi5_str = coffi5.text
        out_coffi5 = coffi5_str.replace('\n', '')

        coffi6 = bg.findAll('td', {'data-market-type': 'HANDICAP'})[0]

        coffi6_str = coffi6.text
        out_coffi6 = coffi6_str.replace('\n', '')

        coffi7 = bg.findAll('td', {'data-market-type': 'HANDICAP'})[1]

        coffi7_str = coffi7.text
        out_coffi7 = coffi7_str.replace('\n', '')

        coffi8 = bg.findAll('td', {'data-market-type': 'TOTAL'})[0]

        coffi8_str = coffi8.text
        out_coffi8 = coffi8_str.replace('\n', '')
        coffi8_splited = out_coffi8.split()

        coffi8_coffi = str(coffi8_splited[0])

        coffi8_coffi2 = coffi8_coffi.replace('(', '').replace(')', '')

        coffi8_more = str(coffi8_splited[1])

        coffi9 = bg.findAll('td', {'data-market-type': 'TOTAL'})[1]

        coffi9_str = coffi9.text
        out_coffi9 = coffi9_str.replace('\n', '')

        coffi9_splited = out_coffi9.split()

        coffi8_less = str(coffi8_splited[1])

        coffi8_more = str(coffi9_splited[1])

        date_time = bg.find('td', {'class': 'date'})
        date_time_str = date_time.text
        out_date_time = date_time_str.replace('\n', '')
        out_date_time_splited = out_date_time.split()

        dict.append(out_date_time_splited[0])

        if len(out_date_time_splited) == 3:

            if out_date_time_splited[1] == 'янв':
                new_month = str(out_date_time_splited[1]).replace('янв', '01')
                dict.append(new_month)
            if out_date_time_splited[1] == 'фев':
                new_month = str(out_date_time_splited[1]).replace('фев', '02')
                dict.append(new_month)
            if out_date_time_splited[1] == 'мар':
                new_month = str(out_date_time_splited[1]).replace('мар', '03')
                dict.append(new_month)
            if out_date_time_splited[1] == 'апр':
                new_month = str(out_date_time_splited[1]).replace('апр', '04')
                dict.append(new_month)
            if out_date_time_splited[1] == 'май':
                new_month = str(out_date_time_splited[1]).replace('май', '05')
                dict.append(new_month)
            if out_date_time_splited[1] == 'июн':
                new_month = str(out_date_time_splited[1]).replace('июн', '06')
                dict.append(new_month)
            if out_date_time_splited[1] == 'июл':
                new_month = str(out_date_time_splited[1]).replace('июл', '07')
                dict.append(new_month)
            if out_date_time_splited[1] == 'авг':
                new_month = str(out_date_time_splited[1]).replace('авг', '08')
                dict.append(new_month)
            if out_date_time_splited[1] == 'сен':
                new_month = str(out_date_time_splited[1]).replace('сен', '09')
                dict.append(new_month)
            if out_date_time_splited[1] == 'окт':
                new_month = str(out_date_time_splited[1]).replace('окт', '10')
                dict.append(new_month)
            if out_date_time_splited[1] == 'ноя':
                new_month = str(out_date_time_splited[1]).replace('ноя', '11')
                dict.append(new_month)
            if out_date_time_splited[1] == 'дек':
                new_month = str(out_date_time_splited[1]).replace('дек', '12')
                dict.append(new_month)

        else:
            continue

        year = str(datetime.now().year)

        year_new = year.replace(',', '')

        if coffi8_coffi2 != "2.5":
            driver.get(
                'https://www.marathonbet.ru/su/betting/Football+-+11?page=' + str(p))

            try:
                # Здесь может возникнуть исключение
                cookie_widget = driver.find_element(
                    By.CLASS_NAME, "cookie-notice")

                cookie_notice_disable = cookie_widget.find_element(
                    By.CLASS_NAME, "v-btn__content").click()

            except Exception as e:
                print(" none ")
            else:
                print("Программа успешно отработала")
            finally:
                print("пупа пупа")

            game_class = driver.find_elements(By.CLASS_NAME, "sub-row")[k]

            clickMemberLink = game_class.find_element(
                By.CLASS_NAME, "member-link")

            clickMemberLink.click()

            link_array = str(driver.current_url).split("+")
            uniq_game_code = link_array[-1]
            id_to_find = 'shortcutLink_event' + uniq_game_code + 'type3'
            print(id_to_find)

            clickTotals = driver.find_element(By.ID, id_to_find)

            clickTotals.click()

            # Проблема в том, что ваш inputтег находится внутри iframe, вам нужно сначала переключиться на него:

            # frame = driver.find_element_by_xpath('//frame[@name="main"]')
            # driver.switch_to.frame(frame)
            # pass1 = driver.find_element_by_id("PASSFIELD1")

            # time.sleep(5)

        dict.append(year)
        dict.append(out_date_time_splited[2])
        dict.append(out_team_name)
        dict.append(out_team_name1)
        dict.append(out_coffi0)
        dict.append(out_coffi1)
        dict.append(out_coffi2)
        dict.append(out_coffi3)
        dict.append(out_coffi4)
        dict.append(out_coffi5)
        dict.append(out_coffi6)
        dict.append(out_coffi7)

        # dict.append(out_coffi9)
        dict.append("2.5")
        # dict.append(coffi_in_details_less)
        # dict.append(coffi_in_details_more)
        # https://www.marathonbet.ru/su/betting/Football/Clubs.+International/UEFA+Champions+League/Group+Stage/Galatasaray+vs+Bayern+Munich+-+16853302?siteStyle=MULTIMARKETS&oddsType=Decimal&timeZone=Europe%2FMoscow&pageAction=default
        matrix.append(dict)

df = pd.DataFrame(matrix)

df.to_excel('marafon_data.xlsx', sheet_name='DATA', index=False)

print(df)

driver.close()
driver.quit()

input("Нажмите Enter чтобы продолжить спасибо всем пока...")
