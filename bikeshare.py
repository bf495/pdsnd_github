import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january',
          'february',
          'march',
          'april',
          'may',
          'june',
          'all']

DAYS = ['sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'all']

# Variable used for raw data
n = 0

def get_filters():
# Collects user input for desired city 
    city = input("Hello! Please select one the following cities: Chicago, New York City, Washington \n").lower()
    while city not in CITY_DATA:
        print("\nOops! It seems there was an error with your selection. The selected city was not found. Restarting...")
        city = input("Hello! Please select one the following cities: Chicago, New York City, Washington \n").lower()
            
    print("You chose: ", city.capitalize())

# Collects user input for desired month
    month = input("Which month would you like to analyze: January, February, March, April, May, June, or All? \n").lower()
    while month not in MONTHS:
        print("\nOops! It seems there was an error with your selection. The selected month was not found. Restarting...")
        month = input("Which month would you like to analyze: January, February, March, April, May, June, or All? \n").lower()
    
    print("You chose: ", month.capitalize())

# Collects user input for desired day of the week
    day = input("Which day would you like to analyze: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All? \n").lower()
    while day not in DAYS:
        print("\nOops! It seems there was an error with your selection. The selected day was not found. Restarting...")
        day = input("Which day would you like to analyze: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All? \n").lower()
    
    print("You chose: ", day.capitalize())

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
"""
Loads data for the specified city and filters by month and day if applicable.

Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    
Returns:
    df - Pandas DataFrame containing city data filtered by month and day
"""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        MONTHS = ['january','february','march','april','may','june']
        month = MONTHS.index(month) + 1

        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day'] == day.title()]
    
    return df


def time_stats(df):
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

# Display the most popular month
    pop_month = df['month'].mode()[0]
    print("Most Popular Month: ", pop_month)

# Display the most common day of week
    pop_day = df['day'].mode()[0]
    print("Most Popular Day: ", pop_day)

# Display the most common start hour
    pop_hour = df['hour'].mode()[0]
    print("Most Popular Hour: ", pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

# Display the most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("The most commonly used start station is ", most_common_start)

# Display the most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print("The most commonly used end station is ", most_common_end)

# Display the most frequent combination of start station and end station trip
    most_common_combo = df.loc[:, 'Start Station':'End Station'].mode()[0:]
    mcc = most_common_combo.to_string(index=False)

    print("The most frequent combination of start station and end station is \n", mcc)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

# Display the total travel time
    df['time diff'] = df['End Time'] - df['Start Time']
    time_diff_sum = df['time diff'].sum()
    print("The total travel time is ", time_diff_sum)

# Display the mean travel time
    time_diff_mean = df['time diff'].mean()
    print("The mean travel time is ", time_diff_mean)
                         
                         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    print("\nCalculating User Stats...\n")
    start_time = time.time()

# Display the counts of user types
    user_counts = df['User Type'].value_counts()
    print("The count of user types is ", user_counts)

# Display the counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("The count of genders is ", gender_counts)
    except:
        print("No gender data available for this selection")

# Display the earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        ey_int = earliest_year.astype(int)
        most_recent_year = df['Birth Year'].max()
        ry_int = most_recent_year.astype(int)
        most_common_year = df['Birth Year'].mode()
        mcy_int = most_common_year.astype(int)
        mcy_string = mcy_int.to_string(index=False)

        print("The oldest customer was born in ", ey_int)
        print("The youngest customer was born in ", ry_int)
        print("The common birth year for our customers is ", mcy_string)
    except:
        print("No birth year data available for this selection")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df, n):
    
#Ask user if they want to display raw data
    raw_data_prompt = input("Would you like to review the next 5 rows of raw data now? Please enter YES or NO \n")
    if raw_data_prompt.lower() == 'yes':
        print(df.iloc[n:n+5])
        n += 5
        return raw_data(df, n)
    
    if raw_data_prompt.lower() == 'no':
        return
    
    else:
        print("Invalid input. Please enter YES or NO.")
        return raw_data(df, n)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df, n)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
