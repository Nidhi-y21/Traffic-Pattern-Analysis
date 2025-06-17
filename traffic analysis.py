import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

# Generate synthetic GPS data
np.random.seed(42)
vehicle_ids = [f'VEH{i}' for i in range(1, 101)]
base_lat, base_lon = 28.6139, 77.2090  # Generic city center (e.g., New Delhi)

records = []
start_date = datetime(2024, 1, 1)
for day in range(7):
    for hour in range(24):
        for _ in range(random.randint(100, 200)):
            vid = random.choice(vehicle_ids)
            lat = base_lat + np.random.normal(0, 0.01)
            lon = base_lon + np.random.normal(0, 0.01)
            speed = abs(np.random.normal(loc=40 - 10 * abs(hour - 12) / 12, scale=5))  # peak congestion mid-day
            timestamp = start_date + timedelta(days=day, hours=hour, minutes=random.randint(0, 59))
            records.append([vid, lat, lon, speed, timestamp])

# Create DataFrame
df = pd.DataFrame(records, columns=['VehicleID', 'Latitude', 'Longitude', 'Speed', 'Timestamp'])
df['Hour'] = df['Timestamp'].dt.hour
df['Day'] = df['Timestamp'].dt.day_name()
df.to_csv("gps_traffic_data.csv", index=False)
print(df.head())

# Heatmap of GPS density (as 2D histogram)
plt.figure(figsize=(10, 6))
plt.hist2d(df['Longitude'], df['Latitude'], bins=100, weights=df['Speed'], cmap='viridis')
plt.colorbar(label='Average Speed')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Traffic Density Heatmap (Static)')
plt.tight_layout()
plt.show()

# Average speed by hour
speed_hour = df.groupby('Hour')['Speed'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=speed_hour, x='Hour', y='Speed', marker='o')
plt.title('Average Speed by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Average Speed')
plt.grid(True)
plt.tight_layout()
plt.show()

# Day vs Night comparison
conditions = [df['Hour'].between(6, 18), ~df['Hour'].between(6, 18)]
choices = ['Day', 'Night']
df['Period'] = np.select(conditions, choices)
speed_period = df.groupby('Period')['Speed'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(data=speed_period, x='Period', y='Speed', palette='Set2')
plt.title('Day vs Night Average Speed')
plt.xlabel('Period')
plt.ylabel('Average Speed')
plt.tight_layout()
plt.show()

print("✅ Static charts displayed successfully using matplotlib and seaborn.")
