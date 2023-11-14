import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/mac/Downloads/state_crime.csv")
print(df.head())

# Checking the data types
print(df.dtypes)

# Checking missing values. There are no missing values in the dataset.
miss = df.isnull().sum()
print(miss)

# Checking duplicates in data frame
duplicate = df[df.duplicated()]
print(len(duplicate))

# Creating a DataFrame and indexing values
index = pd.Index(range(len(df)))
y = df.set_index('Year')
df = pd.DataFrame(df)

# Renaming column names
df.rename(columns = {'Data.Population':'Population', 'Data.Rates.Property.All':'Rates of all crimes', 
                    'Data.Rates.Property.Burglary':'Rates of burglary', 'Data.Rates.Property.Larceny':'Rates of larceny',
                    'Data.Rates.Property.Motor':'Rates of motor', 'Data.Rates.Violent.All':'Rates of violent crimes',
                    'Data.Rates.Violent.Assault':'Rates of violent assault', 'Data.Rates.Violent.Murder':'Rates of violent murder',
                    'Data.Rates.Violent.Rape':'Rates of violent rape', 'Data.Rates.Violent.Robbery':'Rates of violent robbery',
                    'Data.Totals.Property.All':'Total crimes', 'Data.Totals.Property.Burglary':'Total burglary',
                    'Data.Totals.Property.Larceny':'Total larceny', 'Data.Totals.Property.Motor':'Total motor',
                    'Data.Totals.Violent.All':'Total violent crimes', 'Data.Totals.Violent.Assault':'Total violent assault',
                    'Data.Totals.Violent.Murder':'Total violent murder', 'Data.Totals.Violent.Rape':'Total violent rape',
                    'Data.Totals.Violent.Robbery':'Total violent robbery'}, inplace=True)

# Selecting the year 2013 and above  
search_year = df.query('Year >= 2013')

# Show all rows in VS Code terminal and find indexs of rows contained 'United States' value
pd.set_option('max_row', None)
search_year.head(None)
print(search_year)

# Delete the rows contains the United States value
search_year.drop(labels = range(2688, 2695), axis = 0, inplace = True)
print(search_year)

# statistic describe the data
print(search_year.describe())

# List of state values
states_collect = pd.unique(search_year['State'])
print(len(states_collect))

# Q1: What's the average population in each state in 2013-2019?
# Filter out labels of interest, group the data on state values and make a statistic description 
grouped_sp = search_year.filter(['State', 'Population'])
grouped_sp = grouped_sp.groupby(['State']).describe()
grouped_sp = grouped_sp.reset_index()
print(grouped_sp)

max_p = grouped_sp['Population', 'mean'].max()
min_p = grouped_sp['Population', 'mean'].min()
max_population = grouped_sp['Population', 'mean'].idxmax()
min_population = grouped_sp['Population', 'mean'].idxmin()
print(max_p)
print(min_p)
print(max_population)
print(min_population)
# Becuase index 4 is California, the state has a highest average population in 2013-2019, which is about 39162253.
# Because index 50 is Wyoming, the state has a lowest average population in 2013-2019, which is about 582032.

# Draw a plot about the population trend of each state in 2013-2019
grouped_sp['Population', 'mean'].plot(kind = 'line', color = 'skyblue', label = 'Population')
plt.ticklabel_format(style = 'plain')
plt.xlabel('The state name')
plt.ylabel('The population number')
plt.grid()
plt.legend()
plt.show()
# At the graph, populations of most states are under 15000000. The population of California is the highest in 2013-2019.
# The x axis represents states' indexs and the y axis represents the population number.

# Q2: What's the average population in each year during 2013-2019?
grouped_sn = search_year.filter(['State', 'Year', 'Population'])
grouped_sn = grouped_sn.groupby(['Year']).describe()
grouped_sn = grouped_sn.reset_index()
print(grouped_sn)
# The average population in 2013 is lowest. The average population in 2019 is highest.

# Plot a barplot for the average population in each year during 2013-2019
plt.bar(grouped_sn['Year'], grouped_sn['Population', 'mean'], color = 'orange', label = 'The number of population')
plt.xlabel('Year')
plt.ylabel('The average population')
plt.title('The average population during 2013-2019')
plt.grid()
plt.show()
# Through the graph, the trend of average population for all states is increasing by years.

# Q3: What's the average crime rate in each year during 2013-2019?
grouped_sc = search_year.filter(['State', 'Year', 'Rates of all crimes'])
grouped_sc = grouped_sc.groupby(['Year']).describe()
grouped_sc = grouped_sc.reset_index()
print(grouped_sc)
# The average crime rate in 2013 is highest. The average crime rate in 2019 is lowest.

# Plot a barplot for the average crime rate in each year during 2013-2019
plt.bar(grouped_sc['Year'], grouped_sc['Rates of all crimes', 'mean'], color = 'maroon', label = 'Rates of all crimes')
plt.xlabel('Year')
plt.ylabel('The average crime rate')
plt.title('The average crime rate during 2013-2019')
plt.show()
# Through the graph, the trend of average crime rate for all states is decreasing by years. 

# Q4: What is the relationship between the average population and the average crime rate in each year during 2013-2019?
# Plot a scatterplot for the average population and the average crime rate in each year during 2013-2019
x = grouped_sn['Population', 'mean']
y = grouped_sc['Rates of all crimes', 'mean']

plt.scatter(x, y, color = 'green')
plt.xlabel('The average population')
plt.ylabel('The average crime rate')
plt.title('The relationship between the average population and the average crime rate during 2013-2019')

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), color = 'red')
plt.show()
# Through the graph, the relationship between the average population and the average crime rate in each year during 2013-2019 is negative correlation.
# When the average population is increasing, the average crime rate is decreasing.

# Convert CSV to Excel
search_year.to_excel('/Users/mac/Downloads/state_crime.xlsx', index = None, header = True)