import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arxiu = pd.read_csv('df_covid19_countries.csv', sep=',')

arxiu['date'] = pd.to_datetime(arxiu['date'])

arxiu['month_year'] = arxiu['date'].dt.month.astype(str) + '-' + arxiu['date'].dt.year.astype(str)

arxiu = arxiu.groupby(['location', 'month_year']).sum().reset_index()

arxiu = arxiu[['location', 'month_year', 'total_cases']].sort_values(by=['month_year'])

arxiu = arxiu[arxiu['location'] == 'Afghanistan']
print(arxiu)
plt.figure(num='Afghanistan', figsize=(10, 8))
plt.plot(arxiu['total_cases'], arxiu['month_year'], 'o-r')
plt.xlabel('total_cases')
plt.ylabel('month_year')
plt.title('Afghanistan')
plt.annotate('punt màxim', xy=(arxiu['total_cases'].max(), '12-2022'), xytext=(arxiu['total_cases'].max(), '2-2022'), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
