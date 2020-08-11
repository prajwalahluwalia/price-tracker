import time

import requests
from bs4 import BeautifulSoup
import smtplib

URL ='https://www.amazon.in/Test-Exclusive-603/dp/B07HG8SBDV/ref=sr_1_3?crid=2XR1I6U19V2SK&keywords=one+plus7pro&qid=1565862253&s=electronics&smid=A35FCS7U51TK3C&sprefix=one+plu%2Celectronics%2C419&sr=1-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    price = price.replace("₹", " ")
    price = price.replace(",", "")

    converted_price = float(price[1:8])
    print(converted_price)

    if (converted_price < 44999.0):
        send_mail()

    print(title.strip())

    if (converted_price > 44999.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()               #comand sent to email server to identify itself when connecting to another email.
    server.starttls()           #encrypts connection
    server.ehlo()

    server.login('prajuaa0321@gmail.com', 'odzjybwvdsvlmlgf')

    subject = "Go check the product gareeb"
    body = 'https://www.amazon.in/Test-Exclusive-603/dp/B07HG8SBDV/ref=sr_1_3?crid=2XR1I6U19V2SK&keywords=one+plus7pro&qid=1565862253&s=electronics&smid=A35FCS7U51TK3C&sprefix=one+plu%2Celectronics%2C419&sr=1-3'

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'prajuaa0321@gmail.com ',
        'akspreet2497@gmail.com',
        msg
    )

    print("Email has been sent")

    server.quit()
while(True):
    check_price()
    time.sleep(3600)
