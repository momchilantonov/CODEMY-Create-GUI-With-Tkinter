from tkinter import *
import requests
import json

root = Tk()
root.title("weather")
root.geometry("600x100")


def ziplookup():
    # zip.get()
    # zip_label = Label(root, text=zip.get())
    # zip_label.grid(row=1, column=1, columnspa=2)

    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C7C129A2-2532-44B6-84B8-D82F8BC20191

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=5&API_KEY=C7C129A2-2532-44B6-84B8-D82F8BC20191")
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

        my_label = Label(root, text=city+' Air Quality'+str(quality)+' '+category, font=('Helvetica', 20),
                         bg=weather_color)
        my_label.grid(row=1, column=0, columonspan=2)
    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zip_button = Button(root, text="Lookup Zipcode", command=ziplookup)
zip_button.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()
