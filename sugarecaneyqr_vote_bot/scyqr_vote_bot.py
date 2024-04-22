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

while True:
    COUNT = 3
    nomination_time = 15 * 60
    interval = nomination_time / COUNT
    random_sleep_time = random.uniform(interval * 0.5, interval * 1.5)
    six_hours = 3*3600
    for _ in range(COUNT):
        nominate()
        time.sleep(random_sleep_time)

    time.sleep(six_hours - nomination_time)