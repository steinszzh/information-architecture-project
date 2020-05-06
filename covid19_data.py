import panda as pd

# this is an auto updated data 
# this data is US confirmed case
# from Johns Hopkins University (https://github.com/CSSEGISandData/COVID-19)
data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
data
