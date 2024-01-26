import smtplib

import requests
import lxml
from bs4 import BeautifulSoup
# Enter the item link here
url = "https://www.amazon.in/ASUS-Vivobook-i3-1220P-Integrated-X1502ZA-EJ381WS/dp/B0BLP23H71/ref=sr_1_2?crid=21RVKM2YWEJAH&keywords=asus%2Bvivobook%2B15&qid=1704545550&sprefix=asus%2Caps%2C264&sr=8-2&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
title = soup.select("span#productTitle")[0].getText().strip()
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
pricefinal = ''
for num in price_without_currency.split('.')[0]:
    if num not in [',', '.']:
        pricefinal += num
pricefinal = int(pricefinal)
print(pricefinal)

BUY_PRICE = 40000
# Write your buyprice for an item when the price is less than the buyprice you will get an email
if pricefinal < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("yashwanthnaddana2002@gmail.com", "nydv qexs jsxy cxai")
        connection.sendmail(
            from_addr="yashwanthnaddana2002@gmail.com",
            to_addrs="yashrockybhai72@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )