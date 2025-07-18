import pandas as pd
import matplotlib.pyplot as plt
from scipy import linregress

def draw_plot():
    #Read Data
    df = pd.read_csv('epa-sea-level.csv')

    #create scatter plot
    plt.scatter(df['year'], df['CSIRO Adjusted Sea Level'], label = 'Original Data')

    #First line of best fit(1880 to 2050)
    res = linregress(df['year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred * res.intercept
    plt.plot(x_pred, y_pred, 'r', label = 'Best Fit 1880-2051')

    #Second Line of the best (2000 to 2050)
    df_recent  = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, 'g', label = 'Best Fit 2000-2051')

    #Labels and Title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    #Save lpot
    plt.savefig('sea-level.png')
    return plt.gca()