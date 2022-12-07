import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    
    while True:
        city=input('Would you like to see data for Chicago, New York or Washington? ').lower()
        if city not in CITY_DATA.keys():
            print(" Please chooes between Chicago, New York City or Washington: ")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Which month? All, January, February, March, April, May, June or other? ')
        month = month.lower()
        if month == 'other' or month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
           print (" Plase chooes between January, February, March, April, May, June or All ")
           continue
        else:
            break
        
         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('which day? ').lower()
    while day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        day=input('Please type correct day or all if you want').lower()
        
       
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
    if city == 'new york':
        city= 'new_york_city'
    df = pd.read_csv('{}.csv'.format(city))
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
   	 	
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month= df['month'].mode()[0]
    print('The most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most Common day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_station= df['Start Station'].value_counts().idxmax()
    print('The most Commonly used start station:', Start_station)
    print()
    # TO DO: display most commonly used end station
    End_station = df['End Station'].value_counts().idxmax()
    print('The most Commonly used end station:', End_station)
    print()
    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('The most Commonly used combination of start station and end station trip:', Start_station, " & ", End_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time= ", df['Trip Duration'].sum())
    print()
    # TO DO: display mean travel time
    print("Mean travel time= ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\n The counts of user types= ',user_types)

    # TO DO: Display counts of gender
    try:
        print('\n The counts of gender= ', df['Gender'].value_counts())
    except KeyError:
        print('No data available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\n The earliest year of birth: ', int(df['Birth Year'].min()))
        print('\n The most common year of birth: ', int(df['Birth Year'].mode()[0]))
        print('\n The latest year of birth: ', int(df['Birth Year'].max()))
    except KeyError:
        print('No data available') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data (df):
    
    view_data=input('Would you like to view 5 rows of individual trip data? yes or no? ').lower()
    start_loc = 0
    while (view_data!= 'no'):
        print(df.head(start_loc))
        start_loc+=5
        view_data=input('Do you wish to continue yes or no?  ').lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data (df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
