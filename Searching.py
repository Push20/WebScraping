from re import search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

topicSearch = input("What would you like to search for?")

topicSearch = topicSearch.replace(" ","+")

brower = webdriver.Chrome()

brower.get("https://www.google.com/")

for i in range(1):
    elements = brower.get("https://www.google.com/search?q="
                          + topicSearch + "&start=" + str(i))

# brower.close()

# wait implicitly for 10 seconds
wait = WebDriverWait(brower, 10)