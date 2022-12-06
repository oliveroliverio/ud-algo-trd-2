import yfinance as yf
import numpy as np
import plotly.graph_objects as go

tickers = ['AMZN', 'GOOG', 'MSFT']
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1d', interval='5m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

def rsi(DF, roll_window=14):
    df = DF.copy()
    df['change'] = df['Adj Close'] - df['Adj Close'].shift(1)
    df['gain'] = np.where(df['change']>=0, df['change'],0 )  # use numpys where fxn
    df['loss'] = np.where(df['change']<0, -1*df['change'],0 )  # use numpys where fxn
    # note for RMA fxn, pandas gives us alpha parameter we can use to mimic this
    df['avg_gain'] = df['gain'].ewm(alpha=1/roll_window, min_periods=roll_window).mean()
    df['avg_loss'] = df['loss'].ewm(alpha=1/roll_window, min_periods=roll_window).mean()
    df['rs'] = df['avg_gain']/df['avg_loss']
    df['rsi'] = 100 - (100 / (1 + df['rs']))
    return df['rsi']

for ticker in ohlcv_data:
    ohlcv_data[ticker]['RSI'] = rsi(ohlcv_data[ticker])

df = ohlcv_data['AMZN']
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Adj Close']
                                     )])

fig.show()

#a