from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, "newyear/index.html", {
        "date": now,
        "season" : get_season(now.month),
        "night" : now.hour >= 22 or now.hour <= 4
    })

def winter():
    return "WINTER"

def summer():
    return "SUMMER"

def autumn():
    return "AUTUMN"

def spring():
    return "SPRING"

switcher = {
    1: winter,
    2: winter,
    3: spring,
    4: spring,
    5: spring,
    6: summer,
    7: summer,
    8: summer,
    9: autumn,
    10: autumn,
    11: autumn,
    12: winter
}

def get_season(month):
    return switcher.get(month, lambda: "Invalid month")
