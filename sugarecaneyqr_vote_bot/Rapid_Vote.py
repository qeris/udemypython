from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

url = "https://regina.communityvotes.com/2024/02/wellness-hair-and-beauty/hair-removal-and-waxing"

def nominate():
    driver = webdriver.Firefox()
    driver.get(url)
    nominate_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[5]/table/tbody/tr[35]/td[1]/a")
    nominate_button.click()
    driver.quit()
    time.sleep(random.randint(1,10)*60)

while True:
    COUNT = 20
    for _ in range(COUNT):
        nominate()