import requests
from django.shortcuts import render

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=98bcd33249fa8d189f0a429fe073bd37'
	city = 'Las Vegas'

	r =	requests.get(url.format(city))
	data = r.json()
	print(r)
	print(data)
	return render(request, 'weather/weather.html')