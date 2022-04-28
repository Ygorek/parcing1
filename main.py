import requests
from bs4 import BeautifulSoup

url = 'https://cryptoprices.com/wp-admin/admin-ajax.php?draw=1&columns%5B0%5D%5Bdata%5D=rank&columns%5B0%5D%5Bname%5D=rank&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=name&columns%5B1%5D%5Bname%5D=name&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=price_usd&columns%5B2%5D%5Bname%5D=price_usd&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=percent_change_24h&columns%5B3%5D%5Bname%5D=percent_change_24h&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=market_cap_usd&columns%5B4%5D%5Bname%5D=market_cap_usd&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=volume_usd_24h&columns%5B5%5D%5Bname%5D=volume_usd_24h&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=available_supply&columns%5B6%5D%5Bname%5D=available_supply&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=weekly&columns%5B7%5D%5Bname%5D=weekly&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=actions&columns%5B8%5D%5Bname%5D=actions&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false&action=coinmc_table&id=9&watchlist=false&restrict=true&currency=USD&_=1651178329114'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
    "X-Requested-With": "XMLHttpRequest"
    }

result = requests.get(url, headers=headers).json()

for coin in result["data"]:
    name_soup = BeautifulSoup(coin["name"], "lxml")
    price_soup = BeautifulSoup(coin["price_usd"], "lxml")

    name_soup = name_soup.find("img").get("alt")
    price_soup = price_soup.find_all("span")[-1].text
    print(f"{name_soup}: {price_soup}")

    with open("result", "a") as file:
        file.write(f"{name_soup}: {price_soup}\n")
# print(f"{price_soup}\n{name_soup}")
#    print(f"{coin}\n")
#print(result)