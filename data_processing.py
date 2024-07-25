import pandas as pd 
import matplotlib.pyplot as plt

cols = ['Longitude', 'Latitude', 'PrimSource', 'Plant_Name', 'City', 'State']
df = pd.read_csv('Power_Plants.csv', usecols=cols)
clean_sources = ['hydroelectric', 'solar', 'nuclear', 'geothermal', 'wind', 'biomass'] # Row values to construct our clean dataframe 
clean_df = df[df['PrimSource'].isin(clean_sources)]
clean_df['Longitude'] = clean_df['Longitude'] / 1.7 # Accounts for the curvature of the Earth 

source_colors = {'hydroelectric': 'blue', 'solar': 'yellow', 'nuclear': 'black', 'geothermal': 'red', 'wind': 'white', 'biomass': 'green'}

clean_df['Color'] = clean_df['PrimSource'].map(source_colors)

for primsource, group in clean_df.groupby('PrimSource'):
    plt.scatter(group['Longitude'], group['Latitude'], color=group['Color'], label=primsource, s=3.5)
    
plt.rcParams['figure.figsize'] = (8, 8)# Sets the default ratio of the plot 
plt.style.use('seaborn')
# plt.scatter(clean_df['Longitude'], clean_df['Latitude'], s=.5)
plt.xlabel('longitude')
plt.ylabel('latitude')
clean_df
