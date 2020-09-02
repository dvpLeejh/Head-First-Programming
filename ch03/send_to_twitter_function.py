import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where+2
    end_of_price = where+6
    return(text[start_of_price:end_of_price])

def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API","http://tiwtter.com/statuses". "ID", "password")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.lrequest.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode({'status':msg})
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()    

price_now = input("Do you want to see the price now(Y/N)?")

if price_now == "Y":
    msg = get_price()
    send_to_tiwtter(msg)
else:
    price = 99.99
    while price > 10:
        price = float(get_price())
    msg = "Buy!"
    send_to_tiwtter(msg)
    
