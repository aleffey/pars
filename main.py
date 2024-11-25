from fpdf import fpdf
from bs4 import BeautifulSoup
import requests
url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
response = requests.get(url)
print(response)
bs = BeautifulSoup(response.text, "lxml")
print(bs)
temp = bs.find("span", "temp__value temp__value_with-unit")
print("XXXXXXXXXXXXXXXXXXXXX")
print(temp)
print("status")