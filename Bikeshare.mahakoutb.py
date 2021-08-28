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
    # get user input for city (chicago, new york city, washington). 
    # ask user to determine city 
    
    while True:
        city = input("choose city you want to explore from ('chicago', 'new york city', 'washington')")
        if city.lower()in ['chicago', 'new york city', 'washington']:
            break
        else:
         print("{} invalid input".format(city))
        
        
 
    #  get user input for month (all, january, february, ... , june)
    while True:
        month = input("choose the month you want to explore from ('jan','feb','mar','apr','may','jun','all')")
        if month.lower()in['jan','feb','mar','apr','may','jun','all']:
            break             
        else:
            print("{}invalid input".format(month))
                       
                
    #  get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("choose the day you want to explore from ('saturday','sunday','monday','tuesday','wednesday','thursday','friday','all')")
        if day.lower() in ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']:
            break
        else:
            print("{}invalid input".format(day))
            
            


    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    
   
    if month.lower() !='all':
        months=['jan','feb','mar','apr','may','jun']
        month=months.index(month)+1
        df=df[df['month']==month]
    else:
        month='all'
    if day.lower() !='all':
        df=df[df['day_of_week']== day.title()]
    else:
        day='all'                              


              
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month

    common_month = df['month'].mode()[0]
    print('most common month:',common_month)


    #display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('most common day:',common_day)
    
    


    #display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('most common start hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('most common used start station:',common_start_station)



    #display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('most common used end station:',common_end_station)
    
          
    #display most frequent combination of start station and end station trip
    
    common_start_end_station=(df['Start Station']+'-'+df['End Station']).mode()[0]
    print('most frequent combination of start station and end station trip:', common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time =df['Trip Duration'].sum()
    print('total travel time in sec :' ,total_travel_time)     #total_duration in sec 
    print('total travel time in min:' ,total_travel_time/60)   #total_duration in mins
    print('total travel time in hour:' ,total_travel_time/3600)  #total_duration in hours


    #display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time in sec :', mean_travel_time)
    print('mean travel time in min :', mean_travel_time/60)
    print('mean travel time in hour :', mean_travel_time/3600)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('counts of user types :',counts_of_user_types )
    
    


    # Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('counts of gender :',counts_of_gender)
    except KeyError:
        print('counts of gender : no data available')
        

       
    #Display earliest, most recent, and most common year of birth
    try:
        earliest=df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        most_common_year_of_birth=df['Birth Year'].mode()[0]
        print('earliest : ', earliest)
        print('most recent : ', most_recent)
        print( 'most common year of birth : ', most_common_year_of_birth)
    except KeyError:
        print('counts of gender : no data available')          
        
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

  

    #display_raw_data
    #please detrmine if you want to see some lines of raw data 
    
    i=0
    while True:
        display_data = input('would you like to see (5) lines/next (5) lines of raw data ?  , yes or no : ').lower()
        
        if display_data == 'yes':
            print(df[i:i+5])
            i+=5
        else:
            break
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
              
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

             
        restart = input('\nWould you like to restart ? Enter yes or no.\n')
        if restart.lower()!='yes':
            
            print('Thank You')
           
            break
        
        
        
        
    
    
    


if __name__ == "__main__":
	main()
    
   
