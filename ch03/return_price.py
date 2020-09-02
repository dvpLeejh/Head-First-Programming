import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where+2
    end_of_price = where+6
    return(text[start_of_price:end_of_price])

price_now = input("Do you want to see the price now(Y/N)?")

if price_now == "Y":
    print(get_price())
else:
    price = 99.99
    time.sleep(1)
    while price > 4.74:
        price = float(get_price())

print("Buy!")
