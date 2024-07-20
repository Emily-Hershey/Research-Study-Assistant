import sys
import os
import asyncio
from twisted.internet import asyncioreactor

# Set the event loop policy to SelectorEventLoop for Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Install the asyncio reactor
asyncioreactor.install()



from flask import jsonify, request, session
from sqlalchemy.exc import IntegrityError

from app import app, db
from models import Database
from flask_cors import CORS
from scraping import run_spider

from flask_twisted import Twisted
from twisted.internet import reactor, defer
from twisted.internet.defer import inlineCallbacks, returnValue

from scraping import run_spider
import threading


'''
How I plan to split this up now: First page is where the user can enter their own paragraph, with button for entering info,
This button adds info to database and then send it to summary model function. Also with button on the bottom for 
going to next page. THis button prompts the website to switch layout and display info on graph. 
Area on top for searching topics. Summary will only be taken from website, no custom summary. Perhaps will add a button for users
to chose whether they want it, where warning will pop up of time that summary will take. 

Timer function to automatically update page every 10 or so seconds so that graph is accurate to database, esp when summary functions finish running.

'''

'''
@app.route('/update_database', methods=['GET', 'POST'])
def update_database():
        search = request.json.get('topic')  # user input topic
        user_text = request.json.get('user_text')  # user input of personal notes, document text, etc
        
        if not search and not user_text:
            return (
                jsonify({"message": "You must enter something to be processed"}), 
                400,
            )
        if search:
            run_spider()
        else: 
            new_entry = Database(topic='user-input', link='user-input', text=user_text, summary='')
            try:
                db.session.add(new_entry)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
'''   

@app.route("/", methods=['GET', 'POST'])
def search_button(): 
    global search_term
    if request.method == 'POST':
        print("search received")
        data = request.get_json()
        search_term = data.get('search')
        input_box = data.get('input_box')
        if search_term:
            run_spider(search_term)
            print("Finished scraping mode")
            return "Search Received"
        elif input_box:
            new_entry = Database(topic='user-input', link='user-input', text=input_box, summary='')
            try:
                db.session.add(new_entry)
                db.session.commit()
                return "Input Received"

            except IntegrityError:
                db.session.rollback()
                return "Error adding input to database"
        else:
            return "No search performed"
    else:
        # Handle GET request for status or other purposes  
            
        # update the database
        database = Database.query.all()  # Gives us a list of all the rows in the Database database as Python objects
        for item in database:
            print(f"ID: {item.id}, Topic: {item.topic}, Link: {item.link}")
        if not database:
            print("\n\nempty\n\n")
        json_database = list(map(lambda x: x.to_json(), database))  # converts Python objects into JSON
        print("1")
        response = jsonify({"database": json_database})  # returns JSON object under the 'database' key in the JSON library
        print("2")
        return response 
        
        '''
        print("4")
        # Wait for the Deferred to complete and get the result
        d.addCallback(lambda result: (print("5"), result))            
        return d'''


@app.route('/chatbot')
def chatbot():
        '''elif action == 'qa':
            question = data.get('content')
            answer = run_model_on_data(question)
            return jsonify({"answer": answer})

        else:
            return jsonify({"error": "Invalid action"})'''

'''
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/run-script', methods=['POST'])
def run_script():
    subprocess.run(['python', 'your_script.py'])
    return jsonify({'message': 'Script executed successfully'})

@app.route('/data', methods=['GET'])
def get_data():
    data = Data.query.all()
    results = [{'id': item.id, 'content': item.content} for item in data]
    return jsonify(results)'''



''' return f"Hello, {escape(name)}!"'''

if __name__ == '__main__':
    with app.app_context():
        Database.reset_database()  # Reset the database
    from sys import stdout
    from twisted.logger import globalLogBeginner, textFileLogObserver
    from twisted.web import server, wsgi
    from twisted.internet import endpoints, reactor

    # start the logger
    globalLogBeginner.beginLoggingTo([textFileLogObserver(stdout)])

    # start the WSGI server
    root_resource = wsgi.WSGIResource(reactor, reactor.getThreadPool(), app)
    factory = server.Site(root_resource)
    http_server = endpoints.TCP4ServerEndpoint(reactor, 9000)
    http_server.listen(factory)

    # start event loop
    reactor.run()
