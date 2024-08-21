from listings import Listings
from google_form import GoogleForm

# ---------------------------- ZILLOW LISTINGS ----------------------------#

listings = Listings()
addresses = listings.address_list()
rent_prices = listings.rent_price_list()
url_links = listings.url_list()

# ---------------------------- GOOGLE FORM ----------------------------#

google_form = GoogleForm()

for (address, rent_price, url_link) in zip(addresses, rent_prices, url_links):
    print(f"Address: {address}, Rent Price: {rent_price}, URL: {url_link}")  # Check values
    google_form.enter_form_input(address, rent_price, url_link)
    google_form.submit_entry()
    google_form.next_entry()


google_form.close_driver()
