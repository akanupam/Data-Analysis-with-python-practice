'''importing pandas to read a csv file in structured way'''

# import pandas as pd
# import urllib.request
# movies_url = "https://gist.githubusercontent.com/aakashns/afee0a407d44bbc02321993548021af9/raw/6d7473f0ac4c54aca65fc4b06ed831b8a4840190/movies.csv"
# urllib.request.urlretrieve(movies_url,"./data/movie.csv")
# movie_dataframe = pd.read_csv("./data/movie.csv")
# print(movie_dataframe)
# print(movie_dataframe.to_dict())
# print(movie_dataframe.to_dict('records'))

'''actual start'''


import urllib.request 
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
urllib.request.urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')

import pandas as pd

covid_df = pd.read_csv( 'italy-covid-daywise.csv')

# print(type(covid_df))
# print(covid_df)
# print(covid_df.info())
# print(covid_df.describe())
# print(covid_df.shape)

# print(covid_df.new_cases)
'''or'''
# print(covid_df['new_cases'])

# print(type(covid_df.new_cases))

# print(covid_df.new_cases[203])
'''or'''
# print(covid_df.at[203,'new_cases'])
'''use of .at method to retrieve element'''

'''we can call multiple rows '''
# print(covid_df[['new_cases','date']])

covid_df_copy = covid_df.copy()

# print(covid_df.loc[243]) 
'''each retrieved row is a series object'''

# print(covid_df.head(8))
# print(covid_df.tail(15))

'''printing the first valued index'''
# print(covid_df.new_tests.first_valid_index())
'''printing rows in a range'''
# print(covid_df.loc[105:119]) 

'''for printing random index rows '''
# print(covid_df.sample(13))

'''

covid_df['new_cases'] - Retrieving columns as a Series using the column name
new_cases[243] - Retrieving values from a Series using an index
covid_df.at[243, 'new_cases'] - Retrieving a single value from a data frame
covid_df.copy() - Creating a deep copy of a data frame
covid_df.loc[243] - Retrieving a row or range of rows of data from the data frame
head, tail, and sample - Retrieving multiple rows of data from the data frame
covid_df.new_tests.first_valid_index - Finding the first non-empty index in a series

'''

total_cases = covid_df.new_cases.sum()
total_death = covid_df.new_deaths.sum()
# print(total_cases)
# print(total_death)

# print("death rate:", (total_death/total_cases*100))

total_tests = 935310 + covid_df.new_tests.sum()
# print(total_tests)

# print(total_cases/total_tests*100)


high_new_cases = covid_df.new_cases > 1000
# print(high_new_cases)
# print(covid_df[high_new_cases])
'''or'''
# print(covid_df[covid_df.new_cases > 1000])


'''for displaying all the rows of the data'''
# from IPython.display import display
# with pd.option_context('display.max_rows', 100):
#     display(covid_df[high_new_cases])


# high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > total_cases/total_tests]
# print(high_ratio_df)

'''assigning a new column in the data'''
covid_df['positive_rate'] = covid_df.new_cases/covid_df.new_tests
# print(covid_df)

'''removing the column'''
covid_df.drop(columns=['positive_rate'], inplace=True)
# print(covid_df)

'''arranging the data in ascending as well as descending'''
# print(covid_df.sort_values('new_cases', ascending=False).head(10))
# print(covid_df.sort_values('new_cases', ascending=True).head(10))

'''replacing the value at a particular index '''
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2
# print(covid_df.new_cases[172])

'''
covid_df.new_cases.sum() - Computing the sum of values in a column or series
covid_df[covid_df.new_cases > 1000] - Querying a subset of rows satisfying the chosen criteria using boolean expressions
df['pos_rate'] = df.new_cases/df.new_tests - Adding new columns by combining data from existing columns
covid_df.drop('positive_rate') - Removing one or more columns from the data frame
sort_values - Sorting the rows of a data frame using column values
covid_df.at[172, 'new_cases'] = ... - Replacing a value within the data frame

'''

'''Working with dates'''
# print(covid_df.date)

'''converting data type from object to datetime'''
covid_df.date = pd.to_datetime(covid_df.date)
# print(covid_df.date)

'''making columns of day month year and weekdays'''
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

# print(covid_df)

# covid_df_may = covid_df[covid_df.month == 5]
# print(covid_df_may)

# covid_df_may_matrix = covid_df_may[['new_cases','new_deaths','new_tests']]
# print(covid_df_may_matrix.sum())
'''or'''
# print(covid_df[covid_df.month == 5][['new_cases','new_deaths','new_tests']].sum())

# print(covid_df[covid_df.weekday ==6].new_cases.mean())

'''grouping  & aggregation'''

covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
# print(covid_month_df)

covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths','new_tests']].mean()
# print(covid_month_mean_df)

covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum()
'''doing commutative summing means summming up all the values till that index'''
# print(covid_df)

'''merging data from multiple sources'''

urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')
locations_df = pd.read_csv("locations.csv")
# print(locations_df)

location = locations_df[locations_df['location']== 'Italy']
# print(location)

covid_df['location'] = 'Italy'

merged_df = covid_df.merge(locations_df, on = "location")
# print(merged_df)
result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests']]

# print(result_df)

result_df.to_csv('results.csv',index=None)



