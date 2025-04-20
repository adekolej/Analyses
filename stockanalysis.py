import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
from tabulate import tabulate
from wartosci import duza_liczba
import tkinter as tk
from pandasgui import show



akcja = input('Ticker: ')
o = input("Timeframe")
yf.download(akcja, period=str(o))

dat = yf.Ticker(akcja)
dane = dat.history(period=str(o))

df = pd.DataFrame({
    'Open': dane['Open'],
    'High': dane['Close'],
    'Low': dane['Low'],
    'Close': dane['Close'],
    '% Change': (((dane['Close'] - dane['Open']) / dane['Open']) * 100).round(2),
    'Volume:': dane['Volume'].apply(duza_liczba)
    })
show(df)
# print(tabulate(df, headers='keys', tablefmt='psql')) - To w ewentualności (Widok w Terminalu)


wykres = input("Prepare a Graph? Y/N ")

if wykres == "Y":
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(dane.index, dane['Close'], label=f'{dat} Closing Price', color='green')
    ax.set_title(f'{akcja} Index (Closing Prices)')
    ax.set_xlabel('Date')
    plt.grid(True)
    ax.set_ylim(min(dane['Close']) - (np.average(dane['Close'] / 10)), (max(dane['Close']) + (np.average(dane['Close'] / 10))))
    ax.set_facecolor('tab:gray')

    plt.show()
exc = input("Export to Excel? Y/N ")
data = datetime.datetime.now()
if exc == "Y":
    if not os.path.exists('Sheets'):
        os.makedirs('Sheets')
    df.to_excel(f'Sheets/{akcja}_{data.day}_{data.month}.xlsx', index=False)



