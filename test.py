import yfinance as yf
 
ticker_list = ['TSLA', 'AAPL']
 

data = yf.download(
  tickers=ticker_list,
  period = "1mo",
  interval = "1h",
  group_by='ticker',
  threads=True
)
 
for t in ticker_list:
  print(t)

  firstDataValue = data[t]["Open"][1]
  secondDataValue = data[t]["Open"][10]

  print("The price change from index 10 to 1 of " + t + " is " + str(firstDataValue) + " - " + str(secondDataValue) + " = " + str(firstDataValue - secondDataValue))

  #for index, row in data[t]["Open"].iteritems():
    #print(index, row)
 
#for t in (data.loc["TLSA"]):
#  print(t)
