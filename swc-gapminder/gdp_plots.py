import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows
data = pandas.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country').T

# create a plot of the transposed data
ax = data.plot()

# display the plot
plt.show()
