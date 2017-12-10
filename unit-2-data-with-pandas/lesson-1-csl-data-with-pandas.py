# Create a DataFrame I

#import codecademylib
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print df1

# Create a DataFrame II

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=['Store ID', 'Location', 'Number of Employees'])

print df2

# Loading Data

"""cupcakes.csv

name,cake_flavor,frosting_flavor,topping
Devil's Food,chocolate,chocolate,chocolate shavings
Birthday Cake,vanilla,vanilla,rainbow sprinkles
Carrot Cake,carrot,cream cheese,almonds
"""

# Loading and Saving CSVs

df = pd.read_csv('csv/sample.csv')
print df

# Inspect a DataFrame

df = pd.read_csv('csv/imdb.csv')
print df.head()
print df.info()

# Select Columns

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north
# can also do
# clinic_north = df['clinic_north']

print type(clinic_north)
print type(df)

# Selecting Multiple Columns

clinic_north_south = df[['clinic_north', 'clinic_south']]
print type(clinic_north_south)

# Select Rows

march = df.loc[2]

# Selecting Multiple Rows

april_may_june = df[3:]
print april_may_june

# Select Rows with Logic I

january = df[df.month == 'January']
print january

# Select Rows with Logic II

march_april = df[ (df.month == 'March') | (df.month == 'April') ]

print march_april

# Select Rows with Logic III

january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print january_february_march

# Setting indices

df2 = df.loc[[1, 3, 5]]
print df2

df3 = df2.reset_index()
print df3

df2.reset_index(inplace=True, drop=True)
print df2

# Review

orders = pd.read_csv('csv/shoefly.csv')
print orders.head()

emails = orders.email
print emails

frances_palmer = orders[ (orders.first_name == 'Frances') & (orders.last_name == 'Palmer') ]
print frances_palmer

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
print comfy_shoes