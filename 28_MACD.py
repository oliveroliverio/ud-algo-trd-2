import yfinance as yf
import matplotlib.pyplot as plt
# from matplotlib.finance import candlestick_ohlc
import mplfinance as mpf

tickers = ['AMZN', 'MSFT', 'META', 'GOOG']
ohlcv_data = {}

# loop over tickers and store ohlcv dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='15m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

df = ohlcv_data['AMZN']
def MACD(DF, a=12,b=26,c=9):
    df = DF.copy()
    df['ma_fast'] = df['Adj Close'].ewm(span=a, min_periods=a).mean()
    df['ma_slow'] = df['Adj Close'].ewm(span=b, min_periods=b).mean()
    df['macd'] = df['ma_fast']-df['ma_slow']
    df['signal'] = df['macd'].ewm(span=c, min_periods=c).mean()
    return df.loc[:,['macd','signal']] # return all the rows, but only the 'macd' and 'signal' columns

# apply MACD function to all ticker DFs in the ohlcv_data dictionary
for ticker in ohlcv_data:
    ohlcv_data[ticker][['MACD','SIGNAL']] = MACD(ohlcv_data[ticker])# get the DF in the ohlcv_data dictionary, and add the 'macd' and 'signal' columns

plt.style.use('ggplot')
mpf.plot(ohlcv_data['AMZN'], type='candle', volume=True)

asdf =  ohlcv_data['AMZN']
# asdf.iloc[:,
# fig, ax = plt.subplots()
# plt.style.available
# plt.style.use('ggplot')
# ax.set(title='Mean Daily Return of Stocks', xlabel='Stocks', ylabel='Mean Return')