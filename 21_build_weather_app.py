from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("weather")
root.geometry("400x40")
root.configure(bg="green")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C7C129A2-2532-44B6-84B8-D82F8BC20191

try:
    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C7C129A2-2532-44B6-84B8-D82F8BC20191")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error"

my_label = Label(root, text=city+' Air Quality'+str(quality)+' '+category, font=('Helvetica', 20), bg='green')
my_label.pack()

root.mainloop()
