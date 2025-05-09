import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_valid_input(prompt, valid_options):
    """Helper function to get validated input from the user."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please choose from: {', '.join([opt.title() for opt in valid_options])}.")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city, (str) month, (str) day
    """
    print("Hello! Let’s explore some US bikeshare data!")

    city = get_valid_input("Enter a city (Chicago, New York City, Washington): ",
                           ['chicago', 'new york city', 'washington'])

    month = get_valid_input("Enter a month (all, January, February, ..., June): ",
                            ['january', 'february', 'march', 'april', 'may', 'june', 'all'])

    day = get_valid_input("Enter a day of the week (all, Monday, Tuesday, ..., Sunday): ",
                          ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'])

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
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

def display_raw_data(df):
    """Displays 5 rows of raw data upon user request, continues until user declines."""
    i = 0
    while True:
        show_data = input("\nWould you like to see 5 lines of raw data? Enter yes or no:\n").strip().lower()
        if show_data != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5
        if i >= len(df):
            print("No more data to display.")
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    
    popular_month = df['month'].mode()[0]
    print(f"the most common month: {popular_month}")
    
    # TO DO: display the most common day of week
    
    popular_week_day = df['day_of_week'].mode()[0]
    print(f"the most common day of week: {popular_week_day}")
      

    # TO DO: display the most common start hour
    
    popular_hour = df['hour'].mode()[0]
    print(f"the most common start hour: {popular_hour}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most commonly used End station: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combo'] = df['Start Station'] + " to " + df['End Station'] #Create a column for grouping trips
    common_trip = df['Start-End Combo'].mode()[0]
    print(f"Most frequent trip: {common_trip}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print(f"total travel time: {total_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types=df['User Type'].value_counts()
    print(f"counts of user types: {counts_user_types}")


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_gender = df['Gender'].value_counts()
        print(f"Counts of gender:\n{counts_gender}")
    else:
        print("No gender data available.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print(f"Earliest birth year: {earliest}")
        print(f"Most recent birth year: {recent}")
        print(f"Most common birth year: {common}")
    else:
        print("No birth year data available.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()