import csv
import json

# Read the CSV file and convert it to JSON
def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Open the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        # Use csv.DictReader to read the CSV file and map the header row as keys
        csv_reader = csv.DictReader(file)

        # Convert each row to a dictionary and append to the data list
        for row in csv_reader:
            data.append(row)

    # Write the JSON data to a file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"CSV data has been converted to JSON and saved to {json_file_path}")

# Provide the file paths for the input CSV and output JSON files
csv_file_path = 'food-truck-data.csv'  # Path to your CSV file
json_file_path = 'data.json'  # Path to the output JSON file

# Convert the CSV data to JSON
csv_to_json(csv_file_path, json_file_path)