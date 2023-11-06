from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

main_url = 'https://www.marathonbet.ru/su/betting/Football+-+11'

driver.get(main_url)

element_scroll = driver.find_element(
    By.XPATH, "(//span[@data-member-link='true'][last()])")
element_scroll.location_once_scrolled_into_view

bg_coupon_list = len(driver.find_elements(By.CLASS_NAME, "bg"))


print(bg_coupon_list)

driver.close()
driver.quit()
