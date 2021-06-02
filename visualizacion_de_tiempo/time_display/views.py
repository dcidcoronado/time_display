from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime
from datetime import datetime

def root(request):
    return redirect ("/time_display")


def index(request):
    context = {
        "date": strftime("%d-%m, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html', context)


def time(request):
    now = datetime.now()
    context = {
        "datetime": now
    }
    return render(request, 'fecha.html', context)

# Create your views here.
