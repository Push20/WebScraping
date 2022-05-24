# requires pip to install beautifulsoup4, requests(third one), and lxml
from bs4 import BeautifulSoup

# working with files to open html file
with open ('Python\WebScraping\home.html','r') as html_file:
    # read html file
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    # prints the whole html file
    # print(soup.prettify())

    # find the tag and print it
    # tags = soup.find('h1')
    # print(tags)

    # find the tag and print it
    headings = soup.find_all('h1')
    # print(headings)

    for heading in headings:
        print(heading.text)