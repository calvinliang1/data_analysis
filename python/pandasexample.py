import numpy as np
import webbrowser
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import datetime
obj = Series([2,3,4,5])
covid19_confirmed_ca = Series([17298,32623,5863,2224,985],index=['ON','QB','AB','BC','NS'])
#print('NS' in covid19_confirmed_ca)
covid19_confirmed_ca_dict = covid19_confirmed_ca.to_dict()
#can convert dict to series as they match like array to list
#print(covid19_confirmed_ca_dict)
prov = ['ON','AB','MB','QB','NS']
covid19_confirmed_ca_obj = Series(covid19_confirmed_ca,index = prov)
#print(pd.notnull(covid19_confirmed_ca_obj))
#print(covid19_confirmed_ca+covid19_confirmed_ca_obj)
#if adding empty values we will yield an empty
website = 'https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html'
frame = pd.read_clipboard()
#describe .columns
frame2 = DataFrame(frame,columns=['Number of confirmed cases','Number of Deaths'])
frame3 = DataFrame(frame,columns=['Number of Deaths','Col_new'])
#head: first what ever | tail: last what ever
#.iloc index location .loc by index
print(frame.tail(4))
ser = Series(randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
df_ser = DataFrame(ser)
#frame['Datetime'] = '2020-05-09'
latest_update = Series(['Updating','Done'],index=[0,6])
frame['update'] = latest_update
del frame['update']
data = {'City':['Toronto','Mississauga'],'Population':[10000,20000]}
print(data)
prices = wb.get_data_yahoo(['CTC-A.TO'],start = datetime.datetime(2020,5,4),end = datetime.datetime(2020,5,8))['Adj Close']
prices.plot()
plt.show()