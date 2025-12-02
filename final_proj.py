"""
ISTA 350 Final Project:
web: Wikipedia--List of cities by average temperature
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import re

# grab the data from Wikipedia
def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    r = requests.get(url, headers=headers)
    df_list = pd.read_html(r.content)
    return df_list[3] # grab the North America table

# Clean the temperature value
def clean_temp_value(x):
    if pd.isna(x):
        return None
    x = str(x)
    # Extract the first number (Celsius is always first)
    match = re.search(r"[-+]?\d*\.\d+|[-+]?\d+", x)
    return float(match.group()) if match else None

# claen the data
def clean_data(df):
    months = ["Jan","Feb","Mar","Apr","May","Jun",
              "Jul","Aug","Sep","Oct","Nov","Dec"]
    for m in months:
        df[m] = df[m].apply(clean_temp_value)
    return df

# the data for the first plot
# The Tucson average temperature
def Tucson_data(df):
    tucson_df = df[df["City"].str.contains("Tucson", case=False)]
    return tucson_df

# the first plot
def plot1(tucson_df):
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    tucson_temps = tucson_df[months].T
    tucson_df["Year"] = tucson_df["Year"].apply(lambda x: float(x.split()[0]))
    # the numeric annual average
    year_avg = tucson_df["Year"].iloc[0]
    tucson_temps.columns = ["Tucson"]
    tucson_temps.plot(figsize=(10,5), marker="o",color="orange")
    plt.axhline(y=year_avg, linestyle = 'dashed',linewidth = '2',color="red")
    plt.title("Monthly Average Temperature in Tucson",size="20")
    plt.xticks(ticks=range(12), labels=months, size=12)
    plt.xlabel("Month",size=20)
    plt.ylabel("Temperature (°C)",size=20)
    plt.legend(['Tucson temperature','Tucson average temperature(year)'])

# the data for the plot2--the Jan&Jul data of all the United States city shown in this North America DataFrame
def plot2_data(df):
    United_States_df = df[df["Country"].str.contains("United States", case=False)]
    return  United_States_df[['City', 'Jan', 'Jul']]

# plot2
def plot2(United_States_df):
    x = United_States_df["City"]
    y1 = United_States_df["Jul"]
    y2 = United_States_df["Jan"]
    height = y1 - y2
    plt.bar(x, height, bottom=y2, color="orange")
    plt.xticks(rotation=90,size=10)
    plt.yticks(range(0,37),size=10)
    plt.ylabel("Temperature (°C)",size=20)
    plt.title("Comparing Winter(Jan) and Summer(Jul) Temperatures Across U.S. Cities",size=20)

# data for plot3
def plot3_data(df):
    United_States_df = df[df["Country"].str.contains("United States", case=False)]
    return  United_States_df[['City', 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']]

# plot3
def plot3(df):
    x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # Washington subplot--humid subtropical climate
    Washington_df = df[df["City"].str.contains("Washington", case=False)]
    y1 = Washington_df[x].iloc[0]
    plt.subplot(2, 3, 1)
    y1.plot(color="orange")
    plt.title("Washington",size=20)
    plt.xticks(ticks=range(12), labels=x, size=10)
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35], size=10)

    # Chicago--humid continental.
    Chicago_df = df[df["City"].str.contains("Chicago", case=False)]
    y2 = Chicago_df[x].iloc[0]
    plt.subplot(2, 3, 2)
    y2.plot(color="orange")
    plt.title("Chicago",size=20)
    plt.xticks(ticks=range(12), labels=x, size=10)
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35], size=10)

    # Phoenix--hot desert climate
    Phoenix_df = df[df["City"].str.contains("Phoenix", case=False)]
    y3 = Phoenix_df[x].iloc[0]
    plt.subplot(2, 3, 3)
    y3.plot(color="orange")
    plt.title("Phoenix",size=20)
    plt.xticks(ticks=range(12), labels=x, size=10)
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35], size=10)

    # San Francisco--Mediterranean-type
    San_Francisco_df = df[df["City"].str.contains("San Francisco", case=False)]
    y4 = San_Francisco_df[x].iloc[0]
    plt.subplot(2, 3, 4)
    y4.plot(color="orange")
    plt.title("San Francisco",size=20)
    plt.xticks(ticks=range(12), labels=x, size=10)
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35], size=10)

    # Miami--tropical monsoon
    Miami_df = df[df["City"].str.contains("Miami", case=False)]
    y5 = Miami_df[x].iloc[0]
    plt.subplot(2, 3, 5)
    y5.plot(color="orange")
    plt.title("Miami",size=20)
    plt.xticks(ticks=range(12), labels=x, size=10)
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35], size=10)

    # Denver--Continental semi-arid climate
    Denver_df = df[df["City"].str.contains("Denver", case=False)]
    y6 = Denver_df[x].iloc[0]
    plt.subplot(2, 3, 6)
    y6.plot(color="orange")
    plt.title("Denver",size=20)
    plt.xticks(ticks=range(12), labels=x, size=10)
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35], size=10)
    # suptitle
    plt.suptitle("Climate Comparison Across U.S. Cities", size=30)



def main():
    # URL
    url = 'https://en.wikipedia.org/wiki/List_of_cities_by_average_temperature#North_America'
    # grab the data from the website
    df = get_data(url)
    # clean data 
    df = clean_data(df)
    print(f'Cleaned data:\n{df}')
    # Tucson temp data
    tucson_df=Tucson_data(df)
    print(tucson_df)
    # plot1
    plot1(tucson_df)
    plt.show() 
    # Data for plot2
    US_data_17=plot2_data(df)
    print(US_data_17)
    # plot2
    plot2(US_data_17)
    plt.show() 
    # US data
    US_data=plot3_data(df)
    print(US_data)
    # plot3
    plot3(US_data)
    plt.show()
   
if __name__ == '__main__':
    main()

