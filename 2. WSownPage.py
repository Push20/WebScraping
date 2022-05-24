from bs4 import BeautifulSoup

# working with files to open html file
with open ('Python\WebScraping\home.html','r') as html_file:
    # read html file
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    
    # class is a keyword in python so use class_
    divs = soup.find_all('div', class_='Card')
    for div in divs:
        # print(div.p.text)
        # prints the price of the product
        print(div.find('p', class_='price').text)

