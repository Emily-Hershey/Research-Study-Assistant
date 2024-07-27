# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from itemadapter import ItemAdapter
import os
import sys
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import logging 
import sqlite3
from .items import WebScrapyItem
# Add the root directory to sys.path
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_script_dir, '..', '..'))
print("PROJECT_ROOT", project_root)
sys.path.insert(1, project_root)
from app import app,db
from settings import DATABASE
from .models import WebScrapyModel, Base  # Import your SQLAlchemy model

# useful for handling different item types with a single interface
class WebScrapyPipeline:
    def __init__(self, db_url):
        print("init")

        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    @classmethod
    def from_crawler(cls, crawler):
        db_url = crawler.settings.get('DATABASE_URL')
        return cls(db_url)

    '''def open_spider(self, spider):
        # pushes the Flask app context, making sure that the database session is correctly set up.
        self.app_context = app.app_context()
        self.app_context.push()
        self.session = self.Session()

    def close_spider(self, spider):
        # pops the app context, cleaning up the session
        self.app_context.pop()
        self.session.close()'''

    def process_item(self, item, spider):
        # Create a new entry and add it to the session
        
        print("AWFOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        '''new_entry = Database(
            topic=item.get('topic'),
            link=item.get('link'),
            text=item.get('text'),
            summary=item.get('summary')
        )'''
        
        session = self.Session()
        adapter = ItemAdapter(item)
        new_entry = WebScrapyModel(
            topic=adapter.get('topic'),
            link=adapter.get('link'),
            text=adapter.get('text'),
            summary=adapter.get('summary')
        )
        try:
            session.add(new_entry)
            session.commit()
            print(f"Topic: {new_entry.topic}")
            print(f"Link: {new_entry.link}")
            print(f"Text: {new_entry.text}")
            print(f"Summary: {new_entry.summary}")
            logging.debug(f"Item committed to database: {item}")
        except IntegrityError:
            print("Error")
            session.rollback()
            logging.error(f"IntegrityError: Could not insert item {item}")
        except Exception as e:
            print("Exception")
            session.rollback()
            logging.error(f"Error: {e}")
        print("Item returned")

        return item