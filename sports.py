import pandas as pd
import numpy as np
from scipy import stats

a=pd.read_csv('dataset_Facebook.csv',sep=';')
print('столбцы в отдельности')
for i in list(a):
    if i!='Type':
        print(i)
        print(np.mean(a[i].dropna()),'cреднее')
        print(np.max(a[i].dropna()),'max')
        print(np.min(a[i].dropna()),'min')
        print(np.median(a[i].dropna()),'mediana')
        print(stats.mode(a[i].dropna()),'modal')
print(np.amax(np.array(a.drop('Type',axis=1).dropna())),'max')
print(np.amin(np.array(a.drop('Type',axis=1).dropna())),'min')
print(np.mean(np.array(a.drop('Type',axis=1).dropna())),'mean')
print(stats.mode(a.Type.dropna()),'Type mode')
print(stats.mode(a.drop('Type',axis=1).dropna(),axis=None),'array mode')






