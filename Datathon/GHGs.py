import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the data from the CSV file
data = pd.read_csv("GHGs.csv")

# Filter the data for relevant emissions
emission_data = data[data['Domain Code'] == 'GT']  # Filter by Domain Code 'GT'

# Convert 'Year' column to datetime format
emission_data['Year'] = pd.to_datetime(emission_data['Year'], format='%Y')

# Group the data by year and calculate the sum of emissions
yearly_emissions = emission_data.groupby('Year')['Value'].sum()

# Create a line plot to visualize emissions year by year
plt.figure(figsize=(10, 6))
plt.plot(yearly_emissions.index, yearly_emissions.values, marker='o')
plt.title('GHGs Emissions Year by Year')
plt.xlabel('Year')
plt.ylabel('Total Emissions (kt)')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))
plt.grid(True)
plt.show()
