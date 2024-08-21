from bs4 import BeautifulSoup
import requests


class Listings:
    URL = "https://appbrewery.github.io/Zillow-Clone/"

    def __init__(self):
        self.response = requests.get(self.URL)
        self.response.raise_for_status()
        self.zillow = self.response.content
        self.soup = BeautifulSoup(self.zillow, 'html.parser')

    # TODO Establish addresses
    def address_list(self):
        addresses = self.soup.find_all('address')
        stripped_addresses = [address.text.strip() for address in addresses]
        list_of_addresses = [address.split("|")[-1] if "|" in address else address for address in stripped_addresses]
        # print(list_of_addresses)
        print(len(list_of_addresses))
        return list_of_addresses

    # TODO Establish Rent Prices
    def rent_price_list(self):
        rent_prices = self.soup.find_all('span', {'data-test': 'property-card-price'})
        list_of_rent_prices = [int(price.text.replace("$", "").split("+")[0].replace(",", "").split("/")[0]) for price
                               in
                               rent_prices]
        # print(list_of_rent_prices)
        print(len(list_of_rent_prices))
        return list_of_rent_prices

    # TODO Establish URL of listing
    def url_list(self):
        base_url = "https://www.zillow.com"
        links = self.soup.find_all('a', {'data-test': 'property-card-link'})
        list_of_links = list(set([link.get('href') for link in links]))
        fail_safe_links = [link if link.startswith("http") else f"{base_url}{link}" for link in list_of_links]
        # print(fail_safe_links)
        print(len(fail_safe_links))
        return fail_safe_links
