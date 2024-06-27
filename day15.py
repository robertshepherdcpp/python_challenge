import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Choose a website that has data spread across multiple pages.
# Write a script to fetch data from all the pages.
# Extract and print specific information (e.g., titles, descriptions).
url = "https://www.example.com"
counter = 1
# here we are just iterating through the different pages
while True:
    data = requests.get(url + str(counter))
    if data.status_code != 200:
        break
    soup = BeautifulSoup(data.text, "html.parser")
    titles = soup.find_all("h1")
    descriptions = soup.find_all("p")
    if not titles or not descriptions:
        break
    for i in titles:
        print(i)
    for j in descriptions:
        print(j)
    counter += 1

# Choose a website that uses JavaScript to load content dynamically.
# Use Selenium to fetch the dynamic content.
# Extract and print specific information (e.g., titles, descriptions).
url = 'http://example.com/Dynamic'
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
titles_two = soup.find_all("h1", class_="big_titles")
para = soup.find("h", class_="info")
driver.quit()

for i in titles_two:
    print(i)
print(para)

# Combine both pagination and dynamic content handling.
# Extract data from a multi-page website that uses JavaScript to load content.
my_url = 'http://example.com/dynamic'
counter = 1
while True:
    driver = webdriver.Chrome()
    driver.get(my_url + str(counter))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = soup.find_all("h2", class_="small_header")
    paragraphs = soup.find_all("p", class_="paragraph")
    print(titles)
    print(paragraphs)
    counter += 1
driver.quit()
