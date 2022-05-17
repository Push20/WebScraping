from bs4 import BeautifulSoup
import requests as reg
# import httpx

# start timer
import time
start_time = time.time()
shop = int(input("1.Morrisons\n2.Sainsbury\n3.Tesco\n4.Asda"))
# realised sainsburys website is made with js
# response takes too long

if shop == 1:
    html_text = reg.get('https://groceries.morrisons.com/search?entry=rice%2010kg')
    # print("yo",html_text)# = <Response [200]>
    soup = BeautifulSoup(html_text.text, 'lxml')

    # gets all the class = "sidebar"
    Products = soup.find_all('div', class_='fop-contentWrapper')
    min = 99999999999
    min_product = set()
    for product in Products:
        price = product.find('span', class_='fop-price').text
        if int(price.replace('£','').replace('.','')) <11:
            min_product.add(product)
        elif int(price.replace('£','').replace('.','')) <= min:
            min = int(price.replace('£','').replace('.',''))
            min_product = (product)


    productName = min_product.find('h4', class_='fop-title').text
    price = min_product.find('span', class_='fop-price').text
    print(productName,price)
    # print time taken
    print("--- %s seconds ---" % (time.time() - start_time))

elif shop ==2:
    html_text = reg.get('https://www.tesco.com/groceries/en-GB/search?query=rice%2010kg',headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"})
    # html_text = reg.get('https://www.sainsburys.co.uk/shop/gb/groceries/rice-10kg')
    # print("yo",html_text)# = <Response [200]>
    soup = BeautifulSoup(html_text.text, 'lxml')
    print(soup)
    # get element with class = "styles__StyledTiledContent-dvv1wj-3 bcglTg"
    Products = soup.find_all('div', class_='styles__StyledTiledContent-dvv1wj-3 bcglTg')
    # if soup rege 'styles__StyledTiledContent-dvv1wj-3 bcglTg')

    print(price)

    # gets all the class = "sidebar"
    # Products = soup.find_all('div', class_='product-details')
    # min = 99999999999
    # min_product = set()
    # for product in Products:
    #     price = product.find('span', class_='pricePerUnit').text
    #     if int(price.replace('£','').replace('.','')) <11:
    #         min_product.add(product)
    #     elif int(price.replace('£','').replace('.','')) <= min:
    #         min = int(price.replace('£','').replace('.',''))
    #         min_product = (product)


    # productName = min_product.find('h3', class_='productTitle').text
    # price = min_product.find('span', class_='pricePerUnit').text
    # print(productName,price)

elif shop == 3:
    print("Can't get soup from tesco's website")

elif shop == 4:
    html_text = reg.get('https://groceries.asda.com/search/rice%2010kg?cmpid=ahc-_-ghs-_-asdacom-_-hp-_-search-rice-10kg')

    soup = BeautifulSoup(html_text.text, 'lxml')

    print(soup.text)

    product = soup.find('div', class_=' co-item co-item--rest-in-shelf ')
    print(product)

    price = soup.find('strong', class_='co-product__price')
    print(price)
