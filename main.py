import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()

driver.get("https://www.divan.ru/category/svet")

time.sleep(3)

lightings = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
data = []
for lighting in lightings:
    name = lighting.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
    price = lighting.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
    url = lighting.find_element(By.TAG_NAME, 'a').get_attribute('href')
    data.append([name, price, url])

driver.quit()


with open("lightings.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(data)