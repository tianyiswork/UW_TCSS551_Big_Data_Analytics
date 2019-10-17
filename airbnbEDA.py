import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
#QUESTION: What are the price distributions for each of the room-types?
# Read the relations.csv (likes) and profiles.csv (training data) into dataframes
#listings = pd.read_csv('/Users/momo/Desktop/Group Project/listings.csv')
#reviews = pd.read_csv('/Users/momo/Desktop/Group Project/reviews.csv')
listings = pd.read_excel('Seattle_data_4_listings.xls')
#reviews = pd.read_csv('Seattle data 5 - reviews.csv')

#data cleaning
listings['neighbourhood_group'] = listings['neighbourhood_group'].str.strip()
listings['neighbourhood'] = listings['neighbourhood'].str.strip()
listings['room_type'] = listings['room_type'].str.strip()

#PRIVATE ROOM
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
#SHARED ROOM
listings_copy = listings.groupby('room_type').apply(lambda x: x.sort_values('price'))
listings_sr = listings_copy[(listings_copy['room_type']=='Shared room')]
listings_sr_price = listings_sr.loc[:,'price']
#print(listings_sr_price)
listings_sr_distribution = listings_sr_price.groupby(pd.cut(listings_sr["price"], np.arange(0, 1200, 50))).size().reset_index(name='count')
print(listings_sr_distribution)

highest_price = listings_sr_price.tail(1)
lowest_price = listings_sr_price.head(1)
print('highest price:')
print(highest_price)
print('lowest price:')
print(lowest_price)

nbins = int(round((highest_price)/50, 0))
n, bins, patches = plt.hist(x=listings_sr_price, bins=10, color='#0504aa', alpha=0.7, rwidth= 0.95)
plt.grid(axis='y', alpha=0.7)
plt.xlabel('Price per Night')
plt.ylabel('Number of Accomodations')
plt.title('Price Distribution: Shared Room')
#plt.text(5, 5, r'$\mu=15, b=3$', bbox=dict(facecolor='red', alpha=0.5))
maxfreq = n.max()
plt.grid(True)
# Set a clean upper y-axis limit.
plt.xlim(0, 1200)
plt.xticks(np.arange(0, 1200, step=100))
plt.ylim(ymin=0, ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()


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