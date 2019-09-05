import requests
from bs4 import BeautifulSoup
URL = 'https://www.jumia.co.ke/universal-64gb-64g-usb-2.0-foldable-flash-memory-stick-drive-data-storage-thumb-pen-disk-green-8897807.html'
headers = {"User_Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('div', class_="details -validate-size").get_text()

price = soup.find('span', class_="price").get_text()
print(title)
print(price)


