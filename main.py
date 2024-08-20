import requests
import os

from dotenv import load_dotenv

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------------------ CONSTANTS ------------------------------#

load_dotenv()

GOOGLE_FORMS_URL = "https://forms.gle/GdVtyzxEiRSvRH3j8"
GOOGLE_USERNAME = os.getenv("GOOGLE_USERNAME")
GOOGLE_PASSWORD = os.getenv("GOOGLE_PASSWORD")

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

# -------------------------- ZILLOW WEB SCRAPE -------------------------#

response = requests.get(ZILLOW_URL)
response.raise_for_status()
zillow = response.content

soup = BeautifulSoup(zillow, 'html.parser')
# print(soup.prettify())

# TODO Establish addresses
addresses = soup.find_all('address')
stripped_addresses = [address.text.strip() for address in addresses]

list_of_addresses = [address.split("|")[-1] if "|" in address else address for address in stripped_addresses]
# print(list_of_addresses)
print(len(list_of_addresses))

# TODO Establish Rent Prices
rent_prices = soup.find_all('span', {'data-test': 'property-card-price'})
list_of_rent_prices = [price.text.replace("$","").split("+")[0].replace(",","").split("/")[0] for price in rent_prices]
# print(list_of_rent_prices)
print(len(list_of_rent_prices))