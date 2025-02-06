import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mt
import yfinance as yf

forecast = pd.read_csv('gold_price_myForecast-2024Q4.csv', parse_dates=['Date'])

gold = yf.ticker.Ticker('GC=F')
truth = gold.history(period='6mo')
truth = truth.loc[(truth.index >= "2024-09-30 00:00:00-04:00") & (truth.index < "2025-01-01 00:00:00-05:00")]
truth_avg = truth[['High', 'Low']].mean(axis=1)

interpolations = ['Nearest', 'Linear', 'Quadratic']
colors = ['#334E7E', '#DE94C7', '#6E7256']
plt.figure(figsize=(12,6))
plt.plot(forecast.Date, truth_avg, color='#F2BA03', label='ground truth', zorder=2)
for i, interpolation, color in zip(range(3), interpolations, colors):
    plt.plot(forecast.Date, forecast.iloc[:,i+2], color=color,
             label=f'forecast with {interpolation} interpolation', zorder=i+2.5)
trans = mt.blended_transform_factory(plt.gca().transData, plt.gca().transAxes)
plt.vlines(x=[pd.Timestamp("2024-10-01"), pd.Timestamp("2024-11-01"), pd.Timestamp("2024-12-01"), pd.Timestamp("2025-01-01")],
           ymin=0, ymax=1, transform=trans, color='gray', zorder=1.5, linestyle='dashed')
plt.legend()
plt.show()