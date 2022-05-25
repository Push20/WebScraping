from re import search,findall
from xml.etree.ElementPath import find
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

topicSearch = input("What would you like to search for? ")

topicSearch = topicSearch.replace(" ","+")

brower = webdriver.Chrome()

elements = brower.get("https://www.google.com/search?q="
                        + topicSearch + "&start=" + str(0))

# tesco, morrisons, asda, sainsbury's
brower.get("https://www.tesco.com/groceries/en-GB/search?query="+ topicSearch)

TItems = brower.find_elements(By.CLASS_NAME,value="product-details--wrapper")
if len(TItems) == 0:
    print("No items found")
else:
    TProducts = []
    # looping through the product Tdetails and extracting the product name and price into TProducts list
    for i,product in enumerate(TItems):
        Titem = []
        Tdetails= []
        Titem = product.text.split("\n")
        # Rice name
        Tdetails.append(Titem[0])
        if len(Titem) == 6:
            # out of shelf
            Tdetails.append(Titem[2])
        # club card
        elif len(Titem) == 13:
            # club card price
            Tdetails.append(Titem[6])
            # normal price
            Tdetails.append(Titem[8])
        else:
            # normal price
            Tdetails.append(Titem[5])
        TProducts.append(Tdetails)

    # print all of the TProducts list
    for i in TProducts:
        print(i)

    # extracting the prices of the product
    Tproducts_price = []
    for i in range(len(TProducts)):
        Tprices = []
        for j in range(1,len(TProducts[i])):
            # adding the price to the list
            if search(r'\d+',TProducts[i][j]):
                # removes all unwanted characters
                TProducts[i][j] = TProducts[i][j].replace('£','')
                TProducts[i][j] = TProducts[i][j].replace(' Clubcard Price','')
                Tprices.append(float((findall(r'^\d*[.,]?\d*$',TProducts[i][j]))[0]))
        Tproducts_price.append(Tprices)

    Tmin = 9999999.99
    Tindex = 0
    # finding the minimum price
    if len(Tproducts_price) > 0:
        for i in range (len(Tproducts_price)):
            for j in range(len(Tproducts_price[i])):
                # is price is a number
                if type(Tproducts_price[i][j]) == float and (Tproducts_price[i][j]) < Tmin:
                    Tmin = (Tproducts_price[i][j])
                    Tindex = i

    Tminimum =(TProducts[Tindex])

    # prints the minimum price product
    #if Tminimun[1]  doesnt contain any digits with regex
    if findall(r'\d+',Tminimum[1]) == []:
        print("Sorry no product is available currently")
    elif len(Tminimum) == 3:
        print("{} with a clubcard price of {} is the cheapest".format(Tminimum[0],Tminimum[1]))
    else:
        print("{} with a normal price of {} is the cheapest".format(Tminimum[0],Tminimum[1]))

print("--------------------Morrisons--------------------")
brower.get("https://groceries.morrisons.com/search?entry="+ topicSearch)
MItems = brower.find_elements(By.XPATH,value="//ul[@class='fops fops-regular fops-shelf']/li")
if len(MItems) == 0:
    print("No items found")
else:
    MProducts = []
    # looping through the product Tdetails and extracting the product name and price into TProducts list
    for i,product in enumerate(MItems):
        Mitem = []
        Mdetails= []
        Mitem = product.text.split("\n")
        
        # remove by the first element
        Mitem.pop(0)
        # checks if the first element is "new"
        if Mitem[0] == "New":
            # removes the first element
            Mitem.pop(0)
        if Mitem[-1] == "Add to trolley":
            # removes the last element
            Mitem.pop(-1)
        # removes the last element if it contains per or each within the string
        while search(r'(per|each|Out of stock)',Mitem[-1]):
            Mitem.pop(-1)
        if Mitem[0] == "Out of Stock":
            # out of shelf
            Mdetails.append(Mitem[1])
            Mdetails.append(Mitem[0])
        else:
            Mdetails.append(Mitem[0])
            Mdetails.append(Mitem[-1])
        MProducts.append(Mdetails)

    # print all of the TProducts list
    for i in MProducts:
        print(i)

    # extracting the prices of the product
    Mproducts_price = []
    for i in range(len(MProducts)):
        Mprices = []
        for j in range(1,len(MProducts[i])):
            # adding the price to the list
            if search(r'\d+',MProducts[i][j]):
                # removes all unwanted characters
                MProducts[i][j] = MProducts[i][j].replace('£','')
                MProducts[i][j] = MProducts[i][j].replace(' Clubcard Price','')
                Mprices.append(float((findall(r'^\d*[.,]?\d*$',MProducts[i][j]))[0]))
        Mproducts_price.append(Mprices)
        

    Mmin = 9999999.99
    Mindex = 0
    # finding the minimum price
    if len(Mproducts_price) > 0:
        for i in range (len(Mproducts_price)):
            for j in range(len(Mproducts_price[i])):
                if type(Mproducts_price[i][j]) == float and (Mproducts_price[i][j]) < Mmin:
                    Mmin = (Mproducts_price[i][j])
                    Mindex = i

    Mminimum =(MProducts[Mindex])

    # prints the minimum price product
    #if Tminimun[1]  doesnt contain any digits with regex
    if findall(r'\d+',Mminimum[1]) == []:
        print("Sorry no product is available currently")
    else:
        print("{} with the price of {} is the cheapest".format(Mminimum[0],Mminimum[1]))

print("-----------------------Asda-----------------------")
asda = brower.get("https://groceries.asda.com/search/"+ topicSearch)
brower.find_element(By.CLASS_NAME,value="search-page-content__sort search-page-content__sort--product").click()
brower.find_element(By.ID,value="price").click()
# if len(MItems) == 0:
#     print("No items found")
# else:

# sainsbury = brower.get("https://www.sainsburys.co.uk/shop/gb/groceries/search?q="
# + topicSearch)



brower.close()

# wait implicitly for 10 seconds
# wait = WebDriverWait(brower, 10)