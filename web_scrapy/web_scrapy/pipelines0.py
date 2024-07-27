# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from itemadapter import ItemAdapter
import os
import sys
from sqlalchemy.exc import IntegrityError
import logging 
import sqlite3

# Add the root directory to sys.path
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_script_dir, '..', '..'))
print("PROJECT_ROOT", project_root)
sys.path.insert(1, project_root)
from app import app,db
from models import Database
print("\n\nLoading WebScrapyPipeline\n\n")

# useful for handling different item types with a single interface
class WebScrapyPipeline:
        
    def open_spider(self, spider):
        # pushes the Flask app context, making sure that the database session is correctly set up.
        self.app_context = app.app_context()
        self.app_context.push()

    def close_spider(self, spider):
        # pops the app context, cleaning up the session
        self.app_context.pop()
    
    def process_item(self, item, spider):
        # Create a new entry and add it to the session
        
        print("AWFOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        new_entry = Database(
            topic=item.get('topic'),
            link=item.get('link'),
            text=item.get('text'),
            summary=item.get('summary')
        )
        try:
            db.session.add(new_entry)
            db.session.commit()
            print("Added item correctly")
            logging.debug(f"Item committed to database: {item}")
        except IntegrityError:
            print("Error")
            db.session.rollback()
            logging.error(f"IntegrityError: Could not insert item {item}")
        except Exception as e:
            print("Exception")
            db.session.rollback()
            logging.error(f"Error: {e}")
        print("Item returned")
        return item