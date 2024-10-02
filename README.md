# Zillow Google Forms Automation

A Python automation project using Selenium and BeautifulSoup to scrape rental listings from Zillow and fill in a Google Form. This helps gather rental data efficiently for further analysis.

## Features

- **Web Scraping**: Uses BeautifulSoup to scrape rental listings from Zillow, including price, address, and link.
- **Google Form Submission**: Automates the process of entering scraped data into a Google Form using Selenium.
- **Efficient Data Management**: Collects rental information and stores it in an organized way for easy tracking.

## Technologies Used

- **Python**: Programming language for scripting.
- **Selenium**: Automates Google Form submissions.
- **BeautifulSoup**: Scrapes rental data from Zillow.

## Getting Started

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed.
- **Selenium and BeautifulSoup**: Install dependencies using:

  ```bash
  pip install selenium beautifulsoup4 requests

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/champy0527/01-010_zillow-google-forms_selenium-bs4.git
    ```

2. Navigate to the project directory:

    ```bash
    cd 01-010_zillow-google-forms_selenium-bs4
    ```

3.	Create a .env file and add your Google Form link and Zillow URL.

4. Run the script:

    ```bash
    python main.py
    ```

## Usage

- Scrape rental listings from Zillow.
- Automatically fill in a Google Form with the scraped data.


## Lessons Learned

- Improved web scraping skills with BeautifulSoup.
- Improved understanding of Python's `after()` function for creating time-based events.
- Managed dynamic data efficiently for real estate analysis.

## Disclaimer

- This project is for educational purposes only. Web scraping may violate the terms of service of some websites.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for any improvements or bug fixes.
