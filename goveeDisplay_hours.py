import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Set the dark mode background and color palette
plt.style.use('dark_background')

# Read the data from a CSV file
data = pd.read_csv('data.csv')

# Clean up column names to remove extra spaces
data.columns = data.columns.str.strip()

# Convert the Timestamp column to datetime format using the correct column name
data['Timestamp'] = pd.to_datetime(data['Timestamp for sample frequency every 60 min min'])

# Set the Timestamp column as the index of the dataframe
data.set_index('Timestamp', inplace=True)

# Plotting the temperature and humidity data
fig, ax1 = plt.subplots(figsize=(12, 6), dpi=150)  # Increased the figure size

# Define color for temperature plot
color_temp = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature (Celsius)', color=color_temp)
ax1.plot(data.index, data['Temperature_Celsius'], color=color_temp, linestyle='-', marker='', label='Temperature')
ax1.tick_params(axis='y', labelcolor=color_temp)

# Calculate and plot mean for temperature
temp_mean = data['Temperature_Celsius'].mean()
ax1.axhline(temp_mean, color='yellow', linestyle='-.', linewidth=1, label='Mean Temperature')

# Instantiate a second y-axis for the relative humidity
ax2 = ax1.twinx()
color_humid = 'tab:blue'
ax2.set_ylabel('Relative Humidity (%)', color=color_humid)
ax2.plot(data.index, data['Relative_Humidity'], color=color_humid, linestyle='--', marker='', label='Humidity')
ax2.tick_params(axis='y', labelcolor=color_humid)

# Calculate and plot mean for humidity
humid_mean = data['Relative_Humidity'].mean()
ax2.axhline(humid_mean, color='green', linestyle='-.', linewidth=1, label='Mean Humidity')

# Further reduce the number of ticks on the x-axis
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=4))  # Show label every 4 days
ax1.xaxis.set_minor_locator(mdates.DayLocator(interval=8))  # Show minor ticks every 8 days
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Show only the date
ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

# Show grid for major ticks only and reduce density
ax1.grid(True, which='major', color='gray', linestyle='-', linewidth=0.5)  # Major gridlines only
ax1.grid(False, which='minor')  # Turn off minor gridlines

# Title, Legend, and Grid
plt.title('Temperature and Humidity Over Time')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()

