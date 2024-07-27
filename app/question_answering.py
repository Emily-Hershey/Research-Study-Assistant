

import openai
from openai import OpenAI
import os
from models import Database

def run_model_on_data(question):
    #update file
    file_path = 'info.txt'
    database = Database.query.all()  # Gives us a list of all the rows in the Database database as Python objects
    information_to_add = ''
    for row in database:
        if row.topic == "user-input":
            information_to_add += row.text + "\n"
    with open(file_path, 'w') as file:
        file.write(information_to_add)

    my_api_key = os.getenv('OPENAI_API_KEY')
    print(my_api_key)
    client = OpenAI(api_key='key')

    assistant = client.beta.assistants.create(
        name="Study Assistant",
        instructions="Use the given context to answer questions. The given data should be where your answers are rooted, but can be supplemented by your own database.",
        model="gpt-4o-mini",
        tools=[{"type": "file_search"}],
    )

    # Create a vector store caled "Study Assistant"
    vector_store = client.beta.vector_stores.create(name="Study Assistant")

    # Ready the files for upload to OpenAI
    file_paths = ['info.txt']
    file_streams = [open(path, "rb") for path in file_paths]
    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )

    assistant = client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

    # Create a thread and attach the file to the message

    # Upload the user provided file to OpenAI

    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": question,

            }
        ]
    )


    # Use the create and poll SDK helper to create a run and poll the status of
    # the run until it's in a terminal state.
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=assistant.id
    )
    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))
    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    #print(message_content.value)
    print("\n".join(citations))
    return message_content.value
