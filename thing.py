# coding: utf-8
get_ipython().run_line_magic('pwd', '')
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=MQ4RIQTF8CTS5RMM'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=url=MQ4RIQTF8CTS5RMM'
url
import requests
requests.get(url).json()
data = requests.get(url).json()
data = requests.get(url).json()
data
url
url.replace("IBM", "DJT")
data = requests.get(url).json()
dat
data
del data
url = url.replace("IBM", "DJT")
data = requests.get(url).json()
data[0]
data
url = url.replace("DJT", "$SPX")
data = requests.get(url).json()
data
url
del data
data = requests.get(url).json()
data
url = url.replace("$SPX", "^GSPC")
del data
data = requests.get(url).json()
data
url = url.replace("^GSPC", "SPX.SPX.INX")
del data
data = requests.get(url).json()
data
url
url = url.replace("TIME_SERIES_INTRADAY", "TIME_SERIES_DAILY")
url
del data
data = requests.get(url).json()
data
url
url = url.replace("SPX.SPX.INX", "SPY")
data = requests.get(url).json()
data
import readline
readline.write_history_file('./thing')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cat', 'thing')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('rm', 'thing')
get_ipython().run_line_magic('save', 'thing 1-51')
