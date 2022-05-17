
# importing the modules
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
  
# using webdriver for chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
  
# using target url
driver.get(
    "https://www.tesco.com/groceries/en-GB/search?query=rice%2010kg&icid=tescohp_sws-1_m-ft_in-rice%2010kg_ab-226-b_out-rice%2010kg")
  
# printing the content of entire page
# WholePage = (driver.find_element_by_xpath("/html/body").text)

# printing the content of the page which is digits only
words = (driver.find_element_by_xpath("/html/body").text).split("\n")

print(words)
# using regular expression to get the prices only
Rices = []
for index,word in enumerate(words):
    if "Rice 10Kg" in word:
        Rices.append(word)

    #prices
    if re.search(r'£\d', word) != None:
        Rices.append(word)
    if re.search(r'£\s\d', word) != None:
        Rices.append(word)

arr = []
#clean of words with trolley
for word in (Rices):
    #using regular expression to get rid of the trolley
    if re.search(r'trolley$', word) != None:
        # print(words[index-1],"\n",word)
        Rices.remove(word)
    elif re.search(r'^Add\s', word) != None:
        # print(words[index-1],"\n",word)
        Rices.remove(word)
    else:
        arr.append(word)    

print(arr)

Rices.clear()
products = {}
pros = []
for word in arr:
    if "/kg" in word:
        #finds the indes of the word
        index = arr.index(word)
        pros.append( arr[0:index+1])
        arr = arr[index+1:len(arr)]
        
for i in pros:
    products[i[0]] = i[1:len(i)+2]
print(products)

print(products['Laila Basmati Rice 10Kg'])
    # if re.search(r' Rice ',word) != None:
    #     print("Rice",word)

# for i in DigitsOnly:
#     # if i starts with £ 
#     price.append(re.findall('^£[0-9]', i))
#         # print the value
        
# print(price)
# print(re.find[0-9]=="\d")
  
# closing the driver
driver.close()