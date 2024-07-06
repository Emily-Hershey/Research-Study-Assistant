#for each source (row in db bc only want sources that were succesfully scraped), will try to scrape the summary. Summarization function iwll return whether or not succesful, and if not, will ai generate summary.

import sqlite3
import torch
from transformers import pipeline

def summarize_source():
   
    summarizer = pipeline(
        "summarization",
        "pszemraj/long-t5-tglobal-base-16384-book-summary",
        device=0 if torch.cuda.is_available() else -1,
    )
    result = summarizer(rows[0][1])


    conn = sqlite3.connect('app/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM database')
    rows = cursor.fetchall()
    for i in range(rows.length):
        #add summary to row column 3
        cursor.execute('''
            UPDATE database SET summary=? WHERE id =?
        ''', (result, i))
        conn.commit()
    conn.close()
    return result[0]["summary_text"]
