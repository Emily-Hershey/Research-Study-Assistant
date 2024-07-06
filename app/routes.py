from flask import jsonify, request
from app import app, db
from models import Database
from flask_cors import CORS



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
        
@app.route("/", methods=['GET'])
def display_page(): 
    print("FEFE")
    # test   
    user_text = "Hello I am user and I like to text"
    Database.insert_data('user-input', 'user-input-link', user_text, '')
    Database.insert_data('user-input2', 'user-input2-link', "babppsk", '')
    
    # test end
    database = Database.query.all()  # Gives us a list of all the rows in the Database database as Python objects
    '''for item in database:
        print(f"ID: {item.id}, Topic: {item.topic}, Link: {item.link}, Text: {item.text}, Summary: {item.summary}")
    '''
    json_database = list(map(lambda x: x.to_json(), database))  # converts Python objects into JSON
    return jsonify({"database": json_database})  # returns JSON object under the 'database' key in the JSON library



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

    app.run(debug=True)