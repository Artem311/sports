import pandas as pd
import numpy as np

def temp(a):
    y=[]
    for i in range(len(a)-1):
        y.append((a[i+1]-a[i])/a[i])
    return (np.average(y))



a=pd.read_csv('b_cl.csv')
b=pd.read_csv('i_cl.csv')
c=pd.read_csv('m_cl.csv')
bank=a[a['tag_active']==1].copy()
m=c[c['id'].isin(bank['id'])].copy()
m=c[c['number_of_entrances']>=1].copy()
m['count']=1
table=pd.pivot_table(m,values=['count','number_of_entrances'],index='month',aggfunc=np.sum)
i=b[b['number_of_entrances']>=1].copy()
i['count']=1
table1=pd.pivot_table(i,values=['count','number_of_entrances'],index='month',aggfunc=np.sum)
print('мобильные клиенты')
print(table)
print('интернет клиенты')
print(table1)
print('рост приложения' , temp(np.array(table['count']))*100)
#print(table['number_of_entrances']/table['count'])
print('рост интерент банка' ,temp(np.array(table1['count']))*100)
#print(table1['number_of_entrances']/table1['count'])
bank1=a[a['tag_new']==1].copy()
m1=c[c['id'].isin(bank1['id'])].copy()
m1=m1.groupby('id').first().reset_index()
print('мобильное приложение')
print(np.average(((pd.to_datetime(pd.merge(m1,bank1,how='inner',on='id')['month_x'])-pd.to_datetime(pd.merge(m1,bank1,how='inner',on='id')['month_y']))/np.timedelta64(1, 'D')).astype(int)))
i1=b[b['id'].isin(bank1['id'])].copy()
i1=i1.groupby('id').first().reset_index()
print('интеренет версия')
print(np.average(((pd.to_datetime(pd.merge(i1,bank1,how='inner',on='id')['month_x'])-pd.to_datetime(pd.merge(i1,bank1,how='inner',on='id')['month_y']))/np.timedelta64(1, 'D')).astype(int)))





