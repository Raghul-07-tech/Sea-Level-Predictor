import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv("epa-sea-level.csv")
data = data.dropna(subset=['Year', 'CSIRO - Adjusted sea level (inches)'])

x = data['Year']
y = data['CSIRO - Adjusted sea level (inches)']
res = linregress(x, y)

x_pred = pd.Series(range(1880, 2051))
y_pred = res.intercept + res.slope * x_pred

plt.scatter(x, y, label="Original Data", alpha=0.5)
plt.plot(x_pred, y_pred, 'r', label="Fit Line 1880–2050")

recent_data = data[data['Year'] >= 2000]
if not recent_data.empty:
    x_recent = recent_data['Year']
    y_recent = recent_data['CSIRO - Adjusted sea level (inches)']
    res_recent = linregress(x_recent, y_recent)
    x_recent_pred = pd.Series(range(2000, 2051))
    y_recent_pred = res_recent.intercept + res_recent.slope * x_recent_pred
    plt.plot(x_recent_pred, y_recent_pred, 'g', label="Fit Line 2000–2050")

plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("sea_level_plot.png")  
print("Plot saved as 'sea_level_plot.png'")
