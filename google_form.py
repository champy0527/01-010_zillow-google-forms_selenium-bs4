import os
import time

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleForm:
    URL = "https://forms.gle/GTztGrYXVAYTJ5bH9"

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.implicitly_wait(1)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.URL)
        time.sleep(3)

    def enter_form_input(self, address, rent_price, listing_url):
        try:
            enter_address = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                 "//div[@class='lrKTG']//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")))
            enter_address.send_keys(address, Keys.TAB)
        except Exception as e:
            print(f"Failed to type address: {e}")

        try:
            enter_rent_price = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")))
            enter_rent_price.send_keys(rent_price, Keys.TAB)
        except Exception as e:
            print(f"Failed to type rent price: {e}")

        try:
            enter_listing_url = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
            enter_listing_url.send_keys(listing_url)
        except Exception as e:
            print(f"Failed to type listing URL: {e}")

    def submit_entry(self):
        try:
            submit = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
            submit.click()
        except Exception as e:
            print(f"Failed to submit entry: {e}")

    def next_entry(self):
        try:
            new_entry = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
            new_entry.click()
        except Exception as e:
            print(f"Failed to proceed to new entry: {e}")

    def close_driver(self):
        time.sleep(10)
        self.driver.quit()
