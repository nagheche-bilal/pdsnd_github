import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_list = ['chicago', 'new york city', 'washington']
month_list =  ['january', 'february', 'march', 'april', 'may', 'june','all'] 
week_list = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','all']

def confirm_inp(a, b):
    while True:
        entred_input = input(a).lower()
        try:
            if entred_input in city_list and b ==1:
                break
            elif entred_input in month_list and b ==2:
                break
            elif entred_input in week_list and b ==3:
                break
            else:
                if b == 1:
                    print('verify city please')
                if b == 2:
                    print('verify month plaese')
                if b == 3:
                    print('verify day please')
        except ValueError:
            print('wrong')
          
    return entred_input            

def get_filters():
        
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = confirm_inp('specify a city to analyze: chicago, new york city, washington', 1)
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = confirm_inp('specify the month to analyze: all, january, february, ... , june', 2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = confirm_inp('specify the day to analyze: all, monday, tuesday, ... sunday', 3)


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
   
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('common_month is: ', common_month)

    # TO DO: display the most common day of week
    common_day_week = df['day_of_week'].mode()[0]
    print('common_week is: ', common_day_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('common_start_hour is: ', common_start_hour)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print('commonly_start_station', commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print('commonly_end_station', commonly_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    
    group_station=df.groupby(['Start Station','End Station'])
    most_frequent_combination = group_station.size().sort_values(ascending= not True).head(1)
    print('most common trip from start to end:\n', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:', total_travel_time)


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('average travel time:', average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    
    if city == 'chicago' or city =='new yourk city':
        # TO DO: Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('most common year of birth:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('most recent year of birth:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('earliest year of birth:',earliest_year)
    
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def fiv_row(df):
    
    st = 0
    raw = input("\nWould you like to see first 5 rows of raw data: 'yes' or 'no'?\n").lower()
    
    while True: 
        if raw == 'no':
             break
                
        print(df.iloc[st:st+5])                  
        raw = input("\nWould you like to see first 5 rows of raw data: 'yes' or 'no'?\n").lower()
        st += 5   
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        fiv_row(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
