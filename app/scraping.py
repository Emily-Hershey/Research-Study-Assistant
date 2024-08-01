import sys
import os
import requests 
from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings

from scrapy.utils.project import get_project_settings
crawler_settings = get_project_settings()
scrape_in_progress = False
scrape_complete = False
from twisted.internet import defer



'''The below code allows us to import Spider1, despite it not being in the current directory'''

# Determine the project root dynamically
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_script_dir, '..'))


# Add the root directory to sys.path
sys.path.insert(1, project_root)
# Now you should be able to import Spider1
from web_scrapy.web_scrapy.spiders.spider1 import Spider1
import web_scrapy.web_scrapy.settings as my_settings  # Adjust this import as needed


'''
need to handle when topic is empty
'''
def run_spider(topic):
    params = {
        'api_key':'key',
        'q':topic,
        'engine':'google',
        'hl':'en',
    }
    api_result = requests.get('https://api.scaleserp.com/search', params)
    response_data = api_result.json()
    url_list = []
    for item in response_data["organic_results"]:
        URL = item['link'] 
        url_list.append(URL)
    
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    crawl_runner = CrawlerRunner(settings=crawler_settings)      # requires the Twisted reactor to run

    global scrape_in_progress
    global scrape_complete

    if not scrape_in_progress:
        scrape_in_progress = True
        eventual = crawl_runner.crawl(Spider1, start_urls=url_list, topic=topic)
        eventual.addCallback(finished_scrape)
        return eventual
    elif scrape_complete:
        return defer.succeed('SCRAPE COMPLETE')
    return defer.succeed('SCRAPE IN PROGRESS')

def finished_scrape(null):
    """
    A callback that is fired after the scrape has completed.
    Set a flag to allow display the results from /results
    """
    global scrape_complete
    scrape_complete = True

