from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello  ")
    return render(request, "tables/index.html", {"coordinates": [["40.463667", "39.399872"], ["39.399872", "-8.224454"]]})