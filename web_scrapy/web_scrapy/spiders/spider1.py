import scrapy
from bs4 import BeautifulSoup 
import requests 
import sqlite3

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
        paragraphs_list = response.xpath('//p/text()').getall()
        #print("Paragraphs:", paragraphs)
        paragraphs_text = ' '.join(paragraphs_list)
        
        conn = sqlite3.connect('example.db')  # 'example.db' is the database file
        cursor = conn.cursor()  # cursor object allows you to execute SQL commands
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS websites (
                topic TEXT,
                text TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO websites (topic, text) VALUES ('history', ?)
        ''', (paragraphs_text,))
        conn.commit()
        cursor.execute('SELECT * FROM websites')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


        
        conn.close()



