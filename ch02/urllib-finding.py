import urllib.request


price = 99.9

while price > 4.74:
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf-8")

    where = text.find(">$")

    start_of_price = where+2
    end_of_price = start_of_price+4

    price = float(text[start_of_price:end_of_price])

print("buy!")
