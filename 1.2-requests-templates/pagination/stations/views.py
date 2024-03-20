import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # путь к файлу хранится в настройках
    csv_file_path = settings.BUS_STATION_CSV

    # читаем csv-файл в кодировке utf-8
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)

    paginator = Paginator(stations, 10)  # по 10 остановок на страницу
    page = int(request.GET.get('page',1))
    bus_stations = paginator.get_page(page)

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }

    return render(request, 'stations/index.html', context)