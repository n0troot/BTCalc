import requests
from bs4 import BeautifulSoup

usrprice = int(input("Enter buy-in price: \n"))
while True:
    try:
        lst = []
        url = 'https://data.gateio.life/api2/1/ticker/btc_usdt'
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser').text
        soup.split(',')
        lst.append(soup)
        parts = soup.split(',')
        lask = parts[5]
        try1 = float(lask[13:20])
        try2 = float(lask[13:18])
        print("Percent Change: ",float(((float(try1)) - float(usrprice)) / usrprice)*100,"%")
        print("Current Price: ",try1,"$")
        print(" ")
    except Exception as e:
        print("Percent Change: ",float(((float(try1)) - float(usrprice)) / usrprice)*100,"%")
        print("Current Price: ",try2,"$")
        print(" ")
    if try1 or try2 != float:
        continue