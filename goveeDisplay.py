import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Set the dark mode background and color palette
plt.style.use('dark_background')


# Read the data from a CSV file
data = pd.read_csv('data2.csv')

# Convert the Timestamp column to datetime format
data['Timestamp'] = pd.to_datetime(data['Timestamp for sample frequency every 1 min min'])

# Set the Timestamp column as the index of the dataframe
data.set_index('Timestamp', inplace=True)

# Plotting the temperature and humidity data
fig, ax1 = plt.subplots(figsize=(10, 4), dpi=150)

# Define color for temperature plot
color_temp = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature (Celsius)', color=color_temp)
ax1.plot(data.index, data[' Temperature_Celsius'], color=color_temp, linestyle='-', marker='', label='Temperature')
ax1.tick_params(axis='y', labelcolor=color_temp)

# Calculate and plot mean and median for temperature
temp_mean = data[' Temperature_Celsius'].mean()
# temp_median = data[' Temperature_Celsius'].median()
ax1.axhline(temp_mean, color='yellow', linestyle='-.', linewidth=1, label='Mean Temperature')
# ax1.axhline(temp_median, color='purple', linestyle='-.', linewidth=1, label='Median Temperature')

# Instantiate a second y-axis for the relative humidity
ax2 = ax1.twinx()
color_humid = 'tab:blue'
ax2.set_ylabel('Relative Humidity (%)', color=color_humid)
ax2.plot(data.index, data['Relative_Humidity'], color=color_humid, linestyle='--', marker='', label='Humidity')
ax2.tick_params(axis='y', labelcolor=color_humid)

# Calculate and plot mean and median for humidity
humid_mean = data['Relative_Humidity'].mean()
# humid_median = data['Relative_Humidity'].median()
ax2.axhline(humid_mean, color='green', linestyle='-.', linewidth=1, label='Mean Humidity')
# ax2.axhline(humid_median, color='cyan', linestyle='-.', linewidth=1, label='Median Humidity')

# Formatting Date on X-axis to handle hourly intervals
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Title, Legend, and Grid
plt.title('Temperature and Humidity Over Time')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(True, color='gray', linestyle=':', linewidth=0.5)

# Show the plot
plt.show()
