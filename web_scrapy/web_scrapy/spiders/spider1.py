import scrapy
from bs4 import BeautifulSoup 
import requests 


class Spider1(scrapy.Spider):
    name = "spider1"
    '''allowed_domains = ["example.com"]
    start_urls = ["http://example.com"]'''

    def __init__(self, start_urls=None, *args, **kwargs):
        super(Spider1, self).__init__(*args, **kwargs)
        
        print("\n\n\n\n")
        print(start_urls)
        print("\n\n\n\n")
        self.start_urls = start_urls if start_urls else []

    def start_requests(self):
        for url in self.start_urls:
            if url:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''for item in response.css('p'):
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
            r = requests.get(url=item.css('a::attr(href)').get(), headers=headers) 
            #soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
            #paragraph_text = soup.find('p').get_text()
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')
                        
                # Extract text from all <p> tags in the page
                paragraph_text = '\n'.join([p.get_text() for p in soup.find_all('p')])
                
                yield {
                    'title': item.css('a::text').get(),
                    'link': item.css('a::attr(href)').get(),
                    'paragraph_text': paragraph_text
                }
        '''
        '''text_content = response.css('body').xpath('string()').get()
        
        # Now you can do whatever you want with the text_content
        # For example, you can print it
        print(text_content)

         # Extract text from the entire page
        page_text = response.css('body').xpath('string()').get()

        yield {
            'page_text': page_text
        }
        '''
        paragraphs = response.xpath('//p/text()').getall()
        print("Paragraphs:", paragraphs)

