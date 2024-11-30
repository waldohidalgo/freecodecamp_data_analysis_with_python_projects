import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np 

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5,c='r')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended=np.arange(df['Year'].min(), 2051)
    plt.plot(years_extended, res.intercept + res.slope*years_extended, 'b', label='fitted line')

    # Create second line of best fit
    years_from_2000=np.arange(2000, 2051)
    df_2000=df[df.Year>=2000]
    res_2000=linregress(df_2000.Year, df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(years_from_2000, res_2000.intercept + res_2000.slope*years_from_2000, 'g', label='2000 fitted line')

    # Add labels and title
    plt.grid(True, color='gray', linestyle='--', linewidth=0.2,dashes=(25, 25))
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Sea Level (inches)',fontsize=12)
    plt.title('Rise in Sea Level')
    plt.tight_layout()

    y_proj_1 = res.intercept + res.slope * 2050 
    y_proj_2 = res_2000.intercept + res_2000.slope * 2050
    plt.axvline(x=2050, color='purple', linestyle='--', linewidth=1, label='Projection Year (2050)')
    plt.axhline(y=y_proj_1, color='blue', linestyle='--', linewidth=1)
    plt.axhline(y=y_proj_2, color='green', linestyle='--', linewidth=1)


    plt.text(2040, y_proj_1*1.025, f'{y_proj_1:.2f}', color='blue', va='center', fontsize=12,fontweight='bold')
    plt.text(2037, y_proj_2*0.975, f'{y_proj_2:.2f}', color='green', va='center', fontsize=12,fontweight='bold')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()