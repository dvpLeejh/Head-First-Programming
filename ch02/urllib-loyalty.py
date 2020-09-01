import urllib.request

page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
text = page.read().decode("utf-8")

print(text)
