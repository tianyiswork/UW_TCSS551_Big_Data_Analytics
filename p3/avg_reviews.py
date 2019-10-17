import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from sklearn import preprocessing

# Read the relations.csv (likes) and profiles.csv (training data) into dataframes
listings = pd.read_csv('listings.csv', parse_dates=['last_review'])
reviews = pd.read_csv('reviews.csv', parse_dates=['date'])

#Remove unwanted columns
listings.drop(['name','host_id','host_name','latitude','longitude','minimum_nights','neighbourhood_group'
            ,'calculated_host_listings_count','reviews_per_month','number_of_reviews']
            ,inplace=True, axis=1)

#data cleaning 
listings['neighbourhood'] = listings['neighbourhood'].str.strip()
listings['room_type'] = listings['room_type'].str.strip()

#Remove records where price = 0
listings = listings[listings.price != 0]

#Remove records with last_review prior to 2017
listings = listings[listings.last_review >= '2017-01-01']
reviews = reviews[reviews.date >= '2017-01-01']

#make copies of reviews for diff groupby
reviews_2 = reviews.copy()
reviews_3 = reviews.copy()

#find number_of_reviews, initial_review and last_review, and merge them to one table
reviews = reviews.groupby('listing_id')['date'].size().reset_index(name='number_of_reviews')

reviews_2 = reviews_2.sort_values(by=['date']).drop_duplicates(subset='listing_id', keep='first')
reviews_2.rename(columns={'date': 'initial_review'}, inplace=True)
reviews = pd.merge(reviews, reviews_2, how='inner', on='listing_id')

reviews_3 = reviews_3.sort_values(by=['date']).drop_duplicates(subset='listing_id', keep='last')
reviews_3.rename(columns={'date': 'last_review'}, inplace=True)
reviews = pd.merge(reviews, reviews_3, how='inner', on='listing_id')

#fill in a new column called avg_reviews_per_month
reviews = reviews.assign(avg_reviews_per_month=reviews['number_of_reviews']/(12 *
                    (reviews['last_review'].map(lambda x: x.year) -
                     reviews['initial_review'].map(lambda x: x.year)) +
                    (reviews['last_review'].map(lambda x: x.month) -
                     reviews['initial_review'].map(lambda x: x.month))+1))

#we can merge the table if we want
listings = listings.rename(columns={"id": "listing_id"})
listings = pd.merge(listings, reviews, how='inner', on=['listing_id','last_review'])

#print(reviews)
print(listings)
