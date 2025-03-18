# SIMPLE SCRAPER - NOT SCRAPY
import requests
import json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

url = "https://www.amazon.com/CeraVe-Hydrating-Facial-Cleanser-Fragrance/dp/B07RL88DD2/ref=mp_s_a_1_2_sspa?crid=2QFR8L06D6AA6&dib=eyJ2IjoiMSJ9.8phhNZdmKGY_GR0i02CkzJjCxPPeh2ZoiAFsyQqVv9i-g2SvC3j0rncepO9IBHXIHfo8N9zjGaOdDvmVizULm0LxiFKDKPU6uH0c6PioC4V7ZqaPS6NqQULq9ScGP2bKsdkQWHqHjHVcZXGHo6wFqeIx3nPSrJI68pzlWgqfWaoQgI3mN7kYlwqlm86QVI-m5VfYaidtr7DUJJZkL6heuw.hwALKd_Ra2dUIsYxuVcFdkRQCaTRL8-j3nXDHIlfkOA&dib_tag=se&keywords=skincare&qid=1742301585&sprefix=skincare%2Caps%2C202&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9zZWFyY2hfYXRm&psc=1"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

reviews = soup.find_all("span", {"data-hook":"review-body"})
for review in reviews:
    with open("Review_data.json", "w") as file:
        json.dump(review, indent=4)
    print(review.get_text(strip=True))