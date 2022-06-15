from collections import Counter as counta
from matplotlib import pyplot as plt
import random
import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup as b
import requests
from string import punctuation
import pandas as pd
import os 
import re
import other_scraper 
import file_scraper
import time
import data_management

articlePath = fr"C:/Users/{os.getlogin()}/Documents/Articles"

if (os.path.isdir(articlePath) == False):
    os.mkdir(articlePath)

companies_table = pd.read_csv(fr"C:/Users/{os.getlogin()}/Documents/Ransomware Project/table-1.csv")

companies = companies_table["Name"]

class RansomwareSpider(scrapy.Spider):
    name = 'ransomware'
    allowed_domains = ['www.wired.com']
    start_urls = ['http://www.wired.com/tag/ransomware']

    def parse(self, response):

        links = list()

        #getting links that have the term 'ransomware', then adding wired.com to said link
        for link in response.css("a::attr(href)").getall():
            if "ransomware" in link:
                links.append(f"http://www.wired.com{link}")
            else:
                pass

        paragraphs = []

        titles = []

        for link in links:
            try:
                source = requests.get(link).text

                soup = b(source, 'lxml')

                paragraph_match = soup.find("div", class_="grid--item body body__container article__body grid-layout__content").find_all('p')

                [paragraphs.append(p.text) for p in paragraph_match if p.text not in paragraphs]


                title_match = soup.find('h1', class_='content-header__row content-header__hed').text

                if not title_match in titles:
                    titles.append(title_match)

                with open(fr"C:/Documents/Users/{os.getlogin()}/Articles/wired/{title_match}.txt", 'w+') as f:
                    for p in paragraph_match:
                        f.write(p.text)
            except:
                pass
  
        #yielding dictionary data
        yield{
            'links':links

        }



process = CrawlerProcess()
process.crawl(RansomwareSpider)
process.start()

#RUN scrapy crawl ransomware in terminal to only yield objects, use python3 ransomware.py to write to files.

other_scraper.scrape_ABC()
other_scraper.scrape_top10()
file_scraper.scrape_files()
data_management.get_data()