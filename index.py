import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd

urlWith24H = 'https://www.marathonbet.ru/su/betting/Football+-+11?cpcids=all&interval=H24'
urlWithAll = 'https://www.marathonbet.ru/su/betting/Football+-+11?cpcids=all'
req = requests.get(url=urlWithAll)
soup = BeautifulSoup(req.text, "html.parser")
categories = soup.find_all(class_='category-label-link', href=True)
matrix = []
for league in categories:
    bgDict = []
    leagueName = league.text
    leagueCategoryHref = 'https://www.marathonbet.ru' + league['href']
    req2 = requests.get(url=leagueCategoryHref)
    soup2 = BeautifulSoup(req2.text, "html.parser")
    bgs = soup2.find_all(class_='bg coupon-row')
    for bg in bgs:
        team1Raw = bg.find_all(class_='member-link')[0]
        team2Raw = bg.find_all(class_='member-link')[1]

        team1 = team1Raw.text.strip()
        team2 = team2Raw.text.strip()

        coffi0 = bg.findAll('td', {'data-market-type': 'RESULT'})[0]
        coffi0 = coffi0.text.strip()

        coffi1 = bg.findAll('td', {'data-market-type': 'RESULT'})[1]
        coffi1 = coffi1.text.strip()

        coffi2 = bg.findAll('td', {'data-market-type': 'RESULT'})[2]
        coffi2 = coffi2.text.strip()

        coffi3 = bg.findAll('td', {'data-market-type': 'DOUBLE_CHANCE'})[0]
        coffi3 = coffi3.text.strip()

        coffi4 = bg.findAll('td', {'data-market-type': 'RESULT'})[1]
        coffi4 = coffi4.text.strip()

        coffi5 = bg.findAll('td', {'data-market-type': 'RESULT'})[2]
        coffi5= coffi5.text.strip()

        coffi6 = bg.findAll('td', {'data-market-type': 'HANDICAP'})[0]
        coffi6 = coffi6.text.strip()

        coffi7 = bg.findAll('td', {'data-market-type': 'HANDICAP'})[1]
        coffi7 = coffi7.text.strip()

        coffi8 = bg.findAll('td', {'data-market-type': 'TOTAL'})[0]
        coffi8 = coffi8.text.strip()

        coffi9 = bg.findAll('td', {'data-market-type': 'TOTAL'})[1]
        coffi9 = coffi9.text.strip()

        print(leagueName)
        print(team1, team2)
        
        
        dateTime = bg.find('td', {'class': 'date date-short'})
        
        if dateTime is None:
            dateTime = bg.find('td', {'class': 'date date-with-month'})
        
        dateTime = dateTime.text
        dateTime = dateTime.strip()
        dateTime = dateTime.split()

        dt = datetime.datetime.now()
        dtDay = dt.day
        year = dt.year
        dtMonth = dt.month

        try:
            day = dateTime[0]
            month = dateTime[1]
            time = dateTime[2]
        except IndexError:
            time = dateTime[0]
            day = dtDay
            month = dtMonth
            


        print(f"время игры {time}")

        #print(day, month, year, time, coffi0, coffi1, coffi2, coffi3, coffi4, coffi5, coffi6, coffi7, coffi8, coffi9)


        

