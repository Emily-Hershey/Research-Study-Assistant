import scrapy
from bs4 import BeautifulSoup 
import requests 
import sqlite3

class Spider1(scrapy.Spider):
    name = "spider1"
    '''allowed_domains = ["example.com"]
    start_urls = ["http://example.com"]'''

    def __init__(self, start_urls=None, topic=None, *args, **kwargs):
        super(Spider1, self).__init__(*args, **kwargs)
        self.start_urls = start_urls if start_urls else []
        self.topic = topic

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # for each website, scrapes the content and summary and adds all info to database
        # gathers text content from website
        paragraphs_list = response.xpath('//p/text()').getall()
        paragraphs_text = ' '.join(paragraphs_list)
        
        # Attempt to find the summary in different sections
        source_summary = response.css('div.summary p::text').get()
        # If you prefer to use XPath
        # summary = response.xpath('//div[@class="summary"]/p/text()').get()
        if not source_summary:
            source_summary = response.css('div.conclusion p::text').get()
        item = {
            'topic': self.topic,
            'link': response.url,
            'text': paragraphs_text,
            'summary': source_summary,
        }
        yield item



