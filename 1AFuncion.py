import pandas as pd

covid_df = pd.read_csv('df_covid19_countries.csv/df_covid19_countries.csv')
'''df = pd.read_csv('data.csv')
datos = {'location':['Costa Rica','England','Canada','Germany','Peru','Australia','Russia','Egypt','Brazil','China'],
         'date':[]}
num_countries = covid_df.shape[0]
continents = pd.unique(covid_df.location)
print('There are {} countries in the dataset'.format(num_countries))
print(covid_df.head)
print(covid_df.columns)
print(covid_df.shape)'''
print(covid_df['location'].unique())
print(covid_df['date'].unique().count()
print(covid_df[['location','date','total_cases']])
a =covid_df.groupby(['date']).count()
print(a)