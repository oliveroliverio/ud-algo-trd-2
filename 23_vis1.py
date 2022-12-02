import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib

tickers = ['AMZN', 'MSFT', 'META', 'GOOG']
start = dt.datetime.today() - dt.timedelta(3650) # 10 years
end = dt.datetime.today()
cl_price = pd.DataFrame()

for t in tickers:
    cl_price[t] = yf.download(t, start, end)['Adj Close']

cl_price.dropna(axis=0,how='any',inplace=True)

# important stuff
daily_rtn = cl_price.pct_change() # new DF showing pct chnge instead of raw price values

cl_price.plot()