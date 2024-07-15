import sys
import serpapi
import os
import pandas as pd
import requests 
import json
from bs4 import BeautifulSoup 
import subprocess



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
    
    spider_name = "web_scrapy"

    # Construct the base command
    command = ['scrapy', 'crawl', spider_name]

    # Add start_urls as individual -a arguments
    for url in url_list:
        command.extend(['-a', f'start_urls[]={url}'])

    # Add topic as an -a argument
    command.extend(['-a', f'topic={topic}'])
    # Start the subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the subprocess to finish (optional)
    process.wait()
   

