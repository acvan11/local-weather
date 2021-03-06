import requests
from django.shortcuts import render
from .models import City

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=98bcd33249fa8d189f0a429fe073bd37'
	city = 'Las Vegas'

	cities = City.objects.all()

	weather_data = []

	for city in cities:		
		r =	requests.get(url.format(city)).json()

		city_weather = {
			'city': city,
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' :r['weather'][0]['icon'],
		}

		weather_data.append(city_weather)

	print(weather_data)
	
	context = {'city_weather': city_weather}
	return render(request, 'weather/weather.html', context)