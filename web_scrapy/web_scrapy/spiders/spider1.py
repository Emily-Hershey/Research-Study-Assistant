import scrapy
from bs4 import BeautifulSoup 
import requests 


class Spider1(scrapy.Spider):
    name = "spider1"
    '''allowed_domains = ["example.com"]
    start_urls = ["http://example.com"]'''

    def __init__(self, start_urls=None, *args, **kwargs):
        super(Spider1, self).__init__(*args, **kwargs)
        self.start_urls = start_urls if start_urls else []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        paragraphs = response.xpath('//p/text()').getall()
        print("Paragraphs:", paragraphs)

