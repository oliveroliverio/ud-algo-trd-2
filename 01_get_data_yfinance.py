import yfinance as yf
import datetime as dt
import pandas as pd

stocks = ['AMZN', 'MSFT', 'INTC', 'GOOG']

# around 1 year
start = dt.datetime.today()-dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame() # empty dataframe to be filled
ohlc = {}

for t in stocks:
    cl_price[t] = yf.download(t, start, end)['Adj Close']

# get all ohlc data

for t in stocks:
    ohlc[t] = yf.download(t, start, end)

# ohlc['MSFT']['Open']