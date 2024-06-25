import requests
from bs4 import BeautifulSoup

url = 'http://google.com'
response = requests.get(url)

# Check the status of the response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for heading in headings:
        print(heading.text)
    urls = soup.find_all(['a'])
    for url in urls:
        print(url)
    para = soup.find('p')
    print(para)
