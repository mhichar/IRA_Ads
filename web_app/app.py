from flask import Flask, request, render_template
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
import pickle
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('landing.html', methods = ['GET', 'POST'])


@app.route('/AFAM/', methods = ['GET'])
def AFAM():
    return render_template('African_American.html')

@app.route('/Progressive/', methods = ['GET'])
def progressive():
    return render_template('')

@app.route('/model_form/', methods=['GET', 'POST'])
def model_form():
    return render_template('register.html')

@app.route('/predict_page/', methods=['GET','POST'])
def prediction_page():
    # load the model
    with open('data/mk_model.pkl', 'rb') as f:
        model = pickle.load(f)





    
    #lemmatize
    wordnet = WordNetLemmatizer()
    text = request.form['words']

    lemmed_corp=[]
    for word in range(len(text)):
        if text[word]!= None:
            lemmed_corp.append(wordnet.lemmatize(text[word]))

    with open('data/count.pkl', 'rb') as g:
        count = pickle.load(g)
    matrix = count.transform(lemmed_corp)

    #Predict categories based on word count
    preds  = model.predict(matrix)

    
    return render_template('predict0.html')

    






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)