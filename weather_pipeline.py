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
    
    #transform
    try:
        # Navigate JSON structure to get current conditions
        current_condition = raw_data["current_condition"][0]

        temp_c = float(current_condition["temp_C"])
        humidity = int(current_condition["humidity"])
        weather_desc = current_condition["weatherDesc"][0]["value"]

        # Forms a clean, structured dictionary
        processed_data = {
            "city": city.title(),
            "temperature_c": temp_c,
            "humidity_percent": humidity,
            "condition": weather_desc,
            "is_alert_triggered": temp_c > temp_threshold,
        }

        print("[SUCCESS] Data transformation complete.")

    except KeyError as e:
        print(f"[ERROR] JSON structure changed or field missing: {e}")
        return