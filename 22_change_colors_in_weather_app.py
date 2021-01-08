from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("weather")
root.geometry("400x40")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C7C129A2-2532-44B6-84B8-D82F8BC20191

try:
    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=70801&distance=5&API_KEY=C7C129A2-2532-44B6-84B8-D82F8BC20191")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#FF9900"
    elif category == "Unheathy":
        weather_color = "#FF0000"
    elif category == "Very Unheathy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = '#660000'

    root.configure(bg=weather_color)

    my_label = Label(root, text=city+' Air Quality'+str(quality)+' '+category, font=('Helvetica', 20), bg=weather_color)
    my_label.pack()
except Exception as e:
    api = "Error"



root.mainloop()
