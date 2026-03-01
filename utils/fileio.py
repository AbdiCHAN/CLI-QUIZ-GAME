# utils/fileio.py
# Handles loading and saving JSON files

import json  # Built-in module for JSON handling


def load_json(filepath):
    """
    Load data from a JSON file.
    Returns a Python object (list/dict).
    Returns empty list if file not found.
    """
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_json(filepath, data):
    """
    Save Python object (list/dict) into a JSON file.
    """
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)