import json
import time

# Load the JSON file
with open('file.json', 'r') as file:
    data = json.load(file)

# Add an attribute to the JSON data


for i in range(5):
    current_time = time.strftime("%H:%M:%S")
    data[str(i)] = str(current_time)
    with open('file.json', 'w') as file:
        json.dump(data, file, indent=4)
    time.sleep(2)

# Write the updated JSON data back to the file

