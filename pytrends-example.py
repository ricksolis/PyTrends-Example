import pytrends
from pytrends.request import TrendReq 
import pandas as pd
import time
import datetime
from datetime import datetime, date, time

#startTime = datetime.time() 
pytrend = TrendReq(hl='en-US', tz=360, retries=10, backoff_factor=0.5)
colnames = ['keywords'] 
df = pd.read_csv('keywords/keyword_list.csv', names=colnames) 
df2 = df['keywords'].values.tolist() 
df2.remove('Keywords') 
dataset = [] 
keywords = []
for x in range(0,len(df2)): 
    keywords.append(df2[x])
    #print(df2[x])

#print(keywords)
pytrend.build_payload(kw_list=keywords, cat=0, timeframe='2019-01-01 2020-05-01', geo='US') 

data = pytrend.interest_over_time() 
if not data.empty: 
    data = data.drop(labels=['isPartial'],axis='columns') 
    dataset.append(data)
    result = pd.concat(dataset, axis=1) 
    result.to_csv('search_trends.csv') 
    #executionTime = (time.time() - startTime) 
    print('Execution time in sec.: ')#+ str(executionTime))

 

     