import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar
import numpy as np
register_matplotlib_converters()
np.float = float  
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col='date',parse_dates=['date'])

# Clean data
f1=df.value>df.value.quantile(0.025)
f2=df.value<df.value.quantile(0.975)
df = df[f1 & f2]


def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=(14, 6))
    plt.plot(df.index,df.value,'r')
    plt.grid(True)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')    

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    aux = df.resample('M').mean().reset_index()

    aux['year'] = aux['date'].dt.year
    aux['month'] = aux['date'].dt.month 
    
    df_bar=aux.pivot(index='year', columns='month', values='value')
    # Draw bar plot

    fig, ax = plt.subplots(figsize=(13, 8))

    colors = plt.cm.tab20c(np.linspace(0, 1, 12))  

    width = 0.5 / len(df_bar.columns)  
    x = np.arange(len(df_bar.index))  
    month_names = {i: calendar.month_name[i] for i in range(1, 13)}
    for i, month in enumerate(df_bar.columns):
        ax.bar(
            x + i * width, 
            df_bar[month], 
            width=width, 
            label=f'{month_names[month]}', 
            color=colors[i]
        )

    ax.legend(title='Months', loc='upper left')
    ax.set_xlabel('Years', fontsize=12)
    ax.set_xticks(x + width * (len(df_bar.columns) - 1) / 2)
    ax.set_xticklabels(df_bar.index, fontsize=10)
    ax.set_ylabel('Average Page Views',fontsize=12)
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    cmap = plt.cm.tab20 
    colors = list(cmap(np.linspace(0, 1, len(df_box['year'].unique()))))

    flierprops = dict(marker='o', color='black', markersize=7, markerfacecolor='red')

    sns.boxplot(x='year', y='value',data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.grid(True, color='gray', linestyle='--', linewidth=0.5,dashes=(10, 5))

    colors = list(cmap(np.linspace(0, 1, len(df_box['month'].unique()))))
    months=list(calendar.month_abbr[1:])
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=months, hue='month', palette=colors,flierprops=flierprops)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.grid(True, color='gray', linestyle='--', linewidth=0.5,dashes=(10, 5))

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


