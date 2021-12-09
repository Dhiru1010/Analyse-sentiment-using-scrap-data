import scrapy
from ..items import BlackinternItem
import pandas as pd


class ExtracterOnline(scrapy.Spider):
    name = 'quotes'
    start_urls = []

    def __init__(self):
        # run through the excel sheet for extract data
        # this is the most time taking task for the project
        df = pd.read_excel("E:/Blackoffer/Input.xlsx")
        for i in range(170):
            urls = df['URL'][i]
            self.start_urls.append(str(urls))

    def parse(self, response):
        item = BlackinternItem()  # created the item to store data in
        title = response.css('title::text').extract()
        tex = response.css('div.td-post-content p::text').extract()
        text = title + tex
        item['text'] = text
        yield item

# after running the programme in terminal we can save programme using the follow command
# scrapy crawl quotes -o data.csv
# after that we use jupyter notebook for the data science work
