import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/mac/Downloads/Merged Dataset.xlsx')
print(df.dtypes)

df = pd.DataFrame(df)
print(df.columns)

# Filter out labels of interest, group the data on state values and make a statistic description 
grouped_sn = df.filter(['Real GDP', 'Year', 'Rates of all crimes', 'Personal consumption expenditures', 'Per capita personal income'])
grouped_sn = grouped_sn.groupby(['Year']).describe()
grouped_sn = grouped_sn.reset_index()
print(grouped_sn)

# Extract the year, crime rates and real GDP
years = grouped_sn['Year']
crime_rates = grouped_sn['Rates of all crimes', 'mean']
real_GDP = grouped_sn['Real GDP', 'mean']

# Create a line plot to show the relationship between the real GDP and the crime rates
fig, ax1 = plt.subplots(figsize = (8, 6))

ax1.plot(years, crime_rates, color = 'skyblue', marker='.', markersize=12, label = 'Crime rates')
ax1.set_xlabel('Years')
ax1.set_ylabel('The Crime Rates')
ax1.legend()

ax2 = ax1.twinx()

ax2.plot(years, real_GDP, color = 'orange', marker = '.', markersize = 12, label = 'Real GDP')
ax2.set_xlabel('Years')
ax2.set_ylabel('The Real GDP')
ax2.legend()

plt.title('The Real GDP vs The Crime Rates during 2013-2019')
plt.show()

# Filter out labels of interest, group the data on state values and make a statistic description 
grouped_sp = df.filter(['State', 'Personal consumption expenditures', 'Per capita personal income'])
grouped_sp = grouped_sp.groupby(['State']).describe()
grouped_sp = grouped_sp.reset_index()
print(grouped_sp)

states = grouped_sp['State']
consumption_expenditures = grouped_sp['Personal consumption expenditures', 'mean']
per_capita_income = grouped_sp['Per capita personal income', 'mean']

# Creat a scatter plot to show the relationship between the personal consumption expenditures and the per capita personal income
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), color = 'red')
plt.show()

z = grouped_sn['Personal consumption expenditures', 'mean']
e = grouped_sn['Rates of all crimes', 'mean']

plt.scatter(z, e, color = 'green')
plt.xlabel('The personal consumption expenditures')
plt.ylabel('Rates of all crimes')
plt.title('The relationship between personal consumption expenditure and rates of all crimes during 2013-2019')

h = np.polyfit(z, e, 1)
p = np.poly1d(h)
plt.plot(z, p(z), color = 'red')
plt.show()