import pandas as pd

covid_df = pd.read_csv('df_covid19_countries.csv/df_covid19_countries.csv')
#print('Muestra datos',covid_df)
#print('Mostar los paises')
paises = pd.unique(covid_df.location)
#print(paises)
ten = pd.DataFrame(paises).head(10)
#print('diez primeros paises',ten)
max_casos = covid_df['total_cases']
#print(max_casos)

#Pillar los mese del año 2021
fech = pd.date_range('2021-01-01',periods=12,freq='M')
#covid_df = pd.Series(np.arange(12), index= 'total')
#covid_df = pd.date_range(start='2021-01-01', end='2021-01-31',freq='D')
print(fech)
#print(covid_df[['location','date','total_cases']])


#Intentar asociar meses con casos totales

