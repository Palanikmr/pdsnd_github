import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
        city = input("\n Enter the name of the city to analyze :(New york city or Chicago or Washington ) \n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("Entered wrong input . Enter again.")
        else:
            break
# TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\n Enter the month ( January, February, March, April, May, June or all \n").lower()
        if month not in ('january', 'jebruary', 'march', 'april', 'may', 'june', 'all'):
            print("Entered wrong input . Enter again.")
        else:
            break

 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Enter the day of week : Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all \n").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Entered wrong input . Enter again.")
        else:
            break

    print('-'*40)
    return city, month, day
    
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

# filter by month if applicable
# use the index of the months list to get the corresponding int
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
    # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    # filter by day of week to create the new dataframe
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    print("The most common month is: ", df['month'].mode()[0])

    # display the most common day of week
    print("The most common day of week is: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station
    
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    
    Both_Stations = (df['Start Station'] + " -- " + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip ")  
    print(Both_Stations)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time :', total_travel_time/3600, "Hours")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time : ", mean_travel_time/3600,"Hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
      
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
  
    if city == 'new york city' or city == 'chicago':
    
    # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('Gender Count :\n',gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].value_counts().idxmax())
        print("The earliest birth year is:",earliest)
        print("The most recent Year is:",most_recent)
        print("The most common Year of birth is: ",most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    count = 0
    while True:
        data_view = input("Would you like to view 5 rows of individual trip data? (yes or no): ").lower()
        if (data_view == 'yes'):
            print(df[count:count+5])
            count += 5
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
