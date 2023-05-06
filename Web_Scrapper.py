import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.example.com'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))



with open('links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for link in links:
        writer.writerow([link.get('href')])
