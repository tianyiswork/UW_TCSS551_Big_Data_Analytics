import seaborn as sns
import numpy as np
import pylab as plt
import pandas as pd
#import matplotlib.pyplot as plt

#matplotlib.style.use('ggplot')


listings = pd.read_excel('Seattle_data_4_listings.xls')

plt.title('Prices for Entire Home/Apt')
plt.xlabel('Neighbourhoods in Seattle')
plt.ylabel('Average Rental Prices')

l = listings.loc[listings['room_type'] == 'Entire home/apt']
result = l.groupby('neighbourhood_group')['price'].mean()
result.plot(x='neighbourhood_group', y='price', kind='bar')

print(l.shape)
plt.show()


#Entire home/apt
#Private room
#Shared room