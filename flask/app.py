from flask import Flask, jsonify
import time
import requests
import json
from datetime import datetime

app = Flask(__name__)
download_file = 'https://download.kiwix.org/release/kiwix-desktop/kiwix-desktop_windows_x64.zip'
# Define the testing locations and download file
testing_locations = [
    {'name': 'New York', 'url': download_file},
    {'name': 'London', 'url': download_file},
    {'name': 'Bangalore', 'url': download_file}
]
# download_file = 'https://download.kiwix.org/kiwix-desktop/daily/kiwix-desktop-win32.zip'

# Define a function to test the download speed from a given location
def test_speed(location):
    start_time = time.time()
    response = requests.get(location['url'])
    end_time = time.time()
    download_time = end_time - start_time
    download_size_mb = round(len(response.content) / (1024 * 1024), 2)
    download_speed_mb = round(download_size_mb / download_time, 2)
    return {'name': location['name'], 'speed': download_speed_mb}

# Define a route to run the download speed test and save the results in a JSON file
@app.route('/test')
def run_test():
    # Test the download speed from each location
    download_speeds = [test_speed(location) for location in testing_locations]

    # Save the download speed results in a JSON file with a timestamp in the file name
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'download_speeds_{timestamp}.json'
    with open(file_name, 'w') as f:
        json.dump(download_speeds, f)

    # Return the download speed results as a JSON response
    return jsonify(download_speeds)

if __name__ == '__main__':
    app.run(debug=True)
