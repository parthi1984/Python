from yahoo_fin import stock_info as si


while True:
    ticker = input('Which stock (ticker symbol) are you looking for?\n')
    if ticker == "done":
        break
    else:
        price = si.get_live_price(ticker)
        print(f"The stock price for {ticker} is {price}.")
