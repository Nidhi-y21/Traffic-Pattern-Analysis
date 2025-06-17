# Traffic Pattern Analysis Using Synthetic GPS Data

This project simulates GPS-based vehicle tracking data for a city over a week and analyzes traffic patterns using Python. It generates synthetic data and visualizes it using static plots with matplotlib and seaborn.

## Features

* Generates synthetic GPS data for 100 vehicles over 7 days.
* Saves GPS data to a CSV file (`gps_traffic_data.csv`).
* Visualizes:

  * Traffic density as a 2D heatmap (weighted by speed).
  * Hourly average speed across the day.
  * Comparison of average speed between daytime and nighttime.

## Dependencies

* Python 3.x
* pandas
* numpy
* matplotlib
* seaborn

Install dependencies using:

```bash
pip install pandas numpy matplotlib seaborn
```

## How It Works

1. **Data Generation**: Creates timestamped latitude/longitude data for vehicles with simulated speeds.
2. **Data Storage**: Outputs all records to a CSV.
3. **Analysis & Visualization**:

   * Heatmap shows where traffic is most dense based on location and speed.
   * Line plot tracks average speed by hour.
   * Bar plot compares average speed between daytime (6AM–6PM) and nighttime.

## Usage

Run the script using:

```bash
python traffic_analysis.py
```

It will:

* Create and save `gps_traffic_data.csv`
* Display 3 static plots in sequence

## Notes

* Time and speed logic simulate urban traffic with congestion peaking mid-day.
* Coordinates are centered around New Delhi for simulation purposes.

## License

MIT License
