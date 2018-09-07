from flask import Flask, request, render_template
import nltk
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
    return render_template('progressive.html')

@app.route('/model_form/', methods=['GET', 'POST'])
def model_form():
    return render_template('register.html')

@app.route('/predict_page/', methods=['GET','POST'])
def prediction_page():
    # load the model
    with open('data/af_bay.pkl', 'rb') as f:
        af_bay = pickle.load(f)
    with open('data/prog_bay.pkl', 'rb') as f:
        prog_bay = pickle.load(f)
    # with open('data/prog_grad.pkl', 'rb') as g:
    #     prog_grad = pickle.load(g)
    with open('data/lat_bay.pkl', 'rb') as f:
        lat_bay = pickle.load(f)
    with open('data/pat_bay.pkl', 'rb') as f:
        pat_bay = pickle.load(f)
    
    # #The original mknn model
    # with open('data/mk_model.pkl', 'rb') as h:
    #     model = pickle.load(h)
    
    #load tf and count vectorizer
    with open('data/tf.pkl', 'rb') as f:
        tf = pickle.load(f)
    with open('data/count.pkl', 'rb') as g:
        count = pickle.load(g)

    #lemmatize
    wordnet = WordNetLemmatizer()
    string = request.form['words']
    
    lemm = [wordnet.lemmatize(string)]
    matrix = tf.transform(lemm)

    #Predict categories based on word count
    af_pred  = af_bay.predict_proba(matrix)[0][1]
    prog_pred = prog_bay.predict_proba(matrix)[0][1]
    lat_pred = lat_bay.predict_proba(matrix)[0][1]
    pat_pred = pat_bay.predict_proba(matrix)[0][1]
    
    return render_template('prediction1.html', text=lemm,\
     matrix=matrix, af_pred=af_pred, prog_pred=prog_pred, \
     lat_pred=lat_pred, pat_pred=pat_pred)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)