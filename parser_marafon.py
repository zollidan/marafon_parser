from bs4 import BeautifulSoup
import requests
import pandas as pd
from array import *


matrix = []

for p in range(50):

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

        coffi9 = bg.findAll('td', {'data-market-type': 'TOTAL'})[1]

        coffi9_str = coffi9.text
        out_coffi9 = coffi9_str.replace('\n', '')

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
        dict.append(out_coffi8)
        dict.append(out_coffi9)

        matrix.append(dict)

df = pd.DataFrame(matrix)

df.to_excel('marafon_data.xlsx', sheet_name='DATA', index=False)

print(df)

input("Нажмите Enter чтобы продолжить спасибо всем пока...")
