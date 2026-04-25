import requests
import json  
import os  

CONFIG_PATH = "config.json"

def get_data(city_name: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=2bf2e8aa6bbe3d941fc43499ab8e5306&units=metric&lang=ua")
    if response.status_code == 200:
        return response.json()
    

def get_weather(city_name: str):
    response1 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=ec4dfccc065b0295409a1be58b213307&units=metric&lang=ua")
    if response1.status_code == 200:
        return response1.json()
    
def load_cities():
    if not os.path.exists(CONFIG_PATH):
        return ["Dnipro"]

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("city_list", ["Dnipro"])

def save_cities(city_list):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump({"city_list": city_list}, f, ensure_ascii=False, indent=4)