import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 1. Clean the data by filtering out outliers
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# 2. Function to draw the line plot

def draw_line_plot():
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('page Views')
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

draw_line_plot()

# 3. Function to draw the bar plot for monthly averages

def draw_bar_plot():
    # Create a new dataframe for monthly data
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Create a pivot table with year as index and months as columns
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Plot the bar plot

    df_bar.plot(kind='bar', figsize=(10, 5))
    plt.title('Monthly average page views')
    plt.xlabel('Years')
    plt.ylabel('Average page Views')
    plt.legend(title='Month', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

draw_bar_plot()

# 4. Function to draw box plots to show yearly and monthly distributions
def draw_box_plot():
    # Prepare the data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Sort months in chronological order
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Set up the matplotlib figure

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Yearly box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Monthly box plot

    sns.boxenplot(x='month', y='value', data=df_box, order=months_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    #Display the plot
    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()

draw_box_plot()



