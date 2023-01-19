import pandas as pd
import numpy as np

arxiu = pd.read_csv('df_covid19_countries.csv', sep=',')

arxiu['date'] = pd.to_datetime(arxiu['date'])

arxiu['month_year'] = arxiu['date'].dt.month.astype(str) + '-' + arxiu['date'].dt.year.astype(str)
arxiu = arxiu.groupby(['location', 'month_year']).sum().reset_index()

arxiu = arxiu[['location', 'month_year', 'total_cases']].sort_values(by=['month_year'])

arxiu = arxiu[arxiu['location'] == 'Afghanistan']
print(arxiu)