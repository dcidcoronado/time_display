from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime

def root(request):
    return redirect ("/time_display")


def index(request):
    context = {
        "date": strftime("%d-%m, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

# Create your views here.
