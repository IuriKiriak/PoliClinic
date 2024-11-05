from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone


def index(request):
    return render(request, 'index.html')

def personal_page(request):
    return render(request, 'personal_page.html')

def edit_personal_date(request):
    return  render(request, 'personal_page.html')

def register_record(request):
    if request.method == "POST":
        name_records = request.POST["name_records"]
        # doctor = request.POST["doctor"]
        doctor = ""
        date = request.POST["date"]
        element = Records(name_records=name_records, date_record=date)
        element.save
        print(type(element))
        return render(request, 'recording_completed.html', { "name_records": name_records,
                                                                            "doctor": doctor,
                                                                            "date": date
        })
    elif request.method == "GET":
        pass

    return render(request, 'register_record.html')

