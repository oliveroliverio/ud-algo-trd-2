import yfinance as yf

tickers = ['AMZN', 'GOOG', 'MSFT']
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period='1mo', interval='5m')
    temp.dropna(how='any', inplace=True)
    ohlcv_data[ticker] = temp

def bollband(DF, roll_window=14):
    df = DF.copy()
    df['mid'] = df['Adj Close'].rolling(window=roll_window).mean()
    df['upper'] = df['Adj Close'].rolling(window=roll_window).mean() + (df['Adj Close'].rolling(window=roll_window).std(ddof=0))*2
    df['lower'] = df['Adj Close'].rolling(window=roll_window).mean() - (df['Adj Close'].rolling(window=roll_window).std(ddof=0))*2
    # ddof=0 (degree of freedom), without this you're calculating std of the sample, where the denominator is n-1.  However, we want to calc
    # the std of the population, and the denominator has to be "n".  Having this parameter is closest to charting platforms
    df['band_width'] = df['upper'] - df['lower']
    return df[['mid', 'upper', 'lower', 'band_width']]

# df[['upper', 'lower', 'mid']].plot()
for ticker in ohlcv_data:
    ohlcv_data[ticker][['mid', 'upper', 'lower', 'band_width']] = bollband(ohlcv_data[ticker], 20)