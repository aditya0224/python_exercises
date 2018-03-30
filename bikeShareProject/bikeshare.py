import datetime
import time
import re
## TODO: import all necessary packages and functions


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
	'''Asks the user for a city and returns the filename for that city's bike share data.

	Args:
		none.
	Returns:
		(str) Filename for a city's bikeshare data.
	'''
	city = input('\nHello! Let\'s explore some US bikeshare data!\n Would you like to see data for Chicago, New York, or Washington?\n')
	if 'chicago' == city.lower():
		return chicago
	elif 'newyork' == (city.lower()).replace(' ', ''):
		return new_york_city
	elif 'washington' == city.lower():
		return washington
	else:
		print('Please provide a valid input. \n')
		get_city()
	
def get_time_period():
	'''Asks the user for a time period and returns the specified filter.

	Args:
		none.
	Returns:
		(str) the time period which user chose
	'''
	time_period = input('\nWould you like to filter the data by month, day, or not at'
						' all? Type "none" for no time filter.\n')
						
	if time_period.lower() not in ['month', 'day', 'none']:
		print('please provide a valid input. \n')
		get_time_period()
		
	return time_period.lower()

def get_month():
	'''Asks the user for a month and returns the specified month.
	Args:
		none.
	Returns:
		(str) month the use chose from
	'''
	month = input('\nWhich month? January, February, March, April, May, or June?\n')

	if month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:	
		print('please provide a valid input. \n')
		get_month()
	
	return month.lower()

def get_day(month):
	'''Asks the user for a day and returns the specified day.
	Args:
		none.
	Returns:
		(int) return the day of the month 
	'''
	day = input('\nWhich day? Please type your response as an integer.\n')
	
	if day not in range(1,31):
		print('Enter a valid day')
		get_day(month)
		
	return int(day)

def extract_start_date(city_file):	
	'''extract the state date from the file
	Args:
		(string) csv file of the city selected by user
	Returns:
		(list) list of all start dates for the city selected
	'''
	start_dates = []
	read_header = False

	rows = extract_city_data(city_file)
	for row in rows[1:]:
		column_data = row.split(',')
		if column_data[1] is not None:
			if(column_data[1].find('/')> -1):
				start_dates.append(datetime.datetime.strptime(column_data[1], "%m/%d/%Y %H:%M"))
			else:
				start_dates.append(datetime.datetime.strptime(column_data[1], "%Y-%m-%d %H:%M:%S"))
				

	return start_dates

def extract_end_date(city_file):
	'''extract the end date from the file

	Args:
		(string) csv file of the city selected by user
	Returns:
		(list) list of all end dates for the city selected
	'''
	
	end_dates = []
	read_header = False
	
	rows = extract_city_data(city_file)
	
	for row in rows[1:]:
		column_data = row.split(',')
		if(column_data[1].find('/')>-1):
			end_dates.append(datetime.datetime.strptime(column_data[1], "%m/%d/%Y %H:%M"))
		else:
			end_dates.append(datetime.datetime.strptime(column_data[1], "%Y-%m-%d %H:%M:%S"))

	return end_dates
	
def extract_start_station(city_file):
	'''extract the state station from the file

	Args:
		(string) csv file of the city selected by user
	Returns:
		(list) list of all start stations for the city selected
	'''
	start_stations = []
	read_header = False	
	rows = extract_city_data(city_file)
	
	for row in rows[1:]:
		column_data = row.split(',')
		start_stations.append(column_data[4])

	return start_stations

def extract_end_station(city_file):
	'''extract the end stations from the file

	Args:
		(string) csv file of the city selected by user
	Returns:
		(list) list of all end stations for the city selected
	'''
	end_stations = []
	read_header = False	
	rows = extract_city_data(city_file)

	for row in rows[1:]:
		column_data = row.split(',')
		end_stations.append(column_data[5])

	return end_stations
	
def extract_city_data(city_file):
	'''extract the rows of city data

	Args:
		(string) csv file of the city selected by user
	Returns:
		(list) list of all the rows of city data including header
	'''
	with open(city_file, 'r') as file:
		rows = file.readlines()
	
	return rows

def calculate_highest_frequency(values):
	'''calculate the mode of the list of values

	Args:
		(list) input of any values
	Returns:
		(mixed) return the value of highest frequency
	'''
	values_count = {}
	
	for value in values:
		if value in values_count:
			values_count[value] = values_count[value] + 1
		else:
			values_count[value] = 1

	highest_frequency = 0
	frequenct_value = 0
	for value, frequency in values_count.items():
		if frequency > highest_frequency:
			highest_frequency = frequency
			frequenct_value = value
	
	return frequenct_value
	
def get_popular_month(city_file, time_period):
	'''most popular month for start time
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(int) return the most popular month
	'''
	
	start_dates = extract_start_date(city_file)
	start_months = []
	extract_month = lambda start_date: start_date.month
	start_months = map(extract_month, start_dates)
	
	popular_month = calculate_highest_frequency(start_months)
	print(popular_month)
	
	return popular_month
	
def get_popular_day(city_file, time_period):
	'''most popular day for start time
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(int) return the most popular day
	'''
	start_dates = extract_start_date(city_file)
	start_days = []
	extract_day = lambda start_date: start_date.day
	start_days = map(extract_day, start_dates)

	popular_day = calculate_highest_frequency(start_days)
			
	return popular_day

def get_popular_hour(city_file, time_period):
	'''most popular hour for start time
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(int) return the most popular hour
	'''
	# TODO: complete function
	start_dates = extract_start_date(city_file)
	start_hours = []
	extract_hour = lambda start_date: start_date.hour
	start_hours = map(extract_hour, start_dates)
	popular_hour = calculate_highest_frequency(start_hours)
			
	return popular_hour

def get_trip_duration(city_file, time_period):
	'''most popular month for start time
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(list) return total duration and the total trips
	'''

	start_dates = extract_start_date(city_file)
	end_dates = extract_end_date(city_file)

	total_duration = datetime.timedelta(0);
	total_trips = 0;
	for dates in zip(start_dates, end_dates):
		total_duration = (dates[1] - dates[0]) + total_duration
		total_trips += 1
	
	return total_duration, total_trips	

def get_popular_trip(city_file, time_period):
	'''most popular trip
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(list) return list of most popular trip
	'''

	trip_stations = {}
	rows = extract_city_data(city_file)

	for row in rows[1:]:
		column_data = row.split(',')
		end_station = column_data[5]
		start_station = column_data[5]
		trip_station = end_station+'~'+start_station
		if trip_station in trip_stations :
			trip_stations[trip_station] = trip_stations[trip_station] + 1;
		else:
			trip_stations[trip_station] = 1;
	max_count = 0
	popular_trip = '';
	for trip_station in trip_stations.items():
		if max_count < trip_station[1]:
			max_count = trip_station[1]
			popular_trip = trip_station[0]

	return popular_trip.split('~')
	
def users(city_file, time_period):
	'''most popular month for start time
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(dictionary) return the count of subscription user and just customers
	'''

	trip_stations = {}
	rows = extract_city_data(city_file)

	user_data_dict = {'Subscriber': 0, 'Customer':0}
	for row in rows[1:]:
		column_data = row.split(',')
		month_data = column_data[6].rstrip('\n')
		if month_data == 'Subscriber':
			user_data_dict['Subscriber'] = user_data_dict['Subscriber'] + 1
		elif month_data == 'Customer':
			user_data_dict['Customer'] = user_data_dict['Customer'] + 1
	return user_data_dict
	
def gender(city_file, time_period):
	'''most popular month for start time
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(dictionary) return the male and female count of users
	'''

	gender = {}
	rows = extract_city_data(city_file)

	gender_data = {'Male': 0, 'Female':0}
	for row in rows[1:]:
		column_data = row.split(',')
		if len(column_data) > 7 and column_data[7] == 'Male':
			gender_data['Male'] = gender_data['Male'] + 1
		elif len(column_data) > 7 and column_data[7] == 'Female':
			gender_data['Female'] = gender_data['Female'] + 1

	return gender_data

def birth_years(city_file, time_period):
	'''most popular month for start time
	Args:
		(string) csv file of the city selected by user
		(string) time period user requested
	Returns:
		(list) return the most popular year of birth, oldest and youngest user birth year
	'''
	rows = extract_city_data(city_file)
	date_of_birth_list = []
	for row in rows[1:]:
		column_data = row.split(',')
		yearData = column_data[8].rstrip('\n')
		if yearData not in ['Male', 'Female', '', ' ']:
			date_of_birth_list.append(yearData)
	
	popular_year = calculate_highest_frequency(date_of_birth_list)
	oldest_user = max(date_of_birth_list)
	youngest_user = min(date_of_birth_list)

	return [int(float(popular_year)), int(float(oldest_user)), int(float(youngest_user))]
	
def display_data(city):
	'''Displays five lines of data if the user specifies that they would like to.
	After displaying five lines, ask the user if they would like to see five more,
	continuing asking until they say stop.

	Args:
		none.
	Returns:
		TODO: fill out return type and description (see get_city for an example)
	'''
	display = input('\nWould you like to view individual trip data?'
					'Type \'yes\' or \'no\'.\n')
					
	rows = extract_city_data(city)					

	count = 0

	if(display.lower() == 'no'):
		return
		
	for row in rows[1:]:
		column_data = row.split(',')
		print(column_data)
		count = count + 1
		if(count % 5 == 0):
			display = input('\nWould you like to view individual trip data?'
					'Type \'yes\' or \'no\'.\n')			
			if(display.lower() == 'yes'):
				continue
			else:
				break

def statistics():
	'''Calculates and prints out the descriptive statistics about a city and time period
	specified by the user via raw input.

	Args:
		none.
	Returns:
		none.
	'''
	city = get_city()
	time_period = get_time_period()

	print('Calculating the first statistic...')
	if time_period == 'none':
		start_time = time.time()
		popular_month = get_popular_month(city, time_period)
		print('Popular month for time period is : {}'.format(popular_month))
		print("That took %s seconds." % (time.time() - start_time))
		print("Calculating the next statistic...")
	if time_period == 'none' or time_period == 'month':
		start_time = time.time()
		popular_day = get_popular_day(city, time_period)
		print('Popular day for time period is : {}'.format(popular_day))
		print("That took %s seconds." % (time.time() - start_time))
		print("Calculating the next statistic...")    

	start_time = time.time()
	popular_hour = get_popular_hour(city, time_period)
	print('Popular hour for time period is : {}'.format(popular_hour))
	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()
	total_duration, total_trips = get_trip_duration(city, time_period)
	
	print('Total duration of the trips is {}'.format(total_duration))
	print('Average duration of the trips is {}'.format(total_duration / total_trips))
	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()
	
	start_stations = extract_start_station(city)
	end_stations = extract_end_station(city)
	popular_start_station = calculate_highest_frequency(start_stations)
	popular_end_station = calculate_highest_frequency(end_stations)
	
	print('popular station for the trip to start is {} '.format(popular_start_station))
	print('popular station for the trip to end is {} '.format(popular_end_station))
	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	start_time = time.time()
	popular_trip = get_popular_trip(city, time_period)
	
	print('popular trip stations are {}'.format(popular_trip))
	print("That took %s seconds." % (time.time() - start_time))
	print("Calculating the next statistic...")
	
	start_time = time.time()
	user_data = users(city,time_period)
	print('The user data is {}'. format(user_data))

	if city != washington:	
		print("That took %s seconds." % (time.time() - start_time))
		print("Calculating the next statistic...")
		start_time = time.time()
		gender_data = gender(city,time_period)
		print('The user gender data is {}'. format(gender_data))
		print("That took %s seconds." % (time.time() - start_time))
		print("Calculating the next statistic...")
		start_time = time.time()
		birth_year_list = birth_years(city,time_period)
		print('most popular user year , Youngest user and Oldest user are {} '.format(birth_year_list))
		print("That took %s seconds." % (time.time() - start_time))

	display_data(city)

	restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
	if restart.lower() == 'yes':
		statistics()


if __name__ == "__main__":
	statistics()