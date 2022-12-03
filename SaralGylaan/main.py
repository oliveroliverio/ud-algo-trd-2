# https://saralgyaan.com/posts/python-candlestick-chart-matplotlib-tutorial-chapter-11/

import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates

plt.style.use('ggplot')
df = pd.read_csv('/Users/oliveroliverio/_Projects/F-Trd_Projects/ud-algo-trd-2/SaralGylaan/NIFTY 50_Data.csv')
ohlc = df.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
