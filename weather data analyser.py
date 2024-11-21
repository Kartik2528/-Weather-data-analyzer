import pandas as pd

try:
    weather_data = pd.read_csv('weather_data.csv')
except FileNotFoundError:
    print("Error: The file 'weather_data.csv' was not found.")
    exit()

if 'Date/Time' not in weather_data.columns or 'Temp_C' not in weather_data.columns:
    print("Error: The CSV file must contain 'Date/Time' and 'Temp_C' columns.")
    exit()

try:
    weather_data['Temp_C'] = pd.to_numeric(weather_data['Temp_C'], errors='coerce')
    avg_temp = weather_data['Temp_C'].mean()
    max_temp = weather_data['Temp_C'].max()
    min_temp = weather_data['Temp_C'].min()
    hottest_day = weather_data.loc[weather_data['Temp_C'] == max_temp, 'Date/Time'].iloc[0]
    coldest_day = weather_data.loc[weather_data['Temp_C'] == min_temp, 'Date/Time'].iloc[0]
    print("\nWeather Data Summary:")
    print(f"- Average Temperature: {avg_temp:.2f}°C")
    print(f"- Hottest Day: {hottest_day} with {max_temp}°C")
    print(f"- Coldest Day: {coldest_day} with {min_temp}°C")
except Exception as e:
    print(f"An error occurred during analysis: {e}")
