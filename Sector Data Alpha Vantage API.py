#!/usr/bin/env python
# coding: utf-8

# In[4]:


#first import the necessary packages
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
import pandas as pd
import numpy as np
from datetime import datetime

# Your API key here
key = 'NEDEYZC5RY09YBFE'
ts = TimeSeries(key)

#run sector performance function to get sector data
sp = SectorPerformances(key=key, output_format='pandas')
data, meta_data = sp.get_sector()
print(data)
print(meta_data)

#create lists for certain stocks in certain industries
#airlines = ['AAL','SAVE','JBLU','LUV','DAL','UA','ALK']
#medical= ['JNJ','PFE','XLV','ALXN','BIIB','BSX','GILD','XRAY','EW','RMD','DVA','ZTS']
#video = ['ZM','NFLX','CSCO']
#retail = ['M','BBY','JWN','DDS','JCP','KSS','SHLDQ']
#fastfood = ['SBUX','MCD','DNKN','BKW','DPZ']
#megastores = ['WMT','TGT','COST','BJ']
#tech = ['AAPL','GOOG','FB','LNKD','MSFT','BABA','AMZN','TSLA']
#postalcarriers = ['DHL','UPS','FDX']


# In[3]:





# In[ ]:





# In[ ]:




