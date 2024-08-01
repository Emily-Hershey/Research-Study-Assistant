# Practice-Questions-Bot
Website intended for research and study assistance. Users can create custom chatbots and view previews of websites. This website aims to allow users to study more efficiently by customizing a chatbot to teach their exact course material and to research more efficiently by previewing the contents of websites in search results.
<br>
<h1>Functionalities</h1>
<h3>Chatbot</h3>
<p>Enter text-based data to the input box on the first page. This can be class notes, documentation, book pages, etc. After each entry, press the "submit" button to save your data. Click the "next page" button when done. Your data should appear in the table. You should see a small textbox and another "submit" button at the bottom of the page. Here, you can enter questions/prompts into the chatbot, which will learn from the data you previously submitted. The chatbot's response will appear in the large text area.</p>
<h3>Website Previews</h3>
<p>Press the "next" button to move to the second page. On the top of the page is a small textbox. Enter in search terms here. Press "submit" to initiate the search. The results of the search should appear in the table in the middle of the screen, including the search term, link to the website, and the main topics covered in the website.</p>

<h1>Installation</h1>
<p>This project is intended to run in a IDE and is not currently ready for deployment. </p>
<h3>Prerequisites</h3>
<p>Have your preferred IDE installed, setup, and with two fresh terminals open. Ensure Python is installed (preferably Python 3.x). Ensure Node.js and npm are installed.</p>
<h3>Setup</h3>
<ol>
  <li>Clone the Repository</li>
  ```git clone https://github.com/Emily-Hershey/Practice-Questions-Bot.git   
  cd Practice-Questions-Bot```
  <li>Create API Keys</li> 
    <li>The API keys provided are placeholders and will not work. Navigate to line 21 of app/question_answering.py. You will need to create and insert your own OpenAI API key. Navigate to line 34 of app/scraping.py. You will need to create and insert your own SerpAPI key.</li>
  <li>Set Up the Backend (Flask)</li>
    <li>Create a Virtual Environment</li> 
  ```python -m venv venv      
    source venv/bin/activate  # On Windows use `venv\Scripts\activate```
    <li>Install Backend Dependencies</li> 
    ```pip install -r requirements.txt```
    <li>Run the Backend</li> 
    ```cd app           
    Python routes.py```
  <li>Set Up the Frontend (React)</li>
    <li>In Another Terminal, Navigate to the React Directory</li> 
    ```cd front-end```
    <li>Install Frontend Dependencies</li>  
    ```npm install```
    <li>Run the Frontend</li> 
    ```npm start```
    <li>Open "http://localhost:3000/" in your browser.</li>
<p>Everything should run smoothly from here. If not, check that all dependencies are installed and updated.</p>

