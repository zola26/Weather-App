from django.shortcuts import render, redirect
from weather_api.key import api_key
import requests
import math
# from .models import Social

# Create your views here.

def index(request):
    return render(request, "weather_api/home.html")




def result(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        w_dataset = requests.get(url).json()
        try:
            context = {
                ####
                "city_name":w_dataset["city"]["name"],
                "city_country":w_dataset["city"]["country"],
                "wind":w_dataset['list'][0]['wind']['speed'],
                "degree":w_dataset['list'][0]['wind']['deg'],
                "status":w_dataset['list'][0]['weather'][0]['description'],
                "cloud":w_dataset['list'][0]['clouds']['all'],
                'date':w_dataset['list'][0]["dt_txt"],
                'date1':w_dataset['list'][8]["dt_txt"],
                'date2':w_dataset['list'][16]["dt_txt"],
                'date3':w_dataset['list'][24]["dt_txt"],
                'date4':w_dataset['list'][32]["dt_txt"],
                # 'date5':w_dataset['list'][39]["dt_txt"],
                # 'date6':w_dataset['list'][48]["dt_txt"],


                "temp": round(w_dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(w_dataset["list"][8]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(w_dataset["list"][8]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(w_dataset["list"][16]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(w_dataset["list"][16]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(w_dataset["list"][24]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(w_dataset["list"][24]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(w_dataset["list"][32]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(w_dataset["list"][32]["main"]["temp_max"] -273.0),
                # "temp_min5":math.floor(w_dataset["list"][31]["main"]["temp_min"] -273.0),
                # "temp_max5": math.ceil(w_dataset["list"][31]["main"]["temp_max"] -273.0),
                # "temp_min6":math.floor(w_dataset["list"][39]["main"]["temp_min"] -273.0),
                # "temp_max6": math.ceil(w_dataset["list"][39]["main"]["temp_max"] -273.0),


                "pressure":w_dataset["list"][0]["main"]["pressure"],
                "humidity":w_dataset["list"][0]["main"]["humidity"],
                "sea_level":w_dataset["list"][0]["main"]["sea_level"],


                "weather":w_dataset["list"][1]["weather"][0]["main"],
                "description":w_dataset["list"][1]["weather"][0]["description"],
                "icon":w_dataset["list"][0]["weather"][0]["icon"],
                "icon1":w_dataset["list"][1]["weather"][0]["icon"],
                "icon2":w_dataset["list"][2]["weather"][0]["icon"],
                "icon3":w_dataset["list"][3]["weather"][0]["icon"],
                "icon4":w_dataset["list"][4]["weather"][0]["icon"],
                "icon5":w_dataset["list"][5]["weather"][0]["icon"],
                "icon6":w_dataset["list"][6]["weather"][0]["icon"],

            }
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather_api/results.html", context)
    else:
    	return redirect('home')



