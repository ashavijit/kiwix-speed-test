#!/bin/bash

# Install required packages
sudo apt-get update
sudo apt-get -y install python3-pip
sudo pip3 install requests

# Download the Python script
wget https://raw.githubusercontent.com/ashavijit/kiwix-speed-test/blob/master/flask/app.py

# Define the cron job to run the script every 2 minutes
(crontab -l 2>/dev/null; echo "*/2 * * * * python3 /path/to/speedtest.py >> /path/to/results.json") | crontab -

# Display a message to the user
echo "Installation complete. The download speed testing script will run automatically every 2 minutes and save the results in results.json."
