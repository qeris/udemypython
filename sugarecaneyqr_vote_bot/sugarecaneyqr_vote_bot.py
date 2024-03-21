from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
url = "https://regina.communityvotes.com/2024/02/wellness-hair-and-beauty/hair-removal-and-waxing"
driver = webdriver.Firefox()
driver.get(url)
COUNT = 5

def nominate():
    nominate_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[5]/table/tbody/tr[34]/td[1]/a")
    nominate_button.click()
    time.sleep(COUNT)
    driver.quit()

for _ in range(COUNT):
    nominate()
    interval = random.randint(1*3600, 6*3600)
    time.sleep(interval)
    