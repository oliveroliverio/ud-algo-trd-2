# Bollinger and ATR are volatile based indicators
import yfinance as yf

tickers = ['AMZN', 'GOOG', 'MSFT']
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

df = ohlcv_data['AMZN']
def ATR(DF, n=14):
    df = DF.copy()
    df['hl_diff'] = abs(df['High']-df['Low'])
    df['h_pclose'] = abs(df['High']-df['Adj Close'].shift(1))
    df['l_pclose'] = abs(df['Low']-df['Adj Close'].shift(1))
    df['TR'] = df[['hl_diff', 'h_pclose', 'l_pclose']].max(axis=1, skipna=False)
    df['ATR'] = df['TR'].ewm(com=n, min_periods=n).mean() # using com param instead of span is closer to yfinance's ATR calculation
    return df['ATR']


for ticker in ohlcv_data:
    ohlcv_data[ticker]['ATR'] = ATR(ohlcv_data[ticker])