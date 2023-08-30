import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv("riceUsage.csv")

# Filter the data for rows related to rice usage
rice_data = data[data['Item'].str.contains('rice', case=False, na=False)]

# Group the data by year and calculate the sum of rice usage
yearly_rice_usage = rice_data.groupby('Year')['Value'].sum()

# Create a line plot to visualize total rice usage year by year
plt.figure(figsize=(10, 6))
plt.plot(yearly_rice_usage.index, yearly_rice_usage.values, marker='o')
plt.title('Total Rice Usage Year by Year')
plt.xlabel('Year')
plt.ylabel('Total Rice Usage')
plt.grid(True)
plt.show()
