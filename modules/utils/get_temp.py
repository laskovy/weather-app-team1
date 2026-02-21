from .api import get_data 

def get_temp():
    data = get_data("Dnipro")
    list_weather = data.get("list")
    min_temp = 100
    list_temp = []
    for weather in list_weather:
        temp = int(weather.get("main").get("temp"))
        list_temp.append(temp)
        if temp < min_temp:
            min_temp = temp
    min_visible_temp = (round(min_temp/5)*5) - 10
    list_height = []
    for temp in list_temp:
        height = round((temp - min_visible_temp) * 2.874)
        list_height.append(height) 

    return min_visible_temp, list_height 


    