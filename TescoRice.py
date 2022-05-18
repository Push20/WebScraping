# importing the modules
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
  
# using webdriver for chrome browser
driver = webdriver.Chrome()
  
# using target url
driver.get("https://www.tesco.com/groceries/en-GB/search?query=rice%2010kg&icid=tescohp_sws-1_m-ft_in-rice%2010kg_ab-226-b_out-rice%2010kg")

productDetails = (driver.find_elements(By.CLASS_NAME,value="product-details--wrapper"))

products = []

# looping through the product details and extracting the product name and price into products list
for i,product in enumerate(productDetails):
    rice = []
    details= []
    rice = product.text.split("\n")
    # Rice name
    details.append(rice[0])
    # club card
    if len(rice) == 13:
        # club card price
        details.append(rice[6])
        # normal price
        details.append(rice[8])
    else:
        # normal price
        details.append(rice[5])
    products.append(details)

# print all of the products list
for i in products:
    print(i)

# extracting the prices of the product
products_price = []
for i in range(len(products)):
    prices = []
    for j in range(1,len(products[i])):
        # adding the price to the list
        if re.search(r'\d+',products[i][j]):
            # removes all unwanted characters
            products[i][j] = products[i][j].replace('£','')
            products[i][j] = products[i][j].replace(' Clubcard Price','')
            prices.append((re.findall(r'^\d*[.,]?\d*$',products[i][j]))[0])
    products_price.append(prices)

min = 9999999.99
# finding the minimum price
for i in range (len(products_price)):
    for j in range(len(products_price[i])):
        if float(products_price[i][j]) < min:
            min = float(products_price[i][j])
            index = i

minimum =(products[index])

# prints the minimum price product
if len(minimum) == 3:
    print("{} with a clubcard price of {}".format(minimum[0],minimum[1]))
else:
    print("{} with a normal price of {}".format(minimum[0],minimum[1]))

driver.close()