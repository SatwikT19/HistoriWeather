import requests

base_url = "https://archive-api.open-meteo.com/v1/archive?"

def get_day_temps(latitude, longitude, date):
    url = (
        f"{base_url}"
        f"latitude={latitude}&longitude={longitude}"
        f"&start_date={date}&end_date={date}"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&timezone=auto"
    )
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temps = data.get("daily", {})
        print("Success!")
        return temps
    else:
        print(f"Unable to retrieve data: {response.status_code}")
        return None

# Example: Toronto on Aug 1, 2023
print(get_day_temps(43.690685, -79.41174, "2023-08-01"))
