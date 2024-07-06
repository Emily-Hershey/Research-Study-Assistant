def run_model_on_data():
    conn = sqlite3.connect('database.db')  # Connect to the same database
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM websites')
    rows = cursor.fetchall()
    

    model_name = "deepset/tinyroberta-squad2"

    # a) Get predictions
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {
        'question': 'Who was Patrick Henry?',
        'context': rows[0][1]
    }
    res = nlp(QA_input)
    
    conn.close()

    return res
    