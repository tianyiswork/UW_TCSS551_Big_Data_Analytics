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
listings = pd.merge(listings, reviews, how='inner', on='listing_id')
print(reviews)
print(listings)

#Recalculate reviews_per_month???maybe


'''neighborhoods = listings.neighbourhood.unique()
print(neighborhoods)
le = preprocessing.LabelEncoder()
le.fit((listings['neighbourhood']))
LabelEncoder()
list(le.classes_)'''
#


'''listings_copy = listings.groupby('room_type').apply(lambda x: x.sort_values('price'))
listings_pr = listings_copy[(listings_copy['room_type']=='Private room')]
listings_pr_price = listings_pr.loc[:,'price']
#listings_pr_price = listings_pr_price[listings_pr_price > 1]
#print(listings_pr_price)
listings_pr_distribution = listings_pr_price.groupby(pd.cut(listings_pr["price"], np.arange(0, 1001, 50))).size().reset_index(name='count')
#x_pr = listings_pr_distribution.loc[:,0]
print(listings_pr_distribution)

highest_price = listings_pr_price.tail(1)

nbins = int(round(highest_price/50, 0))
n, bins, patches = plt.hist(x=listings_pr_price, bins=25, color='#0504aa', alpha=0.7, rwidth= 0.95)
plt.grid(axis='y', alpha=0.7)
plt.xlabel('Price per Night')
plt.ylabel('Number of Accomodations')
plt.title('Price Distribution: Private Room')
#plt.text(5, 5, r'$\mu=15, b=3$', bbox=dict(facecolor='red', alpha=0.5))
maxfreq = n.max()
plt.grid(True)
# Set a clean upper y-axis limit.
plt.xlim(0, 1000)
plt.xticks(np.arange(0, 1001, step=100))
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()'''

#====================================================================================================================================

#=======================================================================================================================
#ENTIRE HOME
'''listings_copy = listings.groupby('room_type').apply(lambda x: x.sort_values('price'))
listings_eh = listings_copy[(listings_copy['room_type']=='Entire home/apt')]
listings_eh_price = listings_eh.loc[:,'price']
#print(listings_sr_price)
listings_eh_distribution = listings_eh_price.groupby(pd.cut(listings_eh["price"], np.arange(0, 1200, 50))).size().reset_index(name='count')
print(listings_eh_distribution)

highest_price = listings_eh_price.tail(1)
print('highest price:')
print(highest_price)
#nbins = int(round(highest_price/50, 0))
n, bins, patches = plt.hist(x=listings_eh_price, bins=54, color='#0504aa', alpha=0.7, rwidth= 0.95)
plt.grid(axis='y', alpha=0.7)
plt.xlabel('Price per Night')
plt.ylabel('Number of Accomodations')
plt.title('Price Distribution: Entire home/apt')
#plt.text(5, 5, r'$\mu=15, b=3$', bbox=dict(facecolor='red', alpha=0.5))
maxfreq = n.max()
plt.grid(True)
# Set a clean upper y-axis limit.
plt.xlim(0, 1200)
plt.xticks(np.arange(0, 1200, step=100))
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()'''