import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.beautifulSoup(resp.text)

def convert_wiki_table_to_df():


resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text)
table = soup.find('table', {'class':'wikitable sortable'})
tickers = []
for row in table.findAll('tr')[1:]: # skip header row (row 1 onward)
    ticker = row.findAll('a', {'class', 'external text'})[0].text # find all a tags with 'external text' class, get first column only, and get the text
    tickers.append(ticker)