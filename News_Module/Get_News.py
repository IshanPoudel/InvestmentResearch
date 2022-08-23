







stocks = ['GOOG', 'AAPL', 'FB', 'BABA', 'AMZN', 'GE', 'AMD', 'WMT', 'BAC', 'GM',
'T', 'UAA', 'SHLD', 'XOM', 'RRC', 'BBY', 'MA', 'PFE', 'JPM', 'SBUX']

for stock in stocks:
    get_news(stock)
    #get news and store it in a database for further use.
    #have a flask API that uses the enpoint to get the news.
    
