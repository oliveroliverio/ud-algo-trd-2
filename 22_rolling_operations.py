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

# important stuff
daily_rtn = cl_price.pct_change() # new DF showing pct chnge instead of raw price values
daily_rtn.mean(axis=1)
daily_rtn.std()

df_s = daily_rtn.rolling(window=10).mean() # apply mean operation to a rolling window of 10 days (this is SMA, simple moving avg)
daily_rtn.rolling(window=10).std() # apply std operation to a rolling window of 10 days
daily_rtn.rolling(window=10).max() # apply max operation to a rolling window of 10 days

# EMA (exponential moving avg, apply more recent price with more weight).
df_e = daily_rtn.ewm(com=10,min_periods=10).mean()