import scrapy

class WebScrapyItem(scrapy.Item):
    topic = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    summary = scrapy.Field()
