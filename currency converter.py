import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_rates(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates")
    return response.json()["rates"]

def convert():
    try:
        amount = float(amount_entry.get())
        from_cur = from_currency.get().upper()
        to_cur = to_currency.get().upper()
        rates = get_rates(from_cur)
        if to_cur not in rates:
            messagebox.showerror("Error", f"Currency {to_cur} not found.")
            return
        result = amount * rates[to_cur]
        result_label.config(text=f"{amount} {from_cur} = {result:.2f} {to_cur}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Currency Converter")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky="NSEW")

ttk.Label(mainframe, text="Amount:").grid(row=0, column=0, sticky="E")
amount_entry = ttk.Entry(mainframe, width=15)
amount_entry.grid(row=0, column=1, sticky="W")

ttk.Label(mainframe, text="From:").grid(row=1, column=0, sticky="E")
from_currency = ttk.Entry(mainframe, width=5)
from_currency.grid(row=1, column=1, sticky="W")
from_currency.insert(0, "USD")

ttk.Label(mainframe, text="To:").grid(row=2, column=0, sticky="E")
to_currency = ttk.Entry(mainframe, width=5)
to_currency.grid(row=2, column=1, sticky="W")
to_currency.insert(0, "EUR")

convert_btn = ttk.Button(mainframe, text="Convert", command=convert)
convert_btn.grid(row=3, column=0, columnspan=2, pady=5)

result_label = ttk.Label(mainframe, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()