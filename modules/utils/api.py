import requests

def get_data(city_name: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=2bf2e8aa6bbe3d941fc43499ab8e5306&units=metric&lang=ua")
    if response.status_code == 200:
        return response.json()
    