import yfinance as yf
import numpy as np
import plotly.graph_objects as go

tickers = ['AMZN', 'GOOG', 'MSFT']
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='7mo', interval='1d')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

def CAGR(DF):
    df = DF.copy()
    df['return'] = df['Adj Close'].pct_change()
    df['cum_rtn'] = (1+df['return']).cumprod()
    # n = number of years of which you're performing CAGR analysis, but since you only have 7mo worth of data, this will be a decimal
    # to calculate do this:
    n = len(df)/252 # number of days in your data set divided by number of trading days in a year.
    # note, if you're working with intraday data (hours, minutes, etc), you have to further divide (usually by 8)
    CAGR = (df['cum_rtn'][-1])**(1/n) - 1 # get last value of the series and raise to 1/n, minus 1
    # if your CAGR is negative, then you lost money.
    return CAGR

# calculate CAGR for each of the tickers
for ticker in ohlcv_data:
    print(f"CAGR for {ticker} = {CAGR(ohlcv_data[ticker])}")