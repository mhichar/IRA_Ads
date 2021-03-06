from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

def nlp_pipe(ads):
    '''
    Pipeline that returns the tfidf vectorizer, count vectorizer, 
    tfidf matrix, word count matrix, and sorted word dictionary
    of the count matrix
    '''
    wordnet = WordNetLemmatizer()
    
    #Create corpus for ads in which conversion rate an ad copy have no nans
    # corp=[ads.loc[x,'ad_copy'] for x in range(len(ads))]
    
    conv_ads = ads[~ads['ad_copy'].isna()]
    conv_ads.reset_index(inplace=True)
    conv_corp=[conv_ads.loc[x,'ad_copy'] for x in range(len(conv_ads))]

    lemmed_conv_corp=[]
    for word in range(len(conv_corp)):
        if conv_corp[word]!= None:
            lemmed_conv_corp.append(wordnet.lemmatize(conv_corp[word]))        

    #TFIDF
    tf_conv = TfidfVectorizer(stop_words='english')
    conv_corp_vect=tf_conv.fit_transform(lemmed_conv_corp)

    #Word count vector
    count = CountVectorizer(stop_words='english')
    counted_corp = count.fit_transform(lemmed_conv_corp)
    sum_words = counted_corp.sum(axis=0)
    words_freq = [(word, sum_words[0,idx]) for word, idx in count.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)

    return tf_conv, count, conv_corp_vect, counted_corp, words_freq


def nlp_pipe_conversion(ads):
    '''
    Pipeline that returns the tfidf vectorizer, count vectorizer, 
    tfidf matrix, word count matrix, and sorted word dictionary
    of the count matrix
    '''
    wordnet = WordNetLemmatizer()
    
    #Create corpus for ads in which conversion rate an ad copy have no nans
    # corp=[ads.loc[x,'ad_copy'] for x in range(len(ads))]
    
    conv_ads = ads[(~ads['conversion_rate'].isna()) & (~ads['ad_copy'].isna())]
    conv_ads.reset_index(inplace=True)
    conv_corp=[conv_ads.loc[x,'ad_copy'] for x in range(len(conv_ads))]

    lemmed_conv_corp=[]
    for word in range(len(conv_corp)):
        if conv_corp[word]!= None:
            lemmed_conv_corp.append(wordnet.lemmatize(conv_corp[word]))        

    #TFIDF
    tf_conv = TfidfVectorizer(stop_words='english')
    conv_corp_vect=tf_conv.fit_transform(lemmed_conv_corp)

    #Word count vector
    count = CountVectorizer(stop_words='english')
    counted_corp = count.fit_transform(lemmed_conv_corp)
    sum_words = counted_corp.sum(axis=0)
    words_freq = [(word, sum_words[0,idx]) for word, idx in count.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)

    return tf_conv, count, conv_corp_vect, counted_corp, words_freq

def word_matrix_conversion(vectorizer, X_matrix, y_conversion):
    '''
    Takes a vectorizer, X_matrix of word count or tfidf, and y vector
    for the conversion rate or clicks
    '''
    grad = GradientBoostingRegressor()
    grad.fit(X_matrix, y_conversion)

    #Feature importances
    feats_imports= grad.feature_importances_
    feats_names = np.array(vectorizer.get_feature_names())
    reverse = np.argsort(feats_imports)[::-1]

    n = 10
    top_n = feats_names[reverse][:n]
    return top_n


def word_relation(multinom, tf):
    feature_array = np.array(tf.get_feature_names())
    sorts = np.argsort(multinom.feature_log_prob_[1])[::-1]
    
    n = 10
    top_n = feature_array[sorts][:n]
    values = multinom.feature_log_prob_[1][sorts]
    return top_n, values

def word_importances(vectorizer, regressor):
    '''
    Takes a vectorizer and regressor and returns a top n list of 
    words.  Also returns top n feature importance values.  FOR CONVERSION
    '''
    feats = regressor.feature_importances_
    feature_array = np.array(vectorizer.get_feature_names())
    reverse = np.argsort(feats)[::-1]

    n = 10
    top_n = feature_array[reverse][:n]
    top_n
    return top_n, feats[reverse][:n]

