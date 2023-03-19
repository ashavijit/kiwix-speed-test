import subprocess
import csv
import json

locations = [
    (51.5074, -0.1278),  # London
    (40.7128, -74.0060),  # New York
    (-33.8688, 151.2093),  # Sydney
    (19.4326, -99.1332),  # Mexico City
    (-23.5505, -46.6333), # São Paulo
    (22.5726, 88.3639)  #kolkata    
]

test_url="https://www.kiwix.org/en/download/"

res={}

with open("res.csv", "w") as f:
    fielnames=["lat","lon","download_speed"]
    writer = csv.DictWriter(f, fieldnames=fielnames)
    writer.writeheader()

    for location in locations:
        latitude , longitude = location
        print("Testing location: {}, {}".format(latitude, longitude))

        # command="speedtest-cli --csv --server 1000 --lat {} --lon {}".format(latitude,longitude)
        command= f"wget {test_url} --output-document=/dev/null --quiet --show-progress"
        process=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        process.wait()


        if b'MB/s' in output:
            download_speed = output.split(b" ")[-2].decode("utf-8")
            print("Download speed: {} MB/s".format(download_speed))
            writer.writerow({"lat":latitude,"lon":longitude,"download_speed":download_speed})
        
        else:
            print("Download speed: Unknown")
            writer.writerow({"lat":latitude,"lon":longitude,"download_speed":"Unknown"})
            

