import datetime as dt
import yfinance as yf
import pandas as pd

tickers = ['AMZN', 'MSFT', 'META', 'GOOG']
start = dt.datetime.today() - dt.timedelta(3650) # 10 years
end = dt.datetime.today()
cl_price = pd.DataFrame()

for t in tickers:
    cl_price[t] = yf.download(t, start, end)['Adj Close']

cl_price.dropna(axis=0,how='any',inplace=True)
cl_price.mean()
cl_price.std()
cl_price.median()
cl_price.describe()
cl_price.head()
cl_price.tail()