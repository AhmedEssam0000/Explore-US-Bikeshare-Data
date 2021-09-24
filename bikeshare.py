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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please choose a city from the three available cities (chicago , new york city , washington) : ").lower()
        if city not in ("chicago", "new york city", "washington"):
            print("Unfortunately, you entered wrong input")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month do you want to search for from the following months?\n [January, February, March, April, May, June, OR ALL ]").lower()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
           print("Unfortunately, you entered wrong input")
           continue
        else:
            break   

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("which day do you want to search for from the following days?\n [Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, all]").lower()
        if day not in ("saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "all"):
           print("Unfortunately, you entered wrong input")
           continue
        else:
            break  

    print('-'*50)
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
    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # get month's id and create a new dataframe filtered by month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']==month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == str(day).title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Most_Common_Month = df['month'].mode()[0]
    print(f"Most Common Month = {str(Most_Common_Month)}") 

    # display the most common day of week
    Most_Common_DayOfWeek = df['day_of_week'].mode()[0]
    print(f"Most Common Day Of The Week = {str(Most_Common_DayOfWeek)}")
    # display the most common start hour
    df['Start_hour']= df['Start Time'].dt.hour
    Most_Popular_hour = df['Start_hour'].mode()[0]
    print(f'The Most Common start hour = {str(Most_Popular_hour)}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Most_Common_Start_Station = df["Start Station"].mode()[0]
    print(f"Most Common Start Station = {str(Most_Common_Start_Station)}")

    # display most commonly used end station
    Most_Common_End_Station = df["End Station"].mode()[0]
    print(f"Most Common End Station = {str(Most_Common_End_Station)}")

    # display most frequent combination of start station and end station trip
    df["Stations Combination"] = df["Start Station"] + " & " + df["End Station"]
    Most_Common_Trip = df["Stations Combination"].mode()[0]
    print(f"Most common trip = {str(Most_Common_Trip)}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = np.sum(df['Trip Duration'])
    print(f"Total travel time = {Total_Travel_Time}  ")

    # display mean travel time
    Mean_Travel_Time = np.mean(df["Trip Duration"])
    print(f"Mean Travel Time = {Mean_Travel_Time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    User_Type_Counts = df["User Type"].value_counts()
    print(f"Counts of user types = {User_Type_Counts} ")

    # Display counts of gender
    if 'Gender' in df :
        Count_Of_Gender = df['Gender'].value_counts(dropna= True)
        print(f"Counts Of Gender = {Count_Of_Gender} ")
    else:
        print('No gender data available !')

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        Minimum = int(df["Birth Year"].min())
        maximum = int(df["Birth Year"].max())
        Common_Year_Ofbirth = int(df["Birth Year"].mode()[0])
        print(f"Minimum year of birth = {Minimum}")
        print(f"Maximum year of birth = {maximum}")
        print(f"Most common year of birth = {Common_Year_Ofbirth}")
    else:
        print('Year of birth data is not available for this city!!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def Raw_Input(df):

    Get_User_Answer = input("Do you want to see the first 5 rows of your related data?\n put 'Yes' OR 'No' : ").lower()
    list = ['yes','no']
    i = 0
    if Get_User_Answer  not in list:
        Get_User_Answer=input("please specify a correct answer! Do you want to see the next 5 rows of your related data?\n put 'Yes' OR 'No' : ").lower()
        while Get_User_Answer == 'yes':
            print(df.iloc[i:i+5, :])
            Get_User_Answer=input("Do you want to see the next 5 rows of your related data?\n put 'Yes' OR 'No' : ").lower()
            if Get_User_Answer == 'yes':
                i += 5
            else:
                break
    else:
          while Get_User_Answer == 'yes' :
            print(df.iloc[i: i+5, :])
            Get_User_Answer=input('Do you want to view the next 5 rows of your selected raw data? Yes or No : ').lower()
            if Get_User_Answer =='yes':
                i += 5
            else:
                 break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        Raw_Input(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
