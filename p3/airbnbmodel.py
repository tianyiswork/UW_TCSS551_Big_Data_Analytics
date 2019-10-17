import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from sklearn import preprocessing

# Read the relations.csv (likes) and profiles.csv (training data) into dataframes
listings = pd.read_csv('listings.csv')
reviews = pd.read_csv('reviews.csv')

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

#Recalculate number_of_reviews from reviews and merge the two datasets
reviews = reviews.groupby('listing_id')['date'].size().reset_index(name='number_of_reviews')
listings = listings.rename(columns={"id": "listing_id"})
comb_listings = pd.merge(listings, reviews, how='inner', on='listing_id')
#print(reviews)
#print(comb_listings)

#Calculate the average number of reviews per month

#create a column called iniital_review_date
comb_listings['iniital_review_date'] = ''
for row in df.iterrows():
	diff_months = 



#create a column called avg_review_per_month
comb_listings['avg_review_per_month'] = ''

print(comb_listings)




