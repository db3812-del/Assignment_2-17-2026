
# ============================================================
# Homework Assignment: Data Formats and Access
# ============================================================

import requests
import json
import os

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

# Task 1: Print dates and temperatures
print("Date, Temperature")
for obs in data['observations']:
    print(f"{obs['date']}, {obs['temperature']}°F")

# Task 2: Average temperature
temps = [obs['temperature'] for obs in data['observations']]
avg_temp = sum(temps) / len(temps)
print(f"\nAverage temperature: {avg_temp:.1f}°F")

# Task 3: Days with precipitation
print("\nDays with precipitation:")
for obs in data['observations']:
    if obs['precipitation'] > 0:
        print(f"  {obs['date']}: {obs['precipitation']} inches")

# PART 2: File Downloads
# ============================================================

import pooch

file_path = pooch.retrieve(
    url="https://github.com/pandas-dev/pandas/raw/main/doc/data/air_quality_no2.csv",
    known_hash=None
)

# Task 1: Count lines
line_count = 0
with open(file_path) as f:
    for line in f:
        line_count += 1
print(f"\nNumber of lines: {line_count}")

# Task 2: Download NASA GISTEMP
my_url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
my_file = pooch.retrieve(url=my_url, known_hash=None)
print(f"Downloaded: {my_file}")

# PART 3: NetCDF Metadata
# ============================================================

base_url = "http://iridl.ldeo.columbia.edu/expert/SOURCES/.NOAA/.NCEP/.CPC/.UNIFIED_PRCP/.GAUGE_BASED/.GLOBAL/.v1p0/.Monthly/.RETRO/.rain/dods"

# Get DDS
dds_url = base_url + ".dds"
response = requests.get(dds_url)
print("\n=== DDS ===")
print(response.text[:500])

# Get DAS
das_url = base_url + ".das"
das_response = requests.get(das_url)
print("\n=== DAS ===")
print(das_response.text[:1000])
