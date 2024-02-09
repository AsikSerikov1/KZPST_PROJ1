from django.shortcuts import render
from .models import City
from .forms import CityForm


def home(request):
    city_info = None
    if 'city' in request.GET:
        form = CityForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data['city']
            city_info = {'name': city.name, 'address': city.address, 'phone': city.phone}
    else:
        default_city = City.objects.get(name="Алматы")
        form = CityForm(initial={'city': default_city.pk})
        city_info = {'name': default_city.name, 'address': default_city.address, 'phone': default_city.phone}
    return render(request, 'home.html', {'form': form, 'city_info': city_info})
