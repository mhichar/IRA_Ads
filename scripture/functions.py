import numpy as np
import pandas as pd

def matrix_accuracy(X, y):
    '''This is a Function designed to
    find the accuracy of the given values of one matrix
    to another matrix'''
    su=0
    for i in range(X.shape[0]):
        su += ((X[i]==y[i]).sum()/(X.shape[0]*X.shape[1]))
    return su

def matrix_recall(X,y):
    '''Finds the Recall between two matrices'''
    su = 0
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if (X[i,j]==1 & y[i,j]==1):
                su += 1
    print(su)
    su /= y.sum()
    return su

def get_interest_group(interest):
    '''Gets a dataframe of the given interest group'''
    
    #Inputs the original data into dataframe and converts dates to datetime
    ads = pd.read_json('data/russian_ads.json')
    ads['ad_creation_date']=pd.to_datetime(ads['ad_creation_date'])
    ads['ad_end_date']=pd.to_datetime(ads['ad_end_date'])

    #Binarizing the labels
    interest_set = set()
    ads['interests_categories'].values
    for lst in ads['interests_categories']:
        for cat in lst:
            interest_set.add(cat)
    
    #Create dums dataframe
    dums = ads.copy(deep=True)
    for cat in interest_set:
        for row in range(dums.shape[0]):
            if cat in dums.loc[row,'interests_categories']:
                dums.loc[row,cat]=int(1)
            else:
                dums.loc[row,cat]=int(0)
    
    for cat in interest_set:
        dums[cat]=dums[cat].astype(int)

    new_frame=dums[dums[interest]==1][['ad_clicks','ad_copy','ad_creation_date','ad_end_date','ad_id','ad_impressions','ad_spend_usd',\
   'ad_targeting_location','age','age_lower','age_upper','conversion_rate','date_order_index','efficiency_clicks',\
   'efficiency_impressions','interest_expansion','interests_categories','interests_categories_regex','language',\
   'language_categories','location_categories','location_categories_regex','placement_categories','placements']]
    return new_frame

def get_ads_frame():
    '''Gets the whole dataset of the Russian ads'''
        #Inputs the original data into dataframe and converts dates to datetime
    ads = pd.read_json('data/russian_ads.json')
    ads['ad_creation_date']=pd.to_datetime(ads['ad_creation_date'])
    ads['ad_end_date']=pd.to_datetime(ads['ad_end_date'])

    #Binarizing the labels
    interest_set = set()
    ads['interests_categories'].values
    for lst in ads['interests_categories']:
        for cat in lst:
            interest_set.add(cat)
    
    #Create dums dataframe
    dums = ads.copy(deep=True)
    for cat in interest_set:
        for row in range(dums.shape[0]):
            if cat in dums.loc[row,'interests_categories']:
                dums.loc[row,cat]=int(1)
            else:
                dums.loc[row,cat]=int(0)
    
    for cat in interest_set:
        dums[cat]=dums[cat].astype(int)

    new_frame=dums[['ad_clicks','ad_copy','ad_creation_date','ad_end_date','ad_id','ad_impressions','ad_spend_usd',\
    'ad_targeting_location','age','age_lower','age_upper','conversion_rate','date_order_index','efficiency_clicks',\
    'efficiency_impressions','interest_expansion','interests_categories','interests_categories_regex','language',\
    'language_categories','location_categories','location_categories_regex','placement_categories','placements',\
    'Conservative', 'African American', 'Anti-Immigrant', 'Native American',\
    'Gun Rights', 'Progressive', 'Below Age 30', 'Texas', 'Self-Defense',\
    'Prison', 'Police', 'Products', 'Army', 'Geographic', 'Christianity',\
    'Unknown', 'American South', 'LGBTQ', 'Islam', 'Memes and Products',\
    'Patriotism', 'Memes', 'Latinx', 'Above Age 30']]
    return new_frame