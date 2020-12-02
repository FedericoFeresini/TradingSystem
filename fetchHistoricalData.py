# pre requisites
## install python 3.7 or >, pip (pip3 mac), ipython, pandas, pandas_datareader, matplotlib, numpy, jupyter

# # # download update data set
import pandas_datareader.data as web
from datetime import datetime

start = datetime(2015, 1, 1)
end = datetime(2018, 8, 31)

#collect data
f = web.DataReader('F', 'yahoo', start, end)

# save data into a file
f.to_csv('historicalDataSample.csv')
