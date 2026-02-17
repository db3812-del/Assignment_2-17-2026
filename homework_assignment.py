# ============================================================
# Homework Assignment: Data Formats and Access
# ============================================================
import requests
import json
import os

# ============================================================
# PART 1: Working with JSON Data
# ============================================================
sample_json = '''
{
  "station": "USC00305800",
  "name": "New York Central Park",
  "location": {"latitude": 40.7789, "longitude": -73.9692},
  "observations": [
    {"date": "2023-01-01", "temperature": 32, "precipitation": 0.0},
    {"date": "2023-01-02", "temperature": 28, "precipitation": 0.5},
    {"date": "2023-01-03", "temperature": 35, "precipitation": 0.0},
    {"date": "2023-01-04", "temperature": 38, "precipitation": 0.2},
    {"date": "2023-01-05", "temperature": 41, "precipitation": 0.0}
  ]
}
'''

data = json.loads(sample_json)

# 1. Extract and print all dates and temperatures (8 points)
print("Date, Temperature")
for obs in data['observations']:
    # YOUR CODE HERE
    print(f"{obs['date']}, {obs['temperature']}°F")

# 2. Calculate average temperature (8 points)
total_temp = 0
count = 0
# YOUR CODE HERE
for obs in data['observations']:
    total_temp += obs['temperature']
    count += 1
avg_temp = total_temp / count
print(f"Average temperature: {avg_temp:.1f}°F")

# 3. Find days with precipitation (9 points)
print("\nDays with precipitation:")
# YOUR CODE HERE
for obs in data['observations']:
    if obs['precipitation'] > 0:
        print(f"  {obs['date']}: {obs['precipitation']} inches")

# 4. Real API - Open-Meteo
# YOUR CODE HERE
url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true"
response = requests.get(url)
if response.status_code == 200:
    api_data = response.json()
    current = api_data['current_weather']
    print("\nSuccessfully connected to Open-Meteo API!")
    print(f"Location: New York City")
    print(f"Current Temperature: {current['temperature']}°C")
    print(f"Wind Speed: {current['windspeed']} km/h")

# ============================================================
# PART 2: Downloading Files with Python
# ============================================================
import pooch

file_path = pooch.retrieve(
    url="https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_no2.csv",
    known_hash=None
)

print("\nFile downloaded to:", file_path)

# 1. Verify the file was downloaded (5 points)
file_size = os.path.getsize(file_path)
print(f"File size: {file_size} bytes")

# YOUR CODE HERE
line_count = 0
with open(file_path) as f:
    for line in f:
        line_count += 1
print(f"Number of lines: {line_count}")

# 2. Download another file (10 points)
# YOUR CODE HERE
my_url = "https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv"
my_file = pooch.retrieve(url=my_url, known_hash=None)
print(f"Downloaded: {my_file}")

# 3. Create a data inventory (5 points)
print("\nData Inventory:")
print("1. meteorites.csv - NASA meteorite landings")
print("2. air_quality_no2.csv - Air quality NO2 measurements")
# YOUR CODE HERE
print("3. monthly.csv - Global Temperature Anomalies (NASA/GISS)")

# ============================================================
# PART 3: Understanding NetCDF Metadata
# ============================================================
base_url = "http://iridl.ldeo.columbia.edu/expert/SOURCES/.NOAA/.NCEP/.CPC/.UNIFIED_PRCP/.GAUGE_BASED/.GLOBAL/.v1p0/.Monthly/.RETRO/.rain/dods"

# Get DDS (Dataset Descriptor Structure)
dds_url = base_url + ".dds"
response = requests.get(dds_url)
print("\nDataset Structure:")
print(response.text[:500])

# 2. Get data attributes (5 points)
das_url = base_url + ".das"
# YOUR CODE HERE
das_response = requests.get(das_url)
print("\nDataset Attributes:")
print(das_response.text[:1000])
