# BERTopic-URL

This repository contains a project leveraging BERTopic, a topic modeling technique, for analyzing and extracting topics from a collection of URLs. The goal is to automate the process of identifying and summarizing the main themes present in the content of various web pages.

## Features

- **URL Collection**: Scrape and collect content from a list of URLs.
- **Text Preprocessing**: Clean and preprocess the scraped text for analysis.
- **Topic Modeling**: Apply BERTopic to extract meaningful topics from the text data.
- **Visualization**: Generate visualizations to present the extracted topics.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/roy2392/bertopic-url.git
   cd bertopic-url
   ```

	2.	Install the required dependencies:
      ```bash
      pip install -r requirements.txt
      ```

   3. Prepare the URL List:
      Create a text file urls.txt with each line containing a URL to be analyzed.
      ```bash
      python bertopic_url.py
       ```


   ## Directory Structure
             bertopic-url/
      │
      ├── data/
      │   └── urls.txt            # Input file containing URLs
      │
      ├── output/
      │   └── topics.html         # Generated HTML file with topic visualizations
      │
      ├── bertopic_url.py         # Main script for running the topic modeling pipeline
      ├── requirements.txt        # List of dependencies
      └── README.md               # Project documentation
