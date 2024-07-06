# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from itemadapter import ItemAdapter
import os
import sys
from sqlalchemy.exc import IntegrityError

# ensures that the Python interpreter can find the Flask app.
sys.path.append('/Users/hersh/Practice-Questions-Bot-1/app')
from app import app,db
from app import Database

# useful for handling different item types with a single interface
class WebScrapyPipeline:
    def open_spider(self, spider):
        # pushes the Flask app context, making sure that the database session is correctly set up.
        self.app_context = app.app_contect()
        self.app_context.push()

    def close_spider(self, spider):
        # pops the app context, cleaning up the session
        self.app_context.pop()

    def process_item(self, item, spider):
        # Create a new entry and add it to the session
        new_entry = Database(
            topic=item.get('topic'),
            link=item.get('link'),
            text=item.get('text'),
            summary=item.get('summary')
        )
        try:
            db.session.add(new_entry)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return item
