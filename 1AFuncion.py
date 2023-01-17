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
'''
df_covid19_countries.csv/df_covid19_countries.csv
print(covid_df['date'].unique().count()
print(covid_df[['location','date','total_cases']])
a =covid_df.groupby(['date']).count()
print(a)'''
'''
print(covid_df.head(3))
print(covid_df.tail(3))
print(covid_df['total_cases'].unique())
Muestra los paises en formato lista
print(covid_df['location'].unique().tolist())
'''

'''print(covid_df.loc[covid_df['total_cases'] > 000.0])'''
print(covid_df.tail(3))
print(covid_df.head(3))
list_dates = covid_df['date'].unique()
print(list_dates)

lista[]
#total = covid_df.groupby('location')
#print(total)
#list_location = covid_df['location'].unique().tolist()

#print(list_location)
#for list_location in range(11):
 #   print(list_location)

