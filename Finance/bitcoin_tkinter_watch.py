import tkinter as tk
import requests
import arrow


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

# Create a root window to hold all widgets
root = tk.Tk()
root.title("Bitcoin Watch")
root.geometry("1000x400")
# Create a first label
label = tk.Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# Create Second label
label2 = tk.Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()


# Define the bitcoin_watch function
def bitcoin_watch():
    response = requests.get(url, headers=headers)
    response_json = response.json()
    price = response_json['bpi']['USD']['rate_float']

    # Obtain current date and time information
    tdate = arrow.now().format('MMMM DD, YYYY')
    tm = arrow.now().format('hh:mm:ss A')

    # Put the date and time information in the first label
    label.configure(text=tdate + "\n" + tm)

    # Put the price info in the second label
    label2.configure(text=f'Bitcoin: {price}', justify=tk.LEFT)

    # Call the bitcoin_watch function after 1000 ms
    root.after(1000, bitcoin_watch)


# Call the bitcoint_watch function
bitcoin_watch()

# Run the loop
root.mainloop()
