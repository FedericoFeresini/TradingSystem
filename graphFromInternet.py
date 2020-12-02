import pandas_datareader as datareader
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import numpy as np
import peakutils

from scipy.signal import argrelmax
from scipy.signal import argrelmin
 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # #    RETRIEVE DATA    # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# set up pandas_datareader
start_date = '2018-09-01'
end_date = '2018-09-30' # datetime.date.today()
source = 'yahoo'
currency = 'C'

# download historical price
df = datareader.DataReader(currency, source, start_date, end_date)
# df.to_csv('data/liveData.csv') # save data into file
# df = pd.read_csv('data/liveData.csv') # read from file

# convert date format for ohlc
df['Date'] = df.index.map(mdates.date2num)
ohlc = df[['Date','Open','High','Low','Close']]

# correct for starting period errors
# df = df[df.index > '2015-5-31']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # #  CREATE GRAPH   # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# draw candelstick
f1, ax = plt.subplots(figsize = (10,5))

# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m')) # %Y-%m-%d



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # #  INDICATORS    # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# compute the simple moving average
df['ema50'] = df['Close'].ewm(span=50, adjust=False).mean()
df['ema100'] = df['Close'].ewm(span=100, adjust=False).mean()

# plot the moving average lines
ax.plot(df.index, df['ema50'], color = 'blue', label = 'ma50')
ax.plot(df.index, df['ema100'], color = 'purple', label = 'ma100')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # #   PEAKS FINDER    # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# find relative max peaks
cb = np.array(df['High'])
indices = argrelmax(cb)
massimi=[df['High'][j] for j in indices]

# find relative min peaks
cb2 = np.array(df['Low'])
indices2 = argrelmin(cb2)
minimi=[df['Low'][j] for j in indices2]

# draw zigzag line


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # #   SHOW GRAPH    # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# other parameters
ax.grid(False)
ax.legend()
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# show graph
plt.show()
