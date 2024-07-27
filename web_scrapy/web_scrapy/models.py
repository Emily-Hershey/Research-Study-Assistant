# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

'''from scrapy.item import Item, Field


class WebScrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic = Field()
    link = Field()
    text = Field()
    summary = Field()'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer 
Base = declarative_base()


class WebScrapyModel(Base):
    __tablename__ = 'scrapy_database'
    id = Column(Integer, primary_key=True)
    topic = Column(String)
    link = Column(String)
    text = Column(String)
    summary = Column(String)