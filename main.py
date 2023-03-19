import time
import requests
import json
download_file = 'https://download.kiwix.org/release/kiwix-desktop/kiwix-desktop_windows_x64.zip'
# Define the testing locations and download file
testing_locations = [
    {'name': 'New York', 'url': download_file},
    {'name': 'London', 'url': download_file},
    {'name': 'Bangalore', 'url': download_file}
]
# download_file = 'https://download.kiwix.org/kiwix-desktop/daily/kiwix-desktop-win32.zip'

# Define an empty dictionary to store the download speed results
download_speeds = {}

# Define a function to test the download speed from a given location
def test_speed(location):
    start_time = time.time()
    response = requests.get(location['url'])
    end_time = time.time()
    download_time = end_time - start_time
    download_size_mb = round(len(response.content) / (1024 * 1024), 2)
    download_speed_mb = round(download_size_mb / download_time, 2)
    download_speeds[location['name']] = download_speed_mb
    
# Test the download speed from each location
for location in testing_locations:
    test_speed(location)

# Save the download speed results in a JSON file
with open('download_speeds.json', 'w') as f:
    json.dump(download_speeds, f)



# Print the download speed results
print(download_speeds)
