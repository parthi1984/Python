import requests
from yahoo_fin import stock_info as si


while True:
    firm = input("Which company's ticker symbol are you looking for?\n")
    if firm == "done":
        break
    else:
        try:
            url = "https://query1.finance.yahoo.com/v1/finance/search?q="+firm
            headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            quotes = response_json['quotes']
            ticker = quotes[0]['symbol']
            price = round(float(si.get_live_price(ticker)), 2)
            print(f"The ticker symbol for {firm} is {ticker}.")
            print(f"The stock price for {firm} is {price}.")
        except:
            print("Sorry, not a valid entry!")
        continue
