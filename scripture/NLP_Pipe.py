from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def nlp_pipe(ads):
    '''
    Pipeline that returns the tfidf vectorizer, count vectorizer, 
    tfidf matrix, word count matrix, and sorted word dictionary
    of the count matrix
    '''
    wordnet = WordNetLemmatizer()
    
    #Create corpus for ads in which conversion rate an ad copy have no nans
    # corp=[ads.loc[x,'ad_copy'] for x in range(len(ads))]
    
    conv_ads = ads[~ads['conversion_rate'].isna() & ~ads['ad_copy'].isna()]
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