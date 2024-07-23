'''Q.  Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
'''

import numpy as np

# Input temperatures
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature > 35 degrees Celsius)
hot_days = temperatures > 35

# Identify cold days (temperature < 5 degrees Celsius)
cold_days = temperatures < 5

# Combine hot days and cold days conditions
extreme_days = hot_days | cold_days

# Get indices of extreme days
extreme_days_indices = np.where(extreme_days)[0]

# Display the result
print("Days with extreme temperature conditions (hot days or cold days):")
print(extreme_days_indices)


'''
Output:-

Days with extreme temperature conditions (hot days or cold days):
[2 5 9]

'''
