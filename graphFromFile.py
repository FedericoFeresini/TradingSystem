import pandas_datareader as datareader
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # #    RETRIEVE DATA    # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# set up pandas_datareader
# start_date = '2017-01-01'
# end_date = '2018-09-10' # datetime.date.today()
# source = 'yahoo'
# currency = 'C'

# download historical price
# df = datareader.DataReader(currency, source, start_date, end_date)
# df.to_csv('data/liveData.csv') # save data into file
df = pd.read_csv('data/EURUSD_Candlestick_1_Hour_BID_18.09.2015-15.09.2018.csv', parse_dates=True) # read from file
aa = pd.DatetimeIndex(data=df['Gmt time'])
df.drop(columns=['Gmt time'], inplace=True)
df['Gmt time']=aa
df.set_index('Gmt time', inplace=True)

# convert date format for ohlc
df['Gmt time'] = df.index.map(mdates.date2num)
print(df['Gmt time'])
df_considerato = df[26000:26017]
ohlc = df_considerato[['Gmt time','Open','High','Low','Close']]
print(df_considerato)
datetime.replace(year=self.year, month=self.month, day=self.day)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # #   DRAW GRAPH    # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print(ohlc)
# draw candelstick
f1, ax = plt.subplots()
print(type(ax))
# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=0.06, colorup='green', colordown='red')

ax.xaxis.set_major_formatter(mdates.DateFormatter('(%y-%m-%d T %H:%M:%S)'))

plt.show()
