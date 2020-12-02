import pandas_datareader as datareader
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import numpy as np

import pandas as pd
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # #         ZigZag 1.0        # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def zigZag(data, numOfCandles_forward, aMax, aMin):
    print ("Creating ZigZag . . .")
    #1 step: find starting candle
    locationIdx=0
    #print("==Start==")
    #print("==Step1==")
    while len(aMax) == 0 and len(aMin)==0 :
        if df.iloc[locationIdx]['High'] <= df.iloc[locationIdx+1]['High'] and df.iloc[locationIdx]['Low'] >= df.iloc[locationIdx+1]['Low'] :
            locationIdx+=1
        if df.iloc[locationIdx]['High'] < df.iloc[locationIdx+1]['High'] and df.iloc[locationIdx]['Low'] < df.iloc[locationIdx+1]['Low'] :
            aMin.append(locationIdx)
            maxOrMin = "max"
            locationIdx+=1
        if df.iloc[locationIdx]['High'] > df.iloc[locationIdx+1]['High'] and df.iloc[locationIdx]['Low'] > df.iloc[locationIdx+1]['Low'] :
            aMax.append(locationIdx)
            maxOrMin = "min"
            locationIdx+=1
    secondPoint = maxOrMin

    #2 step: check if max or min
    #print("==Step2==")

    while locationIdx <= df['High'].count()-4:
        #print("Candle = "+ str(locationIdx))
        for iNext in range(1,numOfCandles_forward+1):
            if maxOrMin == "max":
                if df.iloc[locationIdx]['High'] <= df.iloc[locationIdx+iNext]['High'] :
                    locationIdx+=1
                    break
                if df.iloc[locationIdx]['High'] > df.iloc[locationIdx+iNext]['High'] :
                    if iNext == numOfCandles_forward :
                        aMax.append(locationIdx)
                        #print("MAX:")
                        #print(df.iloc[locationIdx])
                        locationIdx+=1
                        maxOrMin = "min"
                        break

            if maxOrMin == "min" :
                if df.iloc[locationIdx]['Low'] >= df.iloc[locationIdx+iNext]['Low'] :
                    locationIdx+=1
                    break
                if df.iloc[locationIdx]['Low'] < df.iloc[locationIdx+iNext]['Low'] :
                    if iNext == numOfCandles_forward :
                        aMin.append(locationIdx)
                        #print("MIN:")
                        #print(df.iloc[locationIdx])
                        locationIdx+=1
                        maxOrMin = "max"
                        break

    return

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # #    RETRIEVE DATA    # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# set up pandas_datareader
start_date = '2018-01-01'
end_date = '2018-09-30' # datetime.date.today()
source = 'yahoo'
currency = 'C'

# download historical price
print("Downloading data from internet. From: " + str(start_date) + " to: " + str(end_date) )
df = datareader.DataReader(currency, source, start_date, end_date)

# df.to_csv('data/liveData.csv') # save data into file
# df = pd.read_csv('data/liveData.csv') # read from file

# convert date format for ohlc
df['Date'] = df.index.map(mdates.date2num)
ohlc = df[['Date','Open','High','Low','Close']]

# correct for starting period
# df = df[df.index > '2015-5-31']

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # #  CREATE GRAPH   # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# draw candelstick
f1, ax = plt.subplots(figsize = (10,5))

# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m')) # %Y-%m-%d


# 5 point strategy [ y= mx + q ...m = y/x]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # #  INDICATORS    # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# compute the simple moving average
# df['ema50'] = df['Close'].ewm(span=50, adjust=False).mean()
# df['ema100'] = df['Close'].ewm(span=100, adjust=False).mean()

# plot the moving average lines
# ax.plot(df.index, df['ema50'], color = 'blue', label = 'ma50')
# ax.plot(df.index, df['ema100'], color = 'purple', label = 'ma100')

#ZigZag indicator

# calculate max and min
aMax= []
aMin= []
zigZag(df, 3, aMax, aMin)

# create zig zag line
zigZagMax = pd.DataFrame()
zigZagMin = pd.DataFrame()
zigZagMax['Point'] = df['High'][aMax]
zigZagMin['Point'] = df['Low'][aMin]
zigZagPoints = [zigZagMax, zigZagMin]
zigZagLine = pd.concat(zigZagPoints)
zigZagLine.sort_index(inplace=True)
ax.plot(zigZagLine['Point'].index, zigZagLine['Point'], color = 'blue', label = 'ZigZag')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # #   SHOW GRAPH    # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# graph parameters
ax.grid(False)
ax.legend()

# show graph
plt.show()
