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

service = Service("/snap/bin/firefox.geckodriver")
driver = webdriver.Firefox(service=service, options=Options)
#
# Initialize CSV file and write headers (if needed)
with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "review_comment","review_rating"])

    link_products = "https://www.amazon.com/s?k=sustainability+products&crid=1DOPVMDCV2ZGV&sprefix=sustainability%2Caps%2C256&ref=nb_sb_ss_ts-doa-p_1_14"
    driver.get(link_products)
    response = requests.get(link_products)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    racine = soup.findAll("div", class_="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor")
    id_review = 0

    for i in racine:
        id_review = id_review + 1

        div = i.find("div", class_="a-section a-spacing-base")
        link_product = div.find('a', href=True)['href']



        link = f"https://www.amazon.com{link_product}"
        driver.get(link)
        print(f"Fetching data link {link}")

        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        link_review = soup.find("div", {"id": "reviews-medley-footer"}).find('a', href=True)['href']

        link_review = f"https://www.amazon.com{link_review}"

        driver.get(link_review)
        print(f"link review is {link_review}")

        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        racine_ = soup.findAll("div", class_="a-section review aok-relative")
        for a in racine_:
            review_comment = a.find("span", class_="a-size-base review-text review-text-content").text
            review_rating = a.find("div", class_="a-row").find("span", class_="a-icon-alt").text

            writer.writerow([id_review,review_comment,review_rating])
            print(f"Data number {id_review} is saved")
            print([id_review,review_comment,review_rating])


"""link_products = "https://www.amazon.com/s?k=sustainability+products&crid=1DOPVMDCV2ZGV&sprefix=sustainability%2Caps%2C256&ref=nb_sb_ss_ts-doa-p_1_14"
driver.get(link_products)

time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# This to scrape all link pages.

racine = soup.findAll("div", class_="sg-col-4-of-2        # print(review)
        #rate = int(float(i.find("span", class_="a-icon-alt").text.split(' ')[0]))4 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor")
for i in racine:
    div = i.find("div", class_="a-section a-spacing-base")
    link_product = div.find('a', href=True)['href']
    # print(review)
    # rate = int(float(i.find("span", class_="a-icon-alt").text.split(' ')[0]))
    print(link_product)"""

""""
    link_products = "https://www.amazon.com/s?k=sustainability+products&crid=1DOPVMDCV2ZGV&sprefix=sustainability%2Caps%2C256&ref=nb_sb_ss_ts-doa-p_1_14"
    driver.get(link_products)

    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # This to scrape all link pages.

    racine = soup.findAll("div",
                          class_="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor")
    for i in racine:
        div = i.find("div", class_="a-section a-spacing-base")
        link_product = div.find('a', href=True)['href']
        # print(review)
        # rate = int(float(i.find("span", class_="a-icon-alt").text.split(' ')[0]))
        print(link_product)
"""

"""link_review = f"https://www.amazon.com/DR-BRIGHT-Eco-Friendly-Biodegradable-Toothbrushes-Compostable/product-reviews/B0CGRJM6LP/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

print(f"link review is {link_review}")

driver.get(link_review)
response = requests.get(link_review)
time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')

racine_ = soup.findAll("div", class_="a-section review aok-relative")
for a in racine_:
    review_comment = a.find("span", class_="a-size-base review-text review-text-content").text
    review_rating = a.find("div", class_="a-row").find("span", class_="a-icon-alt").text

    print(f"Data number is saved")
    print([review_comment, review_rating])
"""
