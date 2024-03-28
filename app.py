from flask import Flask, render_template, request
from bertopic import BERTopic
import pandas as pd
import concurrent.futures
import time
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')

        # define the local path of the pickle file
        local_model_path = '/Users/royzalta/Downloads/Bertopic POC v1.pkl'
        # load the pickle file as loaded_topic_model
        loaded_topic_model = BERTopic.load(local_model_path)

        # Fetch the content of the webpage
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text from the webpage
        webpage_text = soup.get_text()

        # Create a new DataFrame with the random keywords
        new_df = pd.DataFrame({'keyword': [webpage_text]})

        # Transform the new unique keywords to get their corresponding topics
        # Create a ThreadPoolExecutor
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Schedule the transform method to be executed and get a Future object
            future = executor.submit(loaded_topic_model.transform, new_df['keyword'].tolist())

            # Wait for the transform method to complete and get the result
            new_topics, _ = future.result()
        end_time = time.time()
        print(f"Old predict_proba execution time: {end_time - start_time} seconds")

        # Create a dictionary to map new keywords to their corresponding topics
        new_keyword_topic_dict = dict(zip(new_df['keyword'], new_topics))

        # Get the topic information from the loaded topic_model
        topic_info = loaded_topic_model.get_topic_info()

        # Create a dictionary to map topic indices to their representations
        topic_repr_dict = dict(zip(topic_info['Topic'], topic_info['Name']))

        # Assign the topic representations to the new DataFrame
        new_df['topic'] = new_df['keyword'].map(new_keyword_topic_dict).map(topic_repr_dict)

        # Get the frequency of each topic
        topic_freq = loaded_topic_model.get_topic_freq()

        # Sort the topics by frequency in descending order and take the top 5
        top_5_topics = new_df['topic'].value_counts().head(5)

        return render_template('results.html', topics=top_5_topics.to_dict())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)