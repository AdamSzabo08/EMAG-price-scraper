import requests
from bs4 import BeautifulSoup

URL = 'https://www.emag.ro/telefon-mobil-samsung-galaxy-s21-ultra-dual-sim-512gb-16gb-ram-5g-phantom-black-sm-g998bzkheue/pd/DWLGTDMBM/?X-Search-Id=4f3fafd2baa3da7c5d0b&X-Product-Id=7579464&X-Search-Page=1&X-Search-Position=1&X-Section=search&X-MB=0&X-Search-Action=view'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(class_="page-title").get_text()
price = soup.find(class_="product-new-price").get_text()

print(price.strip())
print(title.strip())

