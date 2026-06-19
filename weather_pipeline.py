import json
import requests


def run_weather_pipeline(city: str, temp_threshold: float):
    print(f"--- Starting Weather Pipeline for {city.title()} ---")

    # extract raw JSON data from the API
    # wttr.in gives clean JSON if appended
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        response.raise_for_status()  # checks for HTTP errors
        raw_data = response.json()
        print("[SUCCESS] Data extracted from API.")
    except Exception as e:
        print(f"[ERROR] Failed to extract data: {e}")
        return