import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

path1 = input()
games = pd.DataFrame(pd.read_csv(path1, sep=';'))
path2 = input()
rates = pd.DataFrame(pd.read_csv(path2, sep=';'))
games['avg_rate'] = np.zeros(shape=(games.shape[0],))
for i in range(games.shape[0]):
    id = games['id'][i]
    games['avg_rate'][i] = np.mean(rates.loc[rates['id'] == id, 'mark'])
games = games.sort_values(by='avg_rate', ascending=False)
games = games.reset_index().drop(columns=['index'])
for i in range(3):
    print(games['name'][i], '%.3f' % games['avg_rate'][i])
companies = games[games['avg_rate'] > 8].groupby('company')['name'].count().reset_index()
print(companies['company'][0], companies['name'][0])
