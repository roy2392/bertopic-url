from flask import Flask, render_template, request
from bertopic import BERTopic
from bertopic.cluster import BaseCluster
import time

application = Flask(__name__)

local_model_path = 'bertopic_safetensors'
loaded_topic_model = BERTopic.load(local_model_path)
loaded_topic_model.calculate_probabilities = False
loaded_topic_model.hdbscan_model = BaseCluster()  # Use custom BaseCluster model

topic_info = loaded_topic_model.get_topic_info()
topic_repr_dict = dict(zip(topic_info['Topic'], topic_info['Name']))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        webpage_text = request.form.get('url')
        input = [webpage_text]

        start_time = time.time()
        new_topics, _ = loaded_topic_model.transform(input)
        end_time = time.time()

        print(f"Prediction time: {end_time - start_time} seconds")

        topic_names = [topic_repr_dict.get(x) for x in new_topics]
        print('topics', new_topics, topic_names)

        took = end_time - start_time
        if took < 1:
            took = str(round(took * 1000)) + 'ms'
        else:
            took = str(took) + 's'

        return render_template('results.html', topics=enumerate(topic_names), took=took)

    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True)
