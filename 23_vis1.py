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

cl_price.plot(subplots=True, layout=(2,2), title="Stock Price Evolution")

daily_rtn.plot(subplots=True, layout=(2,2), title="Daily Rtn")

(1 + daily_rtn).cumprod().plot()

# these plots tell you, if you invested $1 in these stocks in 2012, you would have this much today.  (y axis in dollar amounts)
