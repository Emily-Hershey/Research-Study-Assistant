import sys
import serpapi
import os
import pandas as pd
import requests 
import json
from bs4 import BeautifulSoup 
import json

from klein import route, run
from scrapy import signals
from scrapy.crawler import CrawlerRunner

from scrapy.utils.project import get_project_settings
crawler_settings = get_project_settings()




'''The below code allows us to import Spider1, despite it not being in the current directory'''

#sys.path.append('C:/Users/hersh/Practice-Questions-Bot-1/web_scrapy/web_scrapy')

# Determine the project root dynamically
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_script_dir, '..'))


# Add the web_scrapy/web_scrapy directory to sys.path
sys.path.insert(1, project_root)
# Now you should be able to import Spider1
from web_scrapy.web_scrapy.spiders.spider1 import Spider1
#import web_scrapy.web_scrapy.settings as my_settings  # Adjust this import as needed

#crawler_settings.setmodule(my_settings)
'''from PRACTICE_QUESTIONS_BOT_1.web_scrapy.web_scrapy.spiders.spider1 import Spider1 
from PRACTICE_QUESTIONS_BOT_1.web_scrapy.web_scrapy import settings as my_settings 
'''

# Rest of your code




from dotenv import load_dotenv
import sqlite3

#for summarizing model
import torch
from transformers import pipeline 

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


class MyCrawlerRunner(CrawlerRunner):
    """
    Crawler object that collects items and returns output after finishing crawl.
    """
    def __init__(self, settings=None, url_list=None, topic=None):
        super().__init__(settings)
        self.url_list = url_list
        self.topic = topic
        
    def crawl(self, crawler_or_spidercls, *args, **kwargs):
        # keep all items scraped
        self.items = []

        # create crawler (Same as in base CrawlerProcess)
        crawler = self.create_crawler(crawler_or_spidercls)

        # handle each item scraped
        crawler.signals.connect(self.item_scraped, signals.item_scraped)
         # Pass url_list and topic to spider instance
        kwargs['start_urls'] = self.url_list
        kwargs['topic'] = self.topic
        print("ORIG:", kwargs['start_urls'])
        # create Twisted.Deferred launching crawl
        dfd = self._crawl(crawler, *args, **kwargs)

        # add callback - when crawl is done cal return_items
        dfd.addCallback(self.return_items)
        return dfd

    def item_scraped(self, item, response, spider):
        self.items.append(item)

    def return_items(self, result):
        return self.items


def return_spider_output(output):
    """
    :param output: items scraped by CrawlerRunner
    :return: json with list of items
    """
    # this just turns items into dictionaries
    # you may want to use Scrapy JSON serializer here
    return json.dumps([dict(item) for item in output])

def run_spider(topic):
    params = {
        'api_key':'C7568B51036E41BCB8D7C4FCBD3D27F7',
        'q':topic,
        'engine':'google',
        'hl':'en',
    }
    '''
    api_result = requests.get('https://api.scaleserp.com/search', params)
    response_data = api_result.json()
    url_list = []
    for item in response_data["organic_results"]:
        URL = item['link'] 
        url_list.append(URL)
    '''
    url_list = []
    url_list.append("https://en.wikipedia.org/wiki/American_Revolution")
    
    '''crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)'''
    
    # run the scrapy spider
    runner = MyCrawlerRunner(url_list=url_list, topic=topic)
    # Add the Spider1 spider to the process
    #process.crawl(Spider1, start_urls=url_list, topic=topic)
    # Start the crawling process
    deferred = runner.crawl(Spider1)
    deferred.addCallback(return_spider_output)
    return deferred
