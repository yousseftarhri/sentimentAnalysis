from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from bs4 import BeautifulSoup
import time
import datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import requests

Options = Options()
Options.add_argument('--headless=new')

service = Service("/snap/bin/firefox.geckodriver")
driver = webdriver.Firefox(service=service, options=Options)
#
# Initialize CSV file and write headers (if needed)


with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "review_comment","review_rating"])

    link_products = "https://www.amazon.com/s?k=sustainability+products&i=hpc&rh=n%3A3760901%2Cp_72%3A1248903011&s=relevancerank&dc&page=3&crid=36Y5KUOCJB4E2&qid=1727982665&rnid=1248901011&sprefix=%2Caps%2C257&ref=sr_pg_3"
    driver.get(link_products)
    response = requests.get(link_products)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    racine = soup.findAll("div", class_="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor")
    id_review = 0

    for i in racine:

        div = i.find("div", class_="a-section a-spacing-base")
        link_product = div.find('a', href=True)['href']



        link = f"https://www.amazon.com{link_product}"
        driver.get(link)
        print(f"Fetching data link {link}")

        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        racine_ = soup.find("div", class_="a-section review-views celwidget")
        for a in racine_:
            id_review = id_review + 1

            review_comment = a.find("div",class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content").text
            review_rating = a.find("span", class_="a-icon-alt").text

            writer.writerow([id_review,review_comment,review_rating])
            print(f"Data number {id_review} is saved")
            print([id_review,review_comment,review_rating])