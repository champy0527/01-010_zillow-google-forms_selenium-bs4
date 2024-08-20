import requests
import os

from listings import Listings
from dotenv import load_dotenv


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


# ---------------------------- ZILLOW LISTINGS ----------------------------#

listings = Listings()
addresses = listings.address_list()
rent_prices = listings.rent_price_list()
url_links = listings.url_list()



