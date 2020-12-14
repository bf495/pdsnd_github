## Project - Explore US Bikeshare Data
The goal of this project is to analyze data related to bike share systems by using Python. The code looks at datasets from .csv files to provide metrics/statistics to the user. The raw data can also be vieiwed if desired. The user can filter this data using several options, including city, month and day of the week.

## Datasets
There are three datasets in total. Each contains data from a city - Chicago, New York and Washington. 

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

 - Start Time (e.g., 2017-01-01 00:07:57)
 - End Time (e.g., 2017-01-01 00:20:53)
 - Trip Duration (in seconds - e.g., 776)
 - Start Station (e.g., Broadway & Barry Ave)
 - End Station (e.g., Sedgwick St & North Ave)
 - User Type (Subscriber or Customer)

*The Chicago and New York City files also have the following two columns:*

 - Gender
 - Birth Year

## How to use

1. Run the bikeshare.py file
2. Enter the name of the city you wish to collect data from
3. Enter the name of the month you wish to filter by (or type All)
4. Enter the name of the day you wish to filter by (or type All)
5. After the data has been displayed, you can choose to view the raw data in intervals of five rows
6. After declining the option to view raw data, you can choose to run the program again or exit the program

## Resources
https://smallbusiness.chron.com/making-raw-input-lowercase-python-31840.html
https://www.w3schools.com/python/python_try_except.asp
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
