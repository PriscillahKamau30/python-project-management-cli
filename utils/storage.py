import json
import os

DATA_FILE = "data/data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    # Handle empty file
    if os.path.getsize(DATA_FILE) == 0:
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)