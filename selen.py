import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.marathonbet.ru/su/betting/Football+-+11'


try:
    driver.get(url=url)

    nthAmount = len(driver.find_elements(By.CLASS_NAME, "coupon-row-item"))

    print(nthAmount)

    for i in range(0, 90):
        team1 = driver.find_elements(By.CLASS_NAME, "member-link")[i]
        team2 = driver.find_elements(By.CLASS_NAME, "member-link")[i + 1]
        print(team1, " ", team2)

    driver.find_element(By.CLASS_NAME, "member-area-button").click()

    time.sleep(5)
except Exception as ex:
    print(ex)
finally:

    driver.close()
    driver.quit()