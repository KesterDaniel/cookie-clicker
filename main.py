import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\development\chromedriver.exe"
chr_options = webdriver.ChromeOptions()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chr_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)

english_lang_select = driver.find_element(By.XPATH, "//*[@id='langSelect-EN']")
# cookie_number = driver.find_element(By.ID, "cookieNumbers")

english_lang_select.click()

cookie = driver.find_element(By.ID, "bigCookie")

click_timeout = 5  # [seconds]
game_timeout = 300

timeout_start = time.time()

while True:
    cookie.click()
    if time.time() > click_timeout:
        clickable = driver.find_elements(By.CSS_SELECTOR, ".enabled")
        prices = driver.find_elements(By.CSS_SELECTOR, ".enabled .content .price")
        price_list = [int(price.text.replace(",", "")) for price in prices]
        money_count = driver.find_element(By.ID, "cookies").text.strip().split()[0]
        if "," in money_count:
            money_count.replace(",", "")
        cookie_count = int(money_count)
        for price in prices:
            if cookie_count > int(price.text) == max(price_list):
                clickable[prices.index(price)].click()
                click_timeout += 5
    elif time.time > game_timeout:
        print("done")
        break

