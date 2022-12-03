import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['AMZN', 'MSFT', 'META', 'GOOG']
start = dt.datetime.today() - dt.timedelta(3650) # 10 years
end = dt.datetime.today()
cl_price = pd.DataFrame()

for t in tickers:
    cl_price[t] = yf.download(t, start, end)['Adj Close']

cl_price.dropna(axis=0,how='any',inplace=True)

daily_rtn = cl_price.pct_change()

fig, ax = plt.subplots()
plt.style.available
plt.style.use('ggplot')
ax.set(title='Mean Daily Return of Stocks', xlabel='Stocks', ylabel='Mean Return')
plt.bar(x=daily_rtn.columns, height=daily_rtn.mean())