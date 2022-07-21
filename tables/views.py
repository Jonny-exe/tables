from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table

def index(request):
    # return HttpResponse("Hello  ")
    if request.method == "POST":
        lat, lng = float(request.POST["lat"]), float(request.POST["lng"])
        if request.POST["type"] == "add": # Add new marker
            Table.objects.create(lat=lat, lng=lng)
            return redirect('/', permanent=True) # To avoid inserting the same item twice when doing F5
        else: # Search in readius of marker
            radius = float(request.POST["radius"]) / 111.0 # Terrible longitude/latitude to km
            print(radius, type(radius))
            tables = Table.objects.all().filter(lng__lt=lng+radius, 
                                                lng__gt=lng-radius, 
                                                lat__lt=lat+radius,
                                                lat__gt=lat-radius)
    else:
        tables = Table.objects.all()

    return render(request, "tables/index.html", {"coordinates": tables})

def add(request):
    return render(request, "tables/add.html")

def search(request):
    return render(request, "tables/search.html")