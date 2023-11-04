from bs4 import BeautifulSoup as BeautifulSoup
import requests

url = 'https://www.marathonbet.ru/su/betting/Football+-+11'

r = requests.get(url)


soup = BeautifulSoup(r.text, "html.parser")

count_bg = len(soup.findAll('div', class_='bg coupon-row'))

print(count_bg)
