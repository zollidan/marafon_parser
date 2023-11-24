from datetime import date
from datetime import datetime
from time import sleep

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

# -----------------------code starts here-----------------------
# exeptions:
# -1 is cookie banner not found(and it's ok)

driver = webdriver.Chrome()

text = f'All rights reserved. © {date.today().year} LeFort Techs Inc.'
print(f"{text:=^20}")

matrix = []
uniq_id_counter = 0
for p in range(100):

    r = requests.get(
        'https://www.marathonbet.ru/su/betting/Football+-+11?page=' + str(p))

    # print(str(r.status_code) + str(p) + "\n")

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

        # coffi8_more = str(coffi8_splited[1])

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

        # ---------------------selenium part in if statement and two selenium variubles

        coeffTwoFive_less_final_out = None
        coeffTwoFive_more_final_out = None

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
                ()

            game_class = driver.find_elements(By.CLASS_NAME, "sub-row")[k]

            clickMemberLink = game_class.find_element(
                By.CLASS_NAME, "member-link")

            clickMemberLink.click()

            link_array = str(driver.current_url).split("+")
            uniq_game_code = link_array[-1]
            id_to_find = 'shortcutLink_event' + uniq_game_code + 'type3'
            # print(id_to_find)

            sleep(1.5)

            clickTotals = driver.find_element(By.ID, id_to_find)

            clickTotals.click()

            html_from_page = driver.page_source
            soup_after_click = BeautifulSoup(html_from_page, 'html.parser')

            market_wrapper = soup_after_click.findAll(
                'div', {'class': 'market-inline-block-table-wrapper'})

            for name_fields in market_wrapper:
                name_field = name_fields.find(
                    'div', {'class': 'name-field'})
                try:
                    name_field_str = str(name_field.text)
                    name_field_none_space = name_field_str.replace(" ", "")
                    if name_field_none_space == 'Тоталголов':
                        name_field_parent1 = name_field.parent
                        name_field_parent2 = name_field_parent1.parent
                        name_field_parent3 = name_field_parent2.parent
                        name_field_parent4 = name_field_parent3.parent
                        name_field_parent5 = name_field_parent4.parent

                        prices_two_five = name_field_parent5.findAll(
                            'div', {'class': 'coeff-link-2way'})

                        techDicForPrices = []

                        for prices in prices_two_five:
                            if "(2.5)" in prices.text:
                                techDicForPrices.append(prices.text)

                        coeffTwoFive_less = str(techDicForPrices[0])
                        coeffTwoFive_more = str(techDicForPrices[1])

                        coeffTwoFive_less_upd = coeffTwoFive_less.replace(
                            " ", "")
                        coeffTwoFive_more_upd = coeffTwoFive_more.replace(
                            " ", "")

                        coeffTwoFive_less_final_out = coeffTwoFive_less_upd.replace(
                            "(2.5)", "")
                        coeffTwoFive_more_final_out = coeffTwoFive_more_upd.replace(
                            "(2.5)", "")

                        # print(name_field_none_space)
                except Exception:
                    # print("")
                    continue

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
        dict.append(coffi8_coffi2)
        dict.append(coffi8_less)
        dict.append(coffi8_more)
        # dict.append(out_coffi9)
        dict.append("2.5")
        dict.append(coeffTwoFive_less_final_out)
        dict.append(coeffTwoFive_more_final_out)
        # https://www.marathonbet.ru/su/betting/Football/Clubs.+International/UEFA+Champions+League/Group+Stage/Galatasaray+vs+Bayern+Munich+-+16853302?siteStyle=MULTIMARKETS&oddsType=Decimal&timeZone=Europe%2FMoscow&pageAction=default
        matrix.append(dict)

df = pd.DataFrame(matrix)

df.to_excel('marafon_data.xlsx', sheet_name='DATA', index=False)

# print(df)

driver.close()
driver.quit()

input("Нажмите Enter чтобы продолжить спасибо всем пока...")
