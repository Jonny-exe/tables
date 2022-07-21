from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table

def index(request):
    # return HttpResponse("Hello  ")
    if request.method == "POST":
        print(request.POST)
        Table.objects.create(lat=request.POST["lat"], lng=request.POST["lng"])
        return redirect('/', permanent=True) # To avoid inserting the same item twice when doing F5

    print(Table.objects.all())
    return render(request, "tables/index.html", {"coordinates": Table.objects.all()})
def add(request):
    return render(request, "tables/add.html")