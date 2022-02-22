import requests
from django.shortcuts import render, redirect, get_object_or_404

from weather_application.webapp.forms import AddCity, DeleteCity
from weather_application.webapp.models import City


def index(request):
    data = []
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5fcf342ac5bdc0962be23aa69e739dc2'

    if request.method == 'POST':
        form = AddCity(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddCity()

    cities = City.objects.all()

    for city in cities:
        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'id': city.id,
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        data.append(city_weather)

    context = {
        'form': form,
        'data': data,
    }

    return render(request, 'weather.html', context)


def delete_city(request, pk):
    obj = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        form = DeleteCity(request.POST, instance=obj)
        if form.is_valid():
            obj.delete()
            return redirect('index')
    else:
        form = DeleteCity(instance=obj)

    context = {
        'obj': obj,
        'form': form,
    }
    return render(request, 'delete.html', context)
