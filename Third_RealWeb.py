from bs4 import BeautifulSoup
import requests as re

html_text = re.get('https://uk.indeed.com/jobs?q=software%20engineer&l=Leicester&vjk=ca6a398bc7058012')
# print(html_text) = <Response [200]>
soup = BeautifulSoup(html_text.text, 'lxml')

# gets all the class = "sidebar"
jobs = soup.find('div', class_='slider_item')

# class = "date"
date = jobs.find('span', class_='date').text


print(1,date)
