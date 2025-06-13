from flask import Flask, render_template, request
from livereload import Server

import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

app = Flask(__name__)

# Load and train model on startup
df = pd.read_csv('news.csv')
labels = df['label']
texts = df['text']

# Stratified split
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in sss.split(texts, labels):
    x_train, x_test = texts.iloc[train_index], texts.iloc[test_index]
    y_train, y_test = labels.iloc[train_index], labels.iloc[test_index]

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = vectorizer.fit_transform(x_train)
tfidf_test = vectorizer.transform(x_test)

# Train model
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)

# Evaluate
y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)



@app.route('/home/<name>')
def hello_world(name):
    return 'Hello %s!' % name

@app.route('/')
def home():
    # Recalculate accuracy to ensure it's fresh
    y_pred = pac.predict(tfidf_test)
    current_score = accuracy_score(y_test, y_pred)
    print(f"Current accuracy score: {current_score}")  # Debug print
    accuracy_percentage = round(current_score * 100, 2)
    print(f"Accuracy percentage: {accuracy_percentage}")  # Debug print
    return render_template('home.html', accuracy=accuracy_percentage)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input text from the form

    title_input = request.form.get('description_news', '')
    description_input = request.form.get('description_news', '')

    # if not title_input or not description_input:
    #     return "No input provided"

    user_input = title_input + " " + description_input
    input_vector = vectorizer.transform([user_input])
    
    prediction = pac.predict(input_vector)[0]

    return render_template('prediction.html', prediction=prediction)


if __name__ == '__main__':
    app.run