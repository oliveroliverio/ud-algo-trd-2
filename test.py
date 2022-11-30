import yfinance as yf
import datetime as dt
import pandas as pd

# asdf = dt.datetime.today(

stocks = ['AMZN', 'MSFT', 'INTC', 'GOOG']

# around 1 year
start = dt.datetime.today()-dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame() # empty dataframe to be filled