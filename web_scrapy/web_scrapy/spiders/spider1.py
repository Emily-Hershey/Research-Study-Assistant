import scrapy
from bs4 import BeautifulSoup 
import requests 
import sqlite3
from google.cloud import translate_v2 as translate

import sys
import os

sys.path.append('C:/Users/hersh/Practice-Questions-Bot-1/web_scrapy/web_scrapy')
from items import WebScrapyItem

class Spider1(scrapy.Spider):
    name = "spider1"
    '''allowed_domains = ["example.com"] start_urls = ["https://en.wikipedia.org/wiki/American_Revolution"]
    '''
   

    def __init__(self, *args, **kwargs):
        super(Spider1, self).__init__(*args, **kwargs)
        print("AWOOOOOOOSH")
        self.start_urls = kwargs.get('start_urls', [])
        self.topic = kwargs.get('topic')
        print(f"start_urls: {self.start_urls}, topic: {self.topic}")
        
    def start_requests(self):
        print("start_requests initiated")
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # for each website, scrapes the content and summary and adds all info to database
        # gathers text content from website
        paragraphs_list = response.xpath('//p/text()').getall()
        paragraphs_text = ' '.join(paragraphs_list)
        print("FESEDSFSEF")
        # Attempt to find the summary in different sections
        source_summary = response.css('div.summary p::text').get()
        # If you prefer to use XPath
        # summary = response.xpath('//div[@class="summary"]/p/text()').get()
        if not source_summary:
            source_summary = response.css('div.conclusion p::text').get()
        if not source_summary:
            source_summary = response.css('div.abstract p::text').get()
        translated_text = [] 
        headings = response.css('h1::text, h2::text, h3::text, h4::text, h5::text, h6::text').getall()
        for heading in headings:
            if len(heading) > 1:
                translated_text.append(self.translate_text(heading))
        source_summary = '\n'.join(translated_text)

        item =  WebScrapyItem()
        item['topic'] = self.topic
        item['link'] = response.url
        item['text'] = 'paragraphs_text'
        item['summary'] = source_summary
        print("ITEM", item['text'])
        
        yield item

