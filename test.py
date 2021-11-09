import yfinance as yf
 
ticker_list = ['TLSA', 'AAPL']

data = yf.download(
  tickers=ticker_list,
  period = "1mo",
  interval = "1h",
  group_by='ticker',
  threads=True
)
 
for t in ticker_list:
  print(t)
    
  print(data[t]["Open"].date)
 
#for t in (data.loc["TLSA"]):
#  print(t)
